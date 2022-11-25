from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.category, name='category'),
    path('cart/', views.cart, name='cart'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('checkout/', views.checkout, name='checkout'),
    path('single-product/', views.single_product, name='single-product'),
    path('blog/', views.blog, name='blog'),
    path('single-blog/', views.single_blog, name='single-blog'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('tracking-order/', views.tracking_order, name='tracking-order'),
    path('contact/', views.contact, name='contact'),
]