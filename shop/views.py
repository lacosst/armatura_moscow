from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def main(request, cat_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart_product_form = CartAddProductForm()
    if cat_slug:
        category = get_object_or_404(Category, slug=cat_slug)
        products = products.filter(category=category)
    context = {'category': category,
               'categories': categories,
               'products': products,
               'cart_product_form': cart_product_form}
    return render(request, 'shop/shop.html', context=context)


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug,  available=True)

    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


