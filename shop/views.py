from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.views.generic.base import TemplateView
from .mixin import DataMixin


def shop(request, cat_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('category__order', 'order')
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
    categories = Category.objects.all()
    context = {
        'product': product,
        'categories': categories,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/detail.html', context=context)


def contact(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'shop/contact.html', context=context)


class PickupView(DataMixin, TemplateView):
    template_name = 'shop/pickup.html'

    def get_context_data(self, **kwargs):
        data = self.get_user_context()
        context = dict(list(data.items()))
        return context


class PayView(DataMixin, TemplateView):
    template_name = 'shop/pay.html'

    def get_context_data(self, **kwargs):
        data = self.get_user_context()
        context = dict(list(data.items()))
        return context


class CuttingView(DataMixin, TemplateView):
    template_name = 'shop/cutting.html'

    def get_context_data(self, **kwargs):
        data = self.get_user_context()
        context = dict(list(data.items()))
        return context
