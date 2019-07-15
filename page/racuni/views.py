from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
import page.racuni.user_manage as user_manage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import logout
import page.racuni.receipt_manage as receipt_manage


def login(request):
    try:
        if request.POST['special'] == 'logout':
            logout(request)
            return redirect('./login')
    except MultiValueDictKeyError:
        pass
    return render(request, 'racuni/login.html')


class element:
    def __init__(self, arg):
        self.name = arg


def homepage(request):
    try:
        if request.POST['confirm'] == 'register':
            # add register successful/ unsuccessful
            if user_manage.register(request.POST):
                return render(request, './login')
            return render(request, './login')
        if request.POST['confirm'] == 'login':
            if not user_manage.input_validate(request.POST):
                return redirect('./login')
            if not user_manage.login_ses(request):
                return redirect('./login')
    except MultiValueDictKeyError:
        pass

    if not request.user.is_authenticated:
        return redirect('./login')
    # request.user.username is username
    context = {"receipts": receipt_manage.receipts_list(request.user.username)}
    return render(request, 'racuni/homepage.html', context)


def settings(request):
    return render(request, 'racuni/settings.html')


def form_input(request):
    if not request.user.is_authenticated:
        return redirect('./login')
    form_type = 'new'
    try:
        # POST['form_type'] only gets set on editing to 'edit'
        form_type = request.POST['form_type']
        # I could've put setting preset here and in the except. Pretty?
    except MultiValueDictKeyError:
        pass
    
    preset = receipt_manage.Preset()
    context = {'form_type': form_type}
    if form_type == 'new':
        # loads the preset from the saved template
        preset.new_logged_in(request.user.username)
    else:
        if 'pk' not in request.POST:
            return redirect('./homepage')  # add error message
        preset.saved_logged_in(request.user.username, request.POST['pk'])
    return render(request, 'racuni/form_input.html', context)


def form_input_anonymous(request):
    preset = receipt_manage.Preset()

    context = {'preset': preset, 'form_type': 'anon'}
    return render(request, 'racuni/form_input.html', context)
    # return render(request, "racuni/form_input_anonymous.html")


def result(request):
    return render(request, 'racuni/result.html')
