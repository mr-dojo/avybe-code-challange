from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import ValidationError

from .forms import PersonForm, UserStateForm

from .models import Person, UserState

# _________PAGES_______________


def home(request):
    try:
        current_user = UserState.objects.get().current_user
    except UserState.DoesNotExist:
        current_user = {}
    return render(request, 'user_portal/home.html', {'current_user': current_user})


def create_account(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        new_nickname = form.cleaned_data.get('nickname')
        login_as = UserState(current_user=new_nickname)
        login_as.save()
        return HttpResponseRedirect('/')
    else:
        print(form.errors)

    context = {
        'form': form
    }

    return render(request, 'user_portal/new-account.html', context)


def edit_account(request):
    form = UserStateForm(request.POST or None)
    current_user_nickname = UserState.objects.get().current_user
    if form.is_valid():
        # Update current logged in user
        current_user = UserState.objects.get()
        current_user.delete()
        form.save()
        # Update person
        new_nickname = form.cleaned_data.get('current_user')
        person = Person.objects.get(nickname=current_user_nickname)
        person.nickname = new_nickname
        person.save()
        return HttpResponseRedirect('/')
    else:
        print(form.errors)

    context = {
        'form': form
    }

    return render(request, 'user_portal/edit-account.html', context)


def login(request):
    form = PersonForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_nickname = form.cleaned_data.get('nickname')
            valid_nickname = Person.objects.get(nickname=new_nickname)
            login_as = UserState(current_user=new_nickname)
            login_as.save()
            return HttpResponseRedirect('/')

    context = {
        'form': form,
    }
    return render(request, 'user_portal/login.html', context)


# ________ACTIONS_________


def logout(request):
    current_user = UserState.objects.all()
    current_user.delete()

    return HttpResponseRedirect('/')
