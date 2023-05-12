from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h3>Проверка работы<h/3>")


def about(request):
    return HttpResponse("<h3>Страница про нас<h/3>")

