from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Product
from shopping_cart.models import Order
<<<<<<< HEAD
from django.db.models import Q
=======
>>>>>>> dcde77094d473db2565842e8bbaa97853d3d0423
# Create your views here.


def category(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    products = Product.objects.filter(
        Q(category__icontains=q) |
        Q(prod_name__icontains=q) |
        Q(prod_description__icontains=q)
    )

    categories = Product.Category.choices

    prod_count = products.count()
    # room_messages = Message.objects.filter(
    #     Q(room__topic__name__icontains=q))[0:3]

    context = {
        'products': products, 'prod_count': prod_count, 'categories': categories
    }
    return render(request, 'aroma/category.html', context)


def cart(request):
    return render(request, 'aroma/cart.html')


def confirmation(request):
    return render(request, 'aroma/confirmation.html')


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
    fields = ['prod_name', 'prod_description', 'prod_price', 'category', 'prod_image']

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

@login_required
def product_list(request):
    object_list = Product.objects.all()
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [product.product for product in user_order_items]

    context = {
        'object_list': object_list,
        'current_order_products': current_order_products
    }

    return render(request, "product_list.html", context)