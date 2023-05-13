from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h3>Проверка работы<h/3>")


def about(request):
    return render(request, 'main/about.html')

def index_two(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': '18',
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index_two.html', data)

