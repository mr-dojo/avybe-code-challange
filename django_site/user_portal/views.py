from django.shortcuts import render
from django.http import HttpResponse


def landing(request):
    return HttpResponse('<h1>This is the landing page</h1><p>You can either log in or create account</p>')


def home(request):
    output = '<h1>Hello %s</h1>'
    return HttpResponse(output)


def create_account(request):
    return HttpResponse('<h1>Enter nickname and image</h1>')


def edit_account(request):
    return HttpResponse('<h1>Edit your account</h1>')


def login(request):
    return HttpResponse('<h1>Login</h1>')
