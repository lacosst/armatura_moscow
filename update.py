import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "armatura_moscow.settings")
django.setup()

from shop.models import Product, Category

# Вес метра
ves_metra = 0
vm = {
    '5.5': '0.19',
    '6': '0.22',
    '6.5': '0.26',
    '8': '0.40',
    '10': '0.62',
    '12': '0.89',
    '14': '1.21',
    '16': '1.58',
    '18': '2.00',
    '20': '2.47',
    '22': '2.98',
    '25': '3.85',
    '28': '4.83',
    '32': '6.31',
    '36': '7.99',
    '40': '9.87',
}


with open('Price.csv') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:

        if 'мотки' in row[1]:
            row[1] = row[1].replace('мотки', 'бухта')
        if ',' in row[2]:
            row[2] = row[2].replace(',', '.')

        # задаем категорию
        if row[0] == 'Арматура рифленая А3':
            cat_id = 5
        elif row[0] == 'Арматура гладкая А1':
            cat_id = 3
        elif row[0] == 'Катанка':
            cat_id = 4
        elif row[0] == 'Арматура Ат800':
            cat_id = 6

        if cat_id == 4 and 'мотки' in row[4]:
            row[1] = row[1] + ' бухта'

        if row[2] in vm.keys():
            ves_metra = vm.get(row[2])
            print(row[1], ves_metra,)

        Product.objects.update_or_create(
            category_id=cat_id,
            name=row[1],
            diametr=row[2],
            mark_steel=row[3],
            dlina=row[4],
            defaults={
                'price_toon': int(row[5]),
                'meter_weight': ves_metra,
            }
        )






