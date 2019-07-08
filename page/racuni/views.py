from django.shortcuts import render, HttpResponse, redirect
#from django.contrib.auth.models import User
import page.racuni.user_manage as user_manage


def login(request):
    return render(request, "racuni/login.html")


class element:
    def __init__(self, arg):
        self.name = arg


def homepage(request):
    if not user_manage.input_validate(request.POST):
        return redirect('./login')
    if request.POST['confirm'] == 'register':
        pass
    context = {"receipts": [element(request.POST['username']), element(request.POST['password'])]}
    return render(request, "racuni/homepage.html", context)


def settings(request):
    return render(request, "racuni/settings.html")


def form_input(request):
    return render(request, "racuni/form_input.html")


def form_input_anonymous(request):
    return render(request, "racuni/form_input_anonymous.html")


def result(request):
    
    return render(request, "racuni/result.html")
