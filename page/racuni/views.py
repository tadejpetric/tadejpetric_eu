from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, "racuni/index.html")


def form_input(request):
    return render(request, "racuni/form_input.html")


def result(request):
    return render(request, "racuni/result.html")
