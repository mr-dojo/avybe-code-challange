from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import UserState


def landing(request):
    return HttpResponse('<h1>This is the landing page</h1><p>You can either log in or create account</p>')


def home(request):
    try:
        current_user = UserState.objects.get().current_user
    except UserState.DoesNotExist:
        raise Http404('User is not logged in, re-route to login page')
    return render(request, 'user_portal/home.html', {'current_user': current_user})


def create_account(request):
    return HttpResponse('<h1>Enter nickname and image</h1>')


def edit_account(request):
    return HttpResponse('<h1>Edit your account</h1>')


def login(request):
    return HttpResponse('<h1>Login</h1>')
