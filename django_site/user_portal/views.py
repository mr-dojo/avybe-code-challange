from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import ValidationError

from .forms import PersonForm, UserStateForm, LoginForm

from .models import Person, UserState

# _________PAGES_______________


def home(request):
    try:
        current_user = UserState.objects.get().current_user
        profile_image = UserState.objects.get().profile_image
        context = {
            'current_user': current_user,
            'profile_image': profile_image,
        }
    except UserState.DoesNotExist:
        context = {}

    return render(request, 'user_portal/home.html', context)


def create_account(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            nickname = form.cleaned_data.get('nickname')
            image = form.cleaned_data.get('profile_image')
            login_as = UserState(current_user=nickname, profile_image=image)
            login_as.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = PersonForm()

    context = {
        'form': form
    }

    return render(request, 'user_portal/new-account.html', context)


def edit_account(request):
    if request.method == 'POST':
        form = UserStateForm(request.POST, request.FILES)
        current_user_nickname = UserState.objects.get().current_user
        if form.is_valid():
            # Update current logged in user
            current_user = UserState.objects.get()
            current_user.delete()
            form.save()
            # Update person
            new_nickname = form.cleaned_data.get('current_user')
            new_image = form.cleaned_data.get('profile_image')
            person = Person.objects.get(nickname=current_user_nickname)
            person.nickname = new_nickname
            person.profile_image = new_image
            person.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = UserStateForm()

    context = {
        'form': form
    }

    return render(request, 'user_portal/edit-account.html', context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('current_user')
            users_image = Person.objects.get(nickname=user).profile_image
            login_as = UserState(current_user=user, profile_image=users_image)
            login_as.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'user_portal/login.html', context)


def media(request):
    return render(request, 'media.html')


# ________ACTIONS_________


def logout(request):
    current_user = UserState.objects.all()
    current_user.delete()

    return HttpResponseRedirect('/')
