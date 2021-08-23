from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from armatura_moscow import settings
from shop.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('', include('shop.urls')),
    path('orders/', include('orders.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)