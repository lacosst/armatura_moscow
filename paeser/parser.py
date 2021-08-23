import random
import csv
import json

import requests
from bs4 import BeautifulSoup
from time import sleep
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "armatura_moscow.settings")
django.setup()
from shop.models import Product


def get_data(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-encoding': 'gzip, deflate, br',
        'Accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cash-control': 'max-age=0',
        'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    }

    # делаем заппрос на сайте
    r = requests.get(url=url, headers=headers)
    src = r.text

    # print(os.getcwd())
    # сохраняем документ в файл
    with open('/var/www/u1042075/data/www/armatura.moscow/armatura_moscow/paeser/data/index.html', 'w', encoding='utf-8') as file:
        file.write(src)

    # Читаем документ
    with open('/var/www/u1042075/data/www/armatura.moscow/armatura_moscow/paeser/data/index.html', encoding='utf-8') as file:
        doc = file.read()

    soup = BeautifulSoup(doc, 'lxml')
    links = soup.find_all('ul', class_='inserted')

    with open('/var/www/u1042075/data/www/armatura.moscow/armatura_moscow/paeser/categories.json', encoding='utf-8') as file:
        all_categories = json.load(file)

    iteration_count = int(len(all_categories)) - 1
    count = 0
    print(f'всего итераций: {iteration_count}')

    # file_name = datetime.now().strftime("%d_%m_%Y_%H_%M")

    with open('/var/www/u1042075/data/www/armatura.moscow/armatura_moscow/paeser/Price.csv', 'w') as file:
        writer = csv.writer(file, delimiter=';', lineterminator='\n')

    for category_name, category_url in all_categories.items():

        if 'г/к' in category_name:
            category_name = category_name.replace('г/к', 'гк')
        if 'х/к' in category_name:
            category_name = category_name.replace('х/к', 'хк')

        req = requests.get(url=category_url, headers=headers)
        src = req.text

        with open(f'/var/www/u1042075/data/www/armatura.moscow/armatura_moscow/paeser/data/{count}_{category_name}.html', 'w', encoding='utf-8') as file:
            file.write(src)

        with open(f'/var/www/u1042075/data/www/armatura.moscow/armatura_moscow/paeser/data/{count}_{category_name}.html', encoding='utf-8') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')

        try:
            i = 0
            product_data = soup.find('tbody').find_all('tr')
            for item in product_data:
                product_td = item.find_all('td')
                title = product_td[0].text.replace('→', '').strip()
                diametr = product_td[1].text.strip()
                marka_stali = product_td[2].text.strip()
                dlina = product_td[3].text.strip()
                price = product_td[5].text.replace(' ', '').strip()

                with open(f'/var/www/u1042075/data/www/armatura.moscow/armatura_moscow/paeser/Price.csv', 'a') as file:
                    writer = csv.writer(file, delimiter=';', lineterminator='\n')
                    writer.writerow(
                        (
                            category_name,
                            title,
                            diametr,
                            marka_stali,
                            dlina,
                            price,
                            i
                        )
                    )
                    i += 1
            count += 1
        except AttributeError:
            continue

        print(f"Итерация {count}. {category_name} получено...")
        iteration_count -= 1
        if iteration_count == 0:
            print('Работа завершена')
            # input('Для выхода нажмите Enter')
            break

        print(f'Осталось итераций: {iteration_count}')
        sleep(random.randrange(0, 1))


def update_product():
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

    with open('/var/www/u1042075/data/www/armatura.moscow/armatura_moscow/paeser/Price.csv') as f:
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
                # print(row[1], ves_metra, ' # ', row[6])

            Product.objects.update_or_create(
                category_id=cat_id,
                name=row[1],
                diametr=row[2],
                mark_steel=row[3],
                dlina=row[4],
                defaults={
                    'price_toon': int(row[5]),
                    'meter_weight': ves_metra,
                    'order': row[6]
                }
            )


def main():
    get_data('https://mc.ru/products/msk')
    sleep(5)
    print('################')
    update_product()
    print('update complete')


if __name__ == '__main__':
    main()
