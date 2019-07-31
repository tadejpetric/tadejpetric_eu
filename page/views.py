from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('<a href="racuni/login">projektna naloga</a>')
