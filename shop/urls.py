from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', main, name='home'),
    path('<slug:cat_slug>', main, name='category'),
    path('product/<slug:product_slug>', product_detail, name='product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)