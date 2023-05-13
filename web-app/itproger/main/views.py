from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h3>Проверка работы<h/3>")


def about(request):
    return render(request, 'main/about.html')

def index_two(request):
    data = {
        'title': 'Главная страница',
        'values': ['']
    }
    return render(request, 'main/index_two.html', data)

