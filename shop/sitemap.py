from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product


class ProductSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Product.objects.filter(available=True)

    def lastmod(self, obj):
        return obj.updated


class StaticViewsSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return ['shop:home', 'shop:contact', 'shop:pickup', 'shop:pay', 'shop:cutting']

    def location(self, item):
        return reverse(item)
