from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
import page.racuni.user_manage as user_manage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import logout
import page.racuni.receipt_manage as receipt_manage


def login(request):
    # Message passing for error signaling
    special = request.POST.get('special', '')
    if special == 'logout':
        logout(request)
        return redirect('./login')

    return render(request, 'racuni/login.html')


def homepage(request):
    confirm_post = request.POST.get('confirm')
    if confirm_post == 'register':
        # add register successful/ unsuccessful
        if user_manage.register(request.POST):
            return render(request, './login')
        return render(request, './login')
    if confirm_post == 'login':
        if not user_manage.input_validate(request.POST):
            return redirect('./login')
        if not user_manage.login_ses(request):
            return redirect('./login')
    if not request.user.is_authenticated:
        return redirect('./login')

    if confirm_post == 'delete':
        pk = request.POST.get('pk')
        if pk is not None:
            receipt_manage.delete(pk=pk, uname=request.user.username)
    # request.user.username is username
    context = {"receipts": receipt_manage.receipts_list(request.user.username)[::-1], "username": request.user.username}
    return render(request, 'racuni/homepage.html', context)


def settings(request):
    return render(request, 'racuni/settings.html')


def form_input(request):
    if not request.user.is_authenticated:
        return redirect('./login')
    form_type = request.POST.get('form_type', 'new')

    preset = receipt_manage.Preset()
    if form_type == 'new':
        # loads the preset from the saved template
        preset.new_logged_in(request.user.username)
    else:
        # for editing
        if 'pk' not in request.POST:
            return redirect('./homepage')  # add error message
        preset.saved_logged_in(request.user.username, request.POST['pk'])
    context = {'form_type': form_type, 'preset': preset}
    return render(request, 'racuni/form_input.html', context)


def form_input_anonymous(request):
    preset = receipt_manage.Preset()

    context = {'preset': preset, 'form_type': 'anon'}
    return render(request, 'racuni/form_input.html', context)


def result(request):
    action = request.POST.get('action')
    if action == 'save':
        pk = request.POST.get('pk')
        if pk is None:
            # We enter here if making new receipt
            receipt_manage.save_new_to_db(request.POST, request.user.username)
        # here if editing existing receipt
        else:
            receipt_manage.edit_receipt(request.POST, request.user.username, pk)
        return redirect('./homepage')
    if action == 'print':
        context = {}
        return render(request, 'racuni/result.html', context)
        pass
    return redirect('./login')
