from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def input_validate(inputs):
    try:
        if len(inputs['username']) == 0:
            return False
        if len(inputs['password']) == 0:
            return False
    except KeyError:
        return False
    return True


def create_user(inputs):
    user = User.objects.create_user(
        username=inputs['username'],
        password=inputs['password'],
        )
    user.save()


def register(inputs):
    if User.objects.filter(username=inputs['username']).exists():
        return False
    if not input_validate(inputs):
        return False
    create_user(inputs)
    return True


def login_ses(request):
    uname = request.POST.get('username')
    pword = request.POST.get('password')
    print(uname, pword)
    user = authenticate(request, username=uname, password=pword)
    if user is not None:
        login(request, user)
        return True
    else:
        return False
