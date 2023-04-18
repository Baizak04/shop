from django.http import HttpRequest
import pdb
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from myshop.models import Product, Order
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def test(request): 
    return render(request, "cart/signup.html")

def order (request):
    order_obj = Order()
    if request.POST:
        order_obj.email = request.POST['email']
        order_obj.address = request.POST['address']
        order_obj.phone = request.POST['phone']
        order_obj.mbank_number = request.POST['mbank']
        order_obj.product = request.POST['product']
        order_obj.total_price = request.POST['total_price']
    order_obj.save()
    del request.session['cart']

    return render(request, "cart/socsses.html")
    

def cart_detail(request):
    cart = Cart(request)
    print(cart)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})