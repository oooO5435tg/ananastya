from .models import Product
from .forms import ProductCreate
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class Login(LoginView):
    template_name = 'login.html'

class ProductList(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products_list'

class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    template_name = 'add_product.html'
    form_class = ProductCreate
    success_url = reverse_lazy('products')


