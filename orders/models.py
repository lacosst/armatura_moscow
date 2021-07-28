from django.db import models
from shop.models import Product


class Order(models.Model):
    fio = models.CharField(max_length=150, verbose_name='ФИО')
    phone_number = models.CharField(max_length=18, verbose_name='Номер телефона')
    email = models.EmailField()
    choices = (('new', 'Новый заказ'),
               ('confirmed', 'Подтвержден'),
               ('completed', 'Выполнен'),
               ('canceled', 'Отменен'))
    status = models.CharField(max_length=100, choices=choices, default="new", verbose_name='Статус заказ')
    comment = models.TextField(max_length=1000, blank=True, verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обнавлен')
    paid = models.BooleanField(default=False, verbose_name='Оплачен')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.DO_NOTHING, verbose_name='Позиция')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Кол-во')

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
