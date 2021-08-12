from django.http import JsonResponse, response, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib import messages


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST" and request.is_ajax():
        form = CartAddProductForm(request.POST)
        print(1)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
            # msg = messages.add_message(request, messages.SUCCESS, f"{product} х {cd['quantity']} метров добавлено в корзину ↓")
            msg = f"{product} х {cd['quantity']} метров добавлено в корзину ↓"
            data = {'quantity': cd['quantity'],
                    'msg': msg,
                    'total_pice_cart': cart.get_total_price(),
                    'count_item_cart': cart.__len__()}
            return JsonResponse(data, status=200, safe=False)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return redirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


@require_POST
def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    print(request.POST.get('qwt'))
    if request.is_ajax():
        form = CartAddProductForm(request.POST)

        cart.add(product=product,
                 quantity=int(request.POST.get('qwt')),
                 update_quantity=form['update'])
        msg = f"{product} х {int(request.POST.get('qwt'))} метров добавлено в корзину ↓"
        data = {'quantity': int(request.POST.get('qwt')),
                'msg': msg,
                'total_pice_cart': cart.get_total_price(),
                'count_item_cart': cart.__len__()}
        # print(data)
        # cart.save()

        return JsonResponse(data, status=200, safe=False)
    else:
        # errors = form.errors.as_json()
        return JsonResponse(None, status=400, safe=False)

    return redirect(request.META.get('HTTP_REFERER'))

    # print('#####', request.POST.get('qwt'))
    # return redirect('cart:cart_detail')


def cart_detail(request):
    categories = Category.objects.all()
    cart = Cart(request)
    cart_product_form = CartAddProductForm()
    return render(request, 'cart/detail.html', {'cart': cart, 'categories': categories, 'cart_product_form': cart_product_form})
