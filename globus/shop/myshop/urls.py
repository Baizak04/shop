from django.urls import path
from . import views 
from rest_framework import routers
from .views import product_list ,ProductViewSet , CategorySerializer



router = routers.DefaultRouter()
router.register(r'',ProductViewSet,CategorySerializer)

app_name = 'myshop'

urlpatterns = [
    path('',product_list, name='product_list'),
    path('product/',ProductViewSet.as_view({'get':'list'}),name='products'),
    path('order/',CategorySerializer.as_view({'get':'list'}),name='orders'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'
         ),
    path('<int:id>/<slug:slug>', views.product_detail,
         name='product_detail')
]