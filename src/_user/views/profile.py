from django.http import HttpRequest
from django.shortcuts import render


def profile_view(request: HttpRequest):
    return render(request, 'user/pages/profile.html')
