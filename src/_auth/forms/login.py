from django import forms
from django.contrib.auth import login
from django.contrib.auth.password_validation import validate_password
from django.http import HttpRequest
from django.utils import timezone

from _auth.constants.user_locked import LOCKED_ACCOUNT_DURATION, MAX_FAILED_LOGIN_ATTEMPTS
from db.models import User


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(validators=[validate_password])
    user: User | None

    def clean_email(self) -> str:
        email = self.cleaned_data.get('email', '')

        self.user = User.objects.filter(email=email).first()

        if not self.user:
            raise forms.ValidationError('The email is not registed.', code='invalid')

        if not self.user.is_active:
            raise forms.ValidationError('The account is not active.', code='invalid')

        if self.user.locked_to and self.user.locked_to > timezone.now():
            locked_to = timezone.localtime(self.user.locked_to).strftime('%Y-%m-%d %H:%M:%S')
            raise forms.ValidationError(f'The account is locked. (Will unlock at {locked_to})', code='invalid')

        return email

    def clean_password(self) -> str:
        password: str = self.cleaned_data.get('password', '')

        if self.user and not self.user.check_password(raw_password=password):
            self.user.incorrect_password_count += 1
            if self.user.incorrect_password_count >= MAX_FAILED_LOGIN_ATTEMPTS:
                self.user.locked_to = timezone.now() + LOCKED_ACCOUNT_DURATION
            self.user.save()

            raise forms.ValidationError('The password is incorrect', code='invalid')

        return password

    def login(self, request: HttpRequest) -> None:
        if not self.user:
            return

        self.user.incorrect_password_count = 0
        self.user.locked_to = None
        self.user.save()

        login(request=request, user=self.user)
