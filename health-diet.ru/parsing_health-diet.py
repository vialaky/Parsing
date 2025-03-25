import csv
import json
from logging import exception

import requests
from bs4 import BeautifulSoup

main_url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 '
                  'Safari/537.36'
}

folder = 'health-diet.ru/data/'
# filename = 'index.html'

def save_page(url, filename):
    try:
        r = requests.get(url, headers=headers)
        src = r.text

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(src)
            print(f'Main page saved as: {filename}')
    except requests.exceptions.ConnectionError:
        print(f'The page is not available: {url}.\nCheck your internet connection!')

if __name__ == "__main__":

    save_page(main_url, folder + 'index.html')



# with open('health-diet.ru/index.html', encoding='utf-8') as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
# all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')
#
# all_categories_dict = {}
# for item in all_products_hrefs:
#     # print(item)
#     item_text = item.text
#     item_href = 'https://health-diet.ru' + item.get('href')
#     # print(f'{item_text}: {item_href}')
#     all_categories_dict[item_text] = item_href
#
# # 3. Сохранение данных в JSON файл.
# # with open('health-diet.ru/all_categories_dict.json', 'w', encoding='utf-8') as file:
# #     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)
#
# with open('health-diet.ru/all_categories_dict.json', encoding='utf-8') as file:
#     all_categories = json.load(file)
# # print(all_categories)
#
#
# # 4. Замена нескольких символов в строке.
# iteration_count = int(len(all_categories)) - 1
# print(f'Всего итераций: {iteration_count}')
# count = 0
#
# for category_name, category_href in all_categories.items():
#     # if count == 0:
#     rep = [',', ' ', '-', "'"]
#     for item in rep:
#         if item in category_name:
#             category_name = category_name.replace(item, '_')
#     # print(category_name)
#     req = requests.get(url=category_href, headers=headers, proxies={"http": proxy, "https": proxy})
#     src = req.text
#
#     with open(f'health-diet.ru/data/{count}_{category_name}.html', 'w', encoding='utf-8') as file:
#         file.write(src)
#
#     # 5. Получение заголовков таблицы.
#     with open(f'health-diet.ru/data/{count}_{category_name}.html', encoding='utf-8') as file:
#         src = file.read()
#
#     soup = BeautifulSoup(src, 'lxml')
#
#     # проверка страницы на наличие таблицы c продуктами
#     alert_block = soup.find(class_='uk-alert-danger')
#     if alert_block is not None:
#         continue
#
#     # собираем заголовки таблицы
#     table_head = soup.find(class_='mzr-tc-group-table').find('tr').find_all('th')
#     # print(table_head)
#     product = table_head[0].text
#     calories = table_head[1].text
#     proteins = table_head[2].text
#     fats = table_head[3].text
#     carbohydrates = table_head[4].text
#     # print(carbohydrates)
#
#     # 6. Запись заголовков в csv файл.
#     with open(f'health-diet.ru/data/{count}_{category_name}.csv', 'w', encoding='utf-8-sig') as file:
#         writer = csv.writer(file, delimiter=';')
#         writer.writerow(
#             (
#                 product,
#                 calories,
#                 proteins,
#                 fats,
#                 carbohydrates
#             )
#         )
#
#     # 7. Получение химического состава продуктов со страницы.
#     products_data = soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')
#
#     product_info = []
#     for item in products_data:
#         product_tds = item.find_all('td')
#
#         title = product_tds[0].find('a').text
#         # print(title)
#         calories = product_tds[1].text
#         proteins = product_tds[2].text
#         fats = product_tds[3].text
#         carbohydrates = product_tds[4].text
#         # print(proteins)
#
#         # 8. Запись химического состава продуктов в csv файл.
#         with open(f'health-diet.ru/data/{count}_{category_name}.csv', 'a', encoding='utf-8-sig', newline="") as file:
#             writer = csv.writer(file, delimiter=';')
#             writer.writerow(
#                 (
#                     title,
#                     calories,
#                     proteins,
#                     fats,
#                     carbohydrates
#                 )
#             )
#
#         # 9. Создание списка и запись данных в json файл.
#         product_info.append(
#             {
#                 "Title": title,
#                 "Calories": calories,
#                 "Proteins": proteins,
#                 "Fats": fats,
#                 'Carbohydrates': carbohydrates
#             }
#         )
#
#     with open(f'health-diet.ru/data/{count}_{category_name}.json', 'a', encoding='utf-8-sig') as file:
#         json.dump(product_info, file, indent=4, ensure_ascii=False)
#
#     count += 1
#     print(f'# Итерация {count}. {category_name} записан...')
#     iteration_count -= 1
#
#     if iteration_count == 0:
#         print('Работа завершена')
#         break
#
#     print(f'Осталось итераций: {iteration_count}')
