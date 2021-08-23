from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from django.contrib.sitemaps.views import sitemap
from shop.sitemap import ProductSitemap, StaticViewsSitemap
app_name = 'shop'

sitemaps = {
    'static': StaticViewsSitemap,
    'dynamic': ProductSitemap,

}

urlpatterns = [
    path('', shop, name='home'),
    path('<slug:cat_slug>', shop, name='category'),
    path('product/<slug:product_slug>', product_detail, name='product'),
    path('contact/', contact, name='contact'),
    path('pickup/', PickupView.as_view(), name='pickup'),
    path('pay/', PayView.as_view(), name='pay'),
    path('cutting/', CuttingView.as_view(), name='cutting'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)