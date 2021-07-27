from django.shortcuts import render
from django.template.loader import get_template, render_to_string

from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from shop.models import Category
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from armatura_moscow.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL


def sendmail_for_user(um, context):
    html = get_template("orders/email/order_created.html")
    subject, from_email, to = f'Armatura.moscow | Ваш заказ № {context["order"].id} получен', DEFAULT_FROM_EMAIL, um
    text_content = 'This is an important message.'
    html_content = html.render(context)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def order_create(request):
    categories = Category.objects.all()
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            if cart.cart:
                order = form.save()
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
                context = {'order': order, 'cart': cart}
                cart.clear()  # очистка корзины
                um = form.cleaned_data["email"]

                sendmail_for_user(um, context)  # отправка письма пользователю

                return render(request, 'orders/created.html',
                              {'order': order, 'categories': categories})
            else:
                order = Order.objects.first()
                return render(request, 'orders/created.html',
                              {'order': order, 'categories': categories})
    else:
        form = OrderCreateForm
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form, 'categories': categories})
