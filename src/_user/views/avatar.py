from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from _auth.constants import UserModel
from _user.forms import AvatarForm


@require_POST
def avatar_view(request: HttpRequest):
    user = UserModel.objects.get(id=request.user.id)
    form = AvatarForm(request.POST, files=request.FILES, instance=user)

    form.save()

    messages.success(request, 'Avatar updated successfully')
    return redirect('user-profile')
