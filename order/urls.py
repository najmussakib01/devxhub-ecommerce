from django.urls import path, include
from .views import CheckoutView, SaveOrderData


urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('save-order/', SaveOrderData.as_view(), name='save_order'),
    
]