from typing import Any, Dict
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from advertisement .models import Advertisement

def advertisement_list(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    return render(request, 'advertisements/advertisements.html', {
        'advertisements': advertisements
    })

class About (TemplateView):
    template_name = 'advertisement/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Бесплатные объявление в вашем городе'
        context['title'] = 'Бесплатные объявление'
        context['description'] = """Вы хотите что-то"""
        return context