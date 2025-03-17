from typing import Any

from django import forms

from db.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class AvatarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar']
