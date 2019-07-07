from django.shortcuts import render, HttpResponse


def login(request):
    return render(request, "racuni/login.html")


class element:
    def __init__(self, arg):
        self.name = arg

def homepage(request):
    receipts = [element("test"), element("wow")]
    return render(request, "racuni/homepage.html", receipts = receipts)


def settings(request):
    return render(request, "racuni/settings.html")


def form_input(request):
    return render(request, "racuni/form_input.html")


def form_input_anonymous(request):
    return render(request, "racuni/form_input_anonymous.html")


def result(request):
    return render(request, "racuni/result.html")
