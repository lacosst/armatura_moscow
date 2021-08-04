import random
import csv
import json
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from time import sleep

# from past.builtins import raw_input


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

    # сохраняем документ в файл
    with open('data/index.html', 'w', encoding='utf-8') as file:
        file.write(src)

    # Читаем документ
    with open('data/index.html', encoding='utf-8') as file:
        doc = file.read()

    soup = BeautifulSoup(doc, 'lxml')
    links = soup.find_all('ul', class_='inserted')

    # получаем все категории
    # all_categories = {}
    # for i in links:
    #     li = i.find_all('a')
    #     for item in li:
    #         name = item.text
    #         url = 'https://mc.ru' + item.get('href')
    #         all_categories[name] = url
    #
    # with open('all_categories.json', 'w', encoding='utf-8') as file:
    #     json.dump(all_categories, file, indent=4, ensure_ascii=False)

    with open('categories.json', encoding='utf-8') as file:
        all_categories = json.load(file)

    iteration_count = int(len(all_categories)) - 1
    count = 0
    print(f'всего итераций: {iteration_count}')

    # file_name = datetime.now().strftime("%d_%m_%Y_%H_%M")

    with open('../Price.csv', 'w', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter=';', lineterminator='\n')
        # writer.writerow(
        #     (   'Категория',
        #         'Наименование',
        #         'Размер/Диаметр',
        #         'Марка стали',
        #         'Длина',
        #         'Цена за тонну',
        #     )
        # )

    for category_name, category_url in all_categories.items():

        if 'г/к' in category_name:
            category_name = category_name.replace('г/к', 'гк')
        if 'х/к' in category_name:
            category_name = category_name.replace('х/к', 'хк')

        req = requests.get(url=category_url, headers=headers)
        src = req.text

        with open(f'data/{count}_{category_name}.html', 'w', encoding='utf-8') as file:
            file.write(src)

        with open(f'data/{count}_{category_name}.html', encoding='utf-8') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')

        # формируем заголовки CSV
        # with open(f'result/csv/{count}_{category_name}.csv', 'w', encoding='cp1251') as file:
        #     writer = csv.writer(file, delimiter=';', lineterminator='\n')
        #     writer.writerow(
        #         (   'Категория',
        #             'Наименование',
        #             'Размер/Диаметр',
        #             'Марка стали',
        #             'Длина',
        #             'Цена за тонну',
        #         )
        #     )

        # собираем данные товаров
        # with open('../Price.csv', 'a', encoding='cp1251') as file:
        #     writer = csv.writer(file, delimiter=';', lineterminator='\n')
        #     writer.writerow(
        #         (
        #             category_name,
        #         )
        #     )

        try:
            product_data = soup.find('tbody').find_all('tr')
            # print(product_data)

            for item in product_data:
                product_td = item.find_all('td')
                title = product_td[0].text.replace('→', '').strip()
                diametr = product_td[1].text.strip()
                marka_stali = product_td[2].text.strip()
                dlina = product_td[3].text.strip()
                price = product_td[5].text.replace(' ', '').strip()

                with open(f'../Price.csv', 'a', encoding='cp1251') as file:
                    writer = csv.writer(file, delimiter=';', lineterminator='\n')
                    writer.writerow(
                        (
                            category_name,
                            title,
                            diametr,
                            marka_stali,
                            dlina,
                            price
                        )
                    )
                # print(title, diametr, marka_stali, dlina, price)

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


def main():
    get_data('https://mc.ru/products/msk')


if __name__ == '__main__':
    main()
