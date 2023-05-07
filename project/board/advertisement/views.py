from django.shortcuts import render
from django.http import HttpResponse


def advertisement_list(request, *args, **kwargs):
    return HttpResponse(
        '<ul>'
        '<li>Что-то</li>'
        '<li>Выведение из запроса</li>'
        '<li>Услуги экскаватора</li>'
        '</ul>'
    )
