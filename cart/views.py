from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


# Create your views here.

@require_POST
def cart_add(request, product_id):
    """Обработчик для добавление товара в корзину"""
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd["quantity"], update_quantity=cd["update"])
    return redirect("cart:cart_detail")


def cart_remove(request, product_id):
    """Обработчик для удаление продукта из корзины"""
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product)
    return redirect("cart:cart_detail")


def cart_detail(request):
    """Обработчик для списка товаров добавленных в корзину"""
    cart = Cart(request)
    return render(request, "cart/detail.html", {"cart": cart})
