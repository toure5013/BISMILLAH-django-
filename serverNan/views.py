
from django.shortcuts import render


def index(request):
    return render(request, 'pari/index.html')


def basketball(request):
    return render(request, 'pari/basketball.html')


def handball(request):
    return render(request, 'pari/handball.html')


def football(request):
    return render(request, 'pari/football.html')