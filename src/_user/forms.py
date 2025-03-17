from typing import Any

from django import forms
from django.contrib.auth import login
from django.contrib.auth.password_validation import validate_password
from django.http import HttpRequest

from db.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class AvatarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar']


class PasswordForm(forms.Form):
    current_password = forms.CharField()
    new_password = forms.CharField(max_length=128, validators=[validate_password])
    confirm_new_password = forms.CharField(max_length=128, validators=[validate_password])

    user: User

    def __init__(self, *args, user: User, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_current_password(self):
        current_password: str = self.cleaned_data.get('current_password', '')

        if not self.user.check_password(current_password):
            raise forms.ValidationError('Current password is incorrect')

        return current_password

    def clean_new_password(self):
        current_password: str = self.cleaned_data.get('current_password', '')
        new_password: str = self.cleaned_data.get('new_password', '')

        if current_password == new_password:
            raise forms.ValidationError('The new password is the same as the current password')

        return new_password

    def clean_confirm_new_password(self):
        new_password: str = self.cleaned_data.get('new_password', '')
        confirm_new_password: str = self.cleaned_data.get('confirm_new_password', '')

        if new_password and confirm_new_password != new_password:
            raise forms.ValidationError('The confirm password does not match the new password')

        return confirm_new_password

    def save(self):
        new_password: str = self.cleaned_data.get('new_password', '')
        self.user.set_password(new_password)
        self.user.save()

    def login(self, request: HttpRequest):
        login(request=request, user=self.user)
