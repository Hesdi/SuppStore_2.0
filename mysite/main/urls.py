from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    UserProductListView
)
from . import views

urlpatterns = [
    path('product-list/', views.product_list, name='product-list'),
    path('category/', views.category, name='category'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('blog/', views.blog, name='blog'),
    path('single-blog/', views.single_blog, name='single-blog'),
    path('tracking-order/', views.tracking_order, name='tracking-order'),
    path('contact/', views.contact, name='contact'),
    path('', ProductListView.as_view(), name='main-index'),
    path('user/<str:username>', UserProductListView.as_view(), name='user-products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]