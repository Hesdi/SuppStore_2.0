from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.category, name='category'),
    path('cart/', views.cart, name='cart'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('checkout/', views.checkout, name='checkout'),
    path('single-product/', views.single_product, name='single-product'),
]