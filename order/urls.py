from django.urls import path, include
from .views import CheckoutView


urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    
]