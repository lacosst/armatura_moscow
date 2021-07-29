import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "armatura_moscow.settings")
django.setup()

from shop.models import Product, Category


a = []
with open('Price.csv') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        row[0] = row[0].replace('мотки', 'бухта')
        print(row)
        Product.objects.update_or_create(
            category=Category.objects.get(id=5),
            name=row[0],
            diametr=row[1],
            mark_steel=row[2],
            price_toon=int(row[4]),
            meter_weight=float(0),

        )






