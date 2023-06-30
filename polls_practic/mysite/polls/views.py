from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Салам Эламан.")

def erjan(request):
    return HttpResponse("Салам Эржан.")