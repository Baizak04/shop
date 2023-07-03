from django.shortcuts import render
from django.http import HttpResponse


def salam(request):
    return HttpResponse("<u>Salam Python off 7</u><b>salam</b>")
