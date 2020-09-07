# User Portal urls

from django.urls import path
from . import views

app_name = 'user_portal'
urlpatterns = [
    path('', views.landing, name='landing'),
    path('home', views.home, name='home'),
    path('new-account', views.create_account, name='create account'),
    path('edit-account', views.edit_account, name='edit account'),
    path('save-account', views.save_account, name='save account'),
    path('login', views.login, name='login'),
]
