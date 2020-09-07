from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Person
from .models import UserState

# _________PAGES_______________


def home(request):
    try:
        current_user = UserState.objects.get().current_user
    except UserState.DoesNotExist:
        current_user = {}
    return render(request, 'user_portal/home.html', {'current_user': current_user})


def create_account(request):
    return render(request, 'user_portal/new-account.html')


def edit_account(request):
    try:
        current_user = UserState.objects.get().current_user
    except UserState.DoesNotExist:
        return render(request, 'user_portal/home.html')

    else:
        return render(request, 'user_portal/edit-account.html', {'current_user': current_user})


def login(request):
    return render(request, 'user_portal/login.html')


# ________ACTIONS_________


def save_account(request):
    new_user_nickname = request.POST['nickname']
    # Add validation of nickname (is the nickname taken?)
    # Create Person
    new_person = Person(nickname=new_user_nickname)
    new_person.save()
    # Update UserState
    login_as = UserState(current_user=new_user_nickname)
    login_as.save()
    return HttpResponseRedirect('/')


def update_account(request):
    new_user_nickname = request.POST['nickname']
    # Add validation of new nickname (is the new nickname taken?)
    # Update UserState
    current_user_nickname = UserState.objects.get().current_user
    current_logged_in_user = UserState.objects.get()
    current_logged_in_user.current_user = new_user_nickname
    current_logged_in_user.save()

    # Update Person
    person = Person.objects.get(nickname=current_user_nickname)
    person.nickname = new_user_nickname
    person.save()
    return HttpResponseRedirect('/')


def validate_login(request):
    # Add validation (what happens if nickname is incorrect?)
    login_nickname = request.POST['users-nickname']
    valid_nickname = Person.objects.get(nickname=login_nickname) or 0

    current_user = UserState.objects.all()
    current_user.delete()

    login_as = UserState(current_user=valid_nickname)
    login_as.save()
    return HttpResponseRedirect('/')


def logout(request):
    current_user = UserState.objects.all()
    current_user.delete()

    return HttpResponseRedirect('/')
