from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('salam_python', views.salam_python, name='salam_python'),
    path('erjan', views.erjan, name='erjan')
]