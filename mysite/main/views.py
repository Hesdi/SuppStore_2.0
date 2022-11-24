from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'aroma/index.html')


def category(request):
    return render(request, 'aroma/category.html')


def cart(request):
    return render(request, 'aroma/cart.html')


def confirmation(request):
    return render(request, 'aroma/confirmation.html')


def checkout(request):
    return render(request, 'aroma/checkout.html')


def single_product(request):
    return render(request, 'aroma/single-product.html')