from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
import page.racuni.user_manage as user_manage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import logout
import receipt_manage


def login(request):
    try:
        if request.POST['special'] == 'logout':
            logout(request)
            return redirect('./login')
    except MultiValueDictKeyError:
        pass
    return render(request, "racuni/login.html")


class element:
    def __init__(self, arg):
        self.name = arg


def homepage(request):
    try:
        if request.POST['confirm'] == 'register':
            # add register successful/ unsuccessful
            if user_manage.register(request.POST):
                return render(request, './login.html')
            return render(request, './login.html')
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
    return render(request, "racuni/homepage.html", context)


def settings(request):
    return render(request, "racuni/settings.html")


def form_input(request):
    try:
        if request.POST['']:
            pass
    except MultiValueDictKeyError:
        pass
    return render(request, "racuni/form_input.html")


def form_input_anonymous(request):
    if not request.user.is_authenticated:
        return redirect('./login')
    
    return render(request, "racuni/form_input_anonymous.html")


def result(request):
    return render(request, "racuni/result.html")
