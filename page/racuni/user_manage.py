from django.contrib.auth.models import User


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
