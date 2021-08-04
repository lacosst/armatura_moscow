import csv
import decimal
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "armatura_moscow.settings")
django.setup()


from shop.models import Product, Category

with open('Price.csv') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        print(row[1])

        if 'мотки' in row[1]:
            row[1] = row[1].replace('мотки', 'бухта')

        if ',' in row[2]:
            row[2] = row[2].replace(',', '.')

        if row[0] == 'Арматура рифленая А3':
            cat_id = 5
        elif row[0] == 'Арматура гладкая А1':
            cat_id = 3
        elif row[0] == 'Катанка':
            cat_id = 4
        elif row[0] == 'Арматура Ат800':
            cat_id = 6

        Product.objects.update_or_create(
            category_id=cat_id,

            # name=row[1],

            diametr=row[2],
            mark_steel=row[3],
            dlina=row[4],

            # meter_weight=0.0,
            # price_toon=int(row[5]),

            defaults={
                'price_toon': int(row[5]),
                # 'name': row[1],
                # 'meter_weight': meter_weight
            }
        )






