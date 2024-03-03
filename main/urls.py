from django.urls import path
from django.views.generic import RedirectView
from .views import Login
from .views import ProductList
from .views import ProductCreateView

urlpatterns = [
    path('', RedirectView.as_view(url='service')),
    path('login/', Login.as_view(), name='login'),
    path('service/', ProductList.as_view(), name='products'),
    path('add_service/', ProductCreateView.as_view(), name='add_service'),
]
