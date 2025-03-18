from django import forms

from db.models import User


class AvatarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar']
