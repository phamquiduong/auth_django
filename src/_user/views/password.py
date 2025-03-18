from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from _user.forms import PasswordForm
from db.models import User


def change_password_view(request: HttpRequest) -> HttpResponse:
    user = User.objects.get(id=request.user.id)  # type:ignore
    form = PasswordForm(request.POST or None, user=user)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form.login(request=request)
            messages.success(request, 'Password updated successfully. You have been logged out from all sessions.')
            return render(request, 'redirect.html', {'url': reverse('user-change_password')})
        else:
            messages.error(request, 'Update password failed')

    context = {
        'form': form,
    }
    return render(request, 'user/pages/password.html', context)
