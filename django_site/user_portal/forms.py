from django import forms

from .models import Person, UserState


class PersonForm(forms.ModelForm):
    nickname = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'What do they call you?'}))

    class Meta:
        model = Person
        fields = [
            'nickname',
            'profile_image',
        ]


class UserStateForm(forms.ModelForm):
    current_user = forms.CharField(
        label="Nickname",
        widget=forms.TextInput(
            attrs={'placeholder': 'Whats your new nickname?'}))

    class Meta:
        model = UserState
        fields = [
            'current_user',
            'profile_image',
        ]


class LoginForm(forms.Form):
    current_user = forms.CharField()
