from django.db import models

# Create your models here.

class Food(models.Model):
    
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()

class Consume(models.Model):
    user = models.ForeignKey(User)
    food = models.ForeignKey(Food)
    
    