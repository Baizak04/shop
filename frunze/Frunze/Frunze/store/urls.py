from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('Category/', views.CategoryListView. as_view(), name='Category_list'),
    path('Category/<pk>/', views.CategoryDetailView.as_view(), name='Category_detail'),
    path('Product/', views.ProductListView. as_view(), name='Product_list'),
    path('Product/<pk>/', views.ProductDetailView.as_view(), name='Product_detail'),
    path('Order/', views.OrderListView. as_view(), name='Order_list'),
    path('Order/<pk>/', views.OrderDetailView.as_view(), name='Order_detail'),
]