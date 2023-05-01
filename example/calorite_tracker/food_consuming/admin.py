from django.contrib import admin

# Register your models here.
from food_consuming.models import Food, Consume

admin.site.register(Food) 
admin.site.register(Consume) 
