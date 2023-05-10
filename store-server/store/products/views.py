from django.shortcuts import render, HttpResponse

# Create your views here.

def index_one(request):
    return HttpResponse("hello there")

def index(request):
    return render(request, 'products/index.html')