from django.shortcuts import render
from django.http import HttpResponse


def advertisement_list(request, *args, **kwargs):
    advertisements = [
        'Master',
        'что-то'
    ]
    return render(request, 'advertisement/advertisement_list.html', {'adverisements':advertisements})