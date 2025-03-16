from django import forms
from django.contrib.auth import login
from django.contrib.auth.password_validation import validate_password
from django.http import HttpRequest

from _auth.constants import UserModel


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(validators=[validate_password])
    user: UserModel | None = None

    def clean_email(self):
        email = self.cleaned_data.get("email")

        self.user = UserModel.objects.filter(email=email).first()

        if not self.user:
            raise forms.ValidationError("The email is not registed.", code="invalid")

        if not self.user.is_active:
            raise forms.ValidationError("The account is not active.", code="invalid")

        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")

        if not password or (self.user and not self.user.check_password(raw_password=password)):
            raise forms.ValidationError("The password is incorrect", code="invalid")

        return password

    def login(self, request: HttpRequest):
        login(request=request, user=self.user)
