from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField( max_length=254,unique=True, null=True, blank=True)
    
    
    class Meta(AbstractUser.Meta):
       swappable = 'AUTH_USER_MODEL'


# Create your models here.

class Food(models.Model):
    
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()
# # 
class Consume(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='userss')
    # food = models.ForeignKey('Food', on_delete=models.CASCADE, related_name='foods')
    
    