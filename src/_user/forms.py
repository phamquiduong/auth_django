from typing import Any

from django import forms

from _auth.constants import UserModel


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['email', 'first_name', 'last_name']
