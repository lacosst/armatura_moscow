import decimal

from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        # ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category', kwargs={'cat_slug': self.slug})


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='URL')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение')
    diametr = models.PositiveIntegerField(verbose_name='Диаметр')
    mark_steel = models.CharField(max_length=10, verbose_name='Марка стали')
    description = models.TextField(blank=True, verbose_name='Описание')
    meter_weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вес метра, кг.')
    price_toon = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за тонну')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, verbose_name='Цена')
    stock = models.IntegerField(verbose_name='Запасы', default=0)
    available = models.BooleanField(default=True, verbose_name='Опубликован')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['category', 'name']
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    @property
    def get_price(self):
        a = self.price_toon / 1000  # получаем цену за 1 кг
        b = self.meter_weight * a  # получаемм ценну зrа 1 м
        c = int(b) + (int(b) * 0.1)  # делаем наценку
        return decimal.Decimal(c)

    def save(self, *args, **kwargs):
        self.price = self.get_price
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse('shop:product_detail', args=[self.id, self.slug])
        return reverse('shop:product', kwargs={'product_slug': self.slug})

