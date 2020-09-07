from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Person
from .models import UserState


def landing(request):
    return HttpResponse('<h1>This is the landing page</h1><p>You can either log in or create account</p>')


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
        return HttpResponseRedirect('home')


def edit_account(request):
    return HttpResponse('<h1>Edit your account</h1>')


def login(request):
    return HttpResponse('<h1>Login</h1>')
