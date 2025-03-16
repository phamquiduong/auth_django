from django.http import HttpRequest
from django.shortcuts import render


def heath_check_view(request: HttpRequest):
    return render(request, 'pages/heath-check.html')
