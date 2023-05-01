from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from food_consuming.api.serializers import UserSerialiser, FoodSerializer, ConsumeSerializer
from food_consuming.models import Food, Consume

class UserViewSet(viewsets. ModelViewSet):
    gueryset = User.objects.all().order_by('data_joined emes')
    serializer_class = UserSerialiser
    permission_classes = [permissions.IsAuthenticated]
    

class FoodViewSet(viewsets. ModelViewSet):
    gueryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticated]
    


class ConsumeViewSet(viewsets. ModelViewSet):
    gueryset = Consume.objects.all()
    serializer_class = ConsumeSerializer
    permission_classes = [permissions.IsAuthenticated]
