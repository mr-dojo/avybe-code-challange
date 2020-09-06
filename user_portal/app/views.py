from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing(request):
  return HttpResponse('This is the landing page')

def new_account(request):
  return HttpResponse('Create a new account')
  
def login(request):
  return HttpResponse('login to existing account')
