from http import HTTPMethod

from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import render

from _auth.forms import LoginForm


def login_view(request: HttpRequest):
    form = LoginForm(request.POST or None)

    if request.method == HTTPMethod.POST:
        if form.is_valid():
            form.login(request=request)
            messages.success(request, 'Login successful')
            return render(request, 'redirect.html')
        else:
            messages.error(request, 'Login failed')

    context = {
        'form': form,
    }
    return render(request, 'auth/pages/login.html', context)
