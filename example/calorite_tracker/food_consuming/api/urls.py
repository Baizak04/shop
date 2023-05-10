from django.urls import include, path
from rest_framework import routers
from food_consuming.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'foods', views.FoodViewSet, basename='user2')
router.register(r'consumes', views.ConsumeViewSet, basename='user4')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]