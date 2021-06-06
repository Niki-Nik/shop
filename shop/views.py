from django.shortcuts import render
from .models import Category, Product
from cart.forms import CartAddProductForm


# Create your views here.


def product_list(request, category_slug=None):
    """Обработчик страницы для товаров"""
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = Category.objects.get(slug=category_slug)
        products = products.filter(category=category)
    return render(request, "shop/product/list.html", {"category": category,
                                                      "categories": categories, "products": products})


def product_detail(request, product_id, slug):
    """Обработчик страницы для товара"""
    product = Product.objects.get(id=product_id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, "shop/product/detail.html", {"product": product, "cart_product_form": cart_product_form})
