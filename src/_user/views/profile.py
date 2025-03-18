from http import HTTPMethod

from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect, render

from _user.forms import ProfileForm
from db.models.user import User


def profile_view(request: HttpRequest):
    user = User.objects.get(id=request.user.id)  # type:ignore
    form = ProfileForm(request.POST or None, instance=user)

    if request.method == HTTPMethod.POST:
        if form.is_valid():
            form.save()
            messages.success(request, 'Update user information successfully')
            return redirect('user-profile')
        else:
            messages.error(request, 'Update user information failed')

    context = {
        'form': form,
    }
    return render(request, 'user/pages/profile.html', context)
