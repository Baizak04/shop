from django.urls import path
from food_consuming import views

urlpatterns = [
    path('hello', views.IndexView.as_view(), name="hello")
]
