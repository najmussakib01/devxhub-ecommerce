import uuid
import json
from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from django.contrib import messages
from django.views.generic.edit import FormMixin
from django.views.generic import FormView
from .forms import CheckoutForm
from cart.carts import Cart
from cart.models import Coupon
from .models import OrderItem, Order, StatusOptions
from product.models import Product

# Create your views here.
class CheckoutView(generic.View):
    title = "Checkout Form"
    form_class = CheckoutForm
    template_name = 'eshop/checkout/checkout.html'

    def get(self, request, *args, **kwargs):
        first_name = self.request.user.first_name
        last_name = self.request.user.last_name
        email = self.request.user.email
        street = self.request.user.userprofile.street
        city = self.request.user.userprofile.city
        address = self.request.user.userprofile.billing_address
        phone_no = self.request.user.userprofile.phone_number
        form = self.form_class(initial={
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'street': street,
                    'city': city,
                    'address': address,
                    'phone_no': phone_no,
                })
        context = {
            'form': form,
            'title': self.title,
        }
        return render(request, self.template_name, context)
    

    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            return JsonResponse({
                'success': True,
                'errors': None
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': dict(form.errors)
            })


class SaveOrderData(generic.View):
    def post(self, *args, **kwargs):
        data = json.loads(self.request.body)
        cart = Cart(self.request)
        coupon_id = cart.coupon
        user_cart = Cart(self.request).cart
        products = Product.objects.filter(id__in=list(user_cart))
        ordered_products = []

        for product in products:
            order_item = OrderItem.objects.create(
                product = product,
                price = product.price,
                quantity = user_cart[str(product.id)]['quantity'],
            )
            ordered_products.append(order_item)
            # update product stock.
            product.stock -= user_cart[str(product.id)]['quantity']
            product.save()

        order = Order.objects.create(
            user = self.request.user,
            transaction_id = uuid.uuid4().hex,
            status = StatusOptions.RECEIVED,
            paypal_transaction_id = data['paypal_transaction_id'],
            total_amount = cart.grand_total(),
            paid_amount = data['amount'],
        )
        if coupon_id:
            order.coupon = Coupon.objects.get(id=coupon_id)

        order.order_items.add(*ordered_products)
        print(cart.grand_total(), float(data['amount']))
        if float('%.2f' % cart.grand_total()) != float(data['amount']):
            order.paid= False
            order.save()
        order.save()
        cart.clear()
        return JsonResponse({
            'success': True,
            'errors': None
        })