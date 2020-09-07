from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Person
from .models import UserState


def home(request):
    try:
        current_user = UserState.objects.get().current_user
    except UserState.DoesNotExist:
        current_user = {}
    return render(request, 'user_portal/home.html', {'current_user': current_user})


def create_account(request):
    return render(request, 'user_portal/new-account.html')


def save_account(request):
    try:
        user_nickname = request.POST['nickname']
    except (KeyError, user_nickname.DoesNotExist):
        return render(request, 'user_portal:create account.html', {'error_message': "You didn't tell me your nickname, don't be shy"})
    else:
        new_person = Person(nickname=user_nickname)
        new_person.save()
        login_as = UserState(current_user=user_nickname)
        login_as.save()
        return HttpResponseRedirect('/')


def edit_account(request):
    return HttpResponse('<h1>Edit your account</h1>')


def login(request):
    return render(request, 'user_portal/login.html')


def validate_login(request):
    try:
        # Remove currently logged in user and check that login nickname exists
        login_nickname = request.POST['users-nickname']
        valid_nickname = Person.objects.get(nickname=login_nickname) or 0

        current_user = UserState.objects.all()
        current_user.delete()

    except (KeyError, bool(valid_nickname)):
        return render(request, 'user_portal:login.html', {'error_message': "Your nickname is incorrect"})
    except (KeyError, login_nickname.DoesNotExist):
        return render(request, 'user_portal:login.html', {'error_message': "Please enter your nickname"})

    else:
        login_as = UserState(current_user=valid_nickname)
        login_as.save()
        return HttpResponseRedirect('/')
