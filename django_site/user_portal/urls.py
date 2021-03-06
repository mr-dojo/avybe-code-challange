# User Portal urls

from django.urls import path
from django.conf import settings
from . import views

app_name = 'user_portal'
urlpatterns = [
    path('', views.home, name='home'),
    path('new-account', views.create_account, name='create account'),
    path('edit-account', views.edit_account, name='edit account'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
