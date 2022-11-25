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


def contact(request):
    return render(request, 'aroma/contact.html')


def blog(request):
    return render(request, 'aroma/blog.html')


def single_blog(request):
    return render(request, 'aroma/single-blog.html')


def login(request):
    return render(request, 'aroma/login.html')


def register(request):
    return render(request, 'aroma/register.html')


def tracking_order(request):
    return render(request, 'aroma/tracking-order.html')