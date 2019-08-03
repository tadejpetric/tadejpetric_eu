from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
import page.racuni.user_manage as user_manage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import logout
import page.racuni.receipt_manage as receipt_manage


def login(request):
    if request.POST.get('special') == 'logout':
        logout(request)
        return redirect('./login')
    
    if request.user.is_authenticated:
        return redirect('./homepage')
    context = {'message': "", 'colour': "", 'status': False}

    success_colour = '#90e25d'
    fail_colour = '#f25232'

    loging = request.GET.get('login')
    if loging == 'False':
        context['message'] = 'Prijava neuspešna'
        context['colour'] = fail_colour
        context['status'] = True
    registerg = request.GET.get('register')
    if registerg == 'True':
        context['message'] = 'Registracija uspešna'
        context['colour'] = success_colour
        context['status'] = True
    if registerg == 'False':
        context['message'] = 'Registracija neuspešna'
        context['colour'] = fail_colour
        context['status'] = True
    loggedg = request.GET.get('logged')
    if loggedg == 'False':
        context['message'] = 'Za dostop te strani morate biti prijavljeni'
        context['colour'] = fail_colour
        context['status'] = True

    return render(request, 'racuni/login.html', context)


def homepage(request):
    confirm_post = request.POST.get('confirm')
    if confirm_post == 'register':
        # add register successful/ unsuccessful
        if user_manage.register(request.POST):
            return redirect('./login?register=True')
        return redirect('./login?register=False')
    if confirm_post == 'login':
        if not user_manage.input_validate(request.POST):
            return redirect('./login?login=False')
        if not user_manage.login_ses(request):
            return redirect('./login?login=False')
    if not request.user.is_authenticated:
        return redirect('./login?logged=False')

    if confirm_post == 'delete':
        pk = request.POST.get('pk')
        if pk is not None:
            receipt_manage.delete(pk=pk, uname=request.user.username)
    if confirm_post == 'settings':
        receipt_manage.set_settings(uname=request.user.username, post_data=request.POST)
    # request.user.username is username
    context = {"receipts": receipt_manage.receipts_list(request.user.username), "username": request.user.username}
    return render(request, 'racuni/homepage.html', context)


def form_input(request):
    if not request.user.is_authenticated:
        return redirect('./login?logged=False')
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
        preset.prepare_edit()
    context = {'form_type': form_type, 'preset': preset}
    return render(request, 'racuni/form_input.html', context)


def form_input_anonymous(request):
    preset = receipt_manage.Preset()

    context = {'preset': preset, 'form_type': 'anon'}
    return render(request, 'racuni/form_input.html', context)


def result(request):
    action = request.POST.get('action')
    pk = request.POST.get('pk')
    if action == 'save':
        pk = request.POST.get('pk')
        if pk is None:
            # We enter here if making new receipt
            receipt_manage.save_new_to_db(request.POST, request.user.username)
        # here if editing existing receipt
        else:
            receipt_manage.edit_receipt(request.POST, request.user.username, pk)
        return redirect('./homepage')
    if action == 'print' and request.user.is_authenticated and pk is not None:
        preset = receipt_manage.Preset()
        preset.saved_logged_in(request.user.username, pk)
        preset.prepare_print()
        context = {'preset': preset}
        return render(request, 'racuni/result.html', context)
    return redirect('./login')


def settings(request):
    if not request.user.is_authenticated:
        return redirect('./login?logged=False')
    preset = receipt_manage.Preset()
    preset.new_logged_in(request.user.username)
    context = {'preset': preset}
    return render(request, 'racuni/settings.html', context)


def statistics(request):
    if not request.user.is_authenticated:
        return redirect('./login?logged=False')
    uname = request.user.username
    context = {}
    monthly, maximum = receipt_manage.monthly_earnings(uname)
    context['max_per_month'] = maximum
    context['monthly'] = monthly
    average, count = receipt_manage.avg_value_count(uname)
    context['average'] = average
    context['count'] = count
    context['total'] = average * count
    return render(request, 'racuni/statistics.html', context)
