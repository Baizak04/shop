from django.shortcuts import render, redirect
from food_consuming.models import Food, Consume
from django.http import HttpResponse
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
