from http import HTTPMethod

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from _auth.forms import LoginForm


def login_view(request: HttpRequest) -> HttpResponse:
    form = LoginForm(request.POST or None)

    if request.method == HTTPMethod.POST:
        if form.is_valid():
            form.login(request=request)
            messages.success(
                request, f'Welcome back <span class="fw-semibold">{form.user.email}</span>'   # type:ignore
            )
            return render(request, 'redirect.html')
        else:
            messages.error(request, 'Login failed! Please try again')

    context = {
        'form': form,
    }
    return render(request, 'auth/pages/login.html', context)
