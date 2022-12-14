from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Product
# Create your views here.


def category(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'aroma/category.html', context)


def cart(request):
    return render(request, 'aroma/cart.html')


def confirmation(request):
    return render(request, 'aroma/confirmation.html')


def checkout(request):
    return render(request, 'aroma/checkout.html')


def contact(request):
    return render(request, 'aroma/contact.html')


def blog(request):
    return render(request, 'aroma/blog.html')


def single_blog(request):
    return render(request, 'aroma/single-blog.html')


def login(request):
    return render(request, 'users/login.html')


def register(request):
    return render(request, 'users/register.html')
    

def tracking_order(request):
    return render(request, 'aroma/tracking-order.html')



def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'aroma/index.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'aroma/index.html'  
    context_object_name = 'products'
    ordering = ['-prod_date']
    paginate_by = 5

class UserProductListView(ListView):
    model = Product
    template_name = 'aroma/user_products.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Product.objects.filter(author=user).order_by('-prod_date')    


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['prod_name', 'prod_description', 'prod_price', 'category', 'prod_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['prod_name', 'prod_description', 'prod_price', 'category', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.author:
            return True
        return False


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.author:
            return True
        return False
