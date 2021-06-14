"""Главный файл скрапера.

Файл содержит основную функцию, которая производит скраппинг и еще одну
дополнительную функцию, которая преобразует результаты скраппинга в
формат csv.
"""
import time
import csv
from random import randint

import requests
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from newbuilding import NewBuilding


def domrf_scrap(start_p, end_p):
    """Основная функция скрапера.

    Принимает начальную и конечную страницы, на которых нужно
    произвести скраппинг. Возвращает список полученных объектов.
    """
    pages = range(start_p, end_p+1)
    object_count = 0
    building_lst = []
    for page in pages:
        link = f'https://наш.дом.рф/сервисы/каталог-' \
                     'новостроек/список-объектов/список?page' \
                     '={page}&limit=100'
        # try блок на случай разрыва соединения
        try:
            options = Options()
            options.headless = True
            browser = webdriver.Firefox(options=options)
            browser.get(link)
            time.sleep(randint(3, 5))
            soup = BeautifulSoup(browser.page_source, 'lxml')
            # найти все объекты на странице
            item_lst = soup.find_all('div', class_="styles__Row-sc-13ibavg-0 styles__Content-gwedej-1 GCgIg")
            for item in item_lst:
                print('===========================================')
                object_count += 1
                print(f'Object {object_count}')
                address = item.find('a', class_="styles__Address-j3mki0-0 jXtiZU").string
                status_class = item.contents[0].contents[0].contents[0]['class'][1]
                if status_class == "hVoquA":
                    status = 'Сдан'
                elif status_class == "lhwaIV":
                    status = 'Строится'
                else:
                    status = 'Проблемный'
                appartments_num = item.contents[5].string
                builder = item.find('span', class_="styles__Ellipsis-sc-1fw79ul-0 cDcbYl styles__Child-b0i2cq-0 styles__Primary-b0i2cq-1 ccuZsf").string
                land_num = None
                app_sold = None
                square_m_price = None
                if status == 'Строится':
                    new_link = "https://xn--80az8a.xn--d1aqf.xn--p1ai" + str(item.parent['href']) 

                    r = requests.get(new_link)
                    soup = BeautifulSoup(r.text, 'lxml')
                    new_link = soup.find('a', class_="styles__Message-sc-1f4oj2n-1 ivaEOk")['href']
                    r = requests.get(new_link)
                    soup = BeautifulSoup(r.text, 'lxml')
                    land_num = soup.find('div', class_="styles__Wrapper-sc-15tpf9w-0 bRhCTB").contents[0].string
                    info = soup.find('div', class_="styles__InfoFlex-sc-1fvbtz4-0 edAoft").contents
                    app_sold = info[3].contents[1].string
                    square_m_price = info[4].contents[1].contents[0]
                building_lst.append(NewBuilding(address, status, appartments_num,
                                 builder, land_num, app_sold, square_m_price))
                print(address, status, appartments_num, builder, land_num, app_sold, square_m_price)
            browser.close()
        # в случае разрыва соединения показать страницу на которой
        # был остановлен поиск и сохранить результаты.
        except:
            print(f'stopped at {page}')
            return building_lst
    
    print(f"Num of entities scrapped is {len(building_lst)}")
    return building_lst


def create_csv(obj_lst):
    """Функция записывает результаты скраппинга в csv файл."""
    with open('newbuildings2.csv', 'w', newline='') as csvfile:
        fieldnames = ['Адрес','Статус','Кол-во квартир','Застройщик',
                      'Кадастровый номер','Распроданность','Цена(м2)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for obj in obj_lst:
            writer.writerow(obj.to_dict())


def main():
    start = time.time()
    create_csv(domrf_scrap(204, 271))
    print(f'Time elapsed: {time.time()-start} seconds')



if __name__ == '__main__':
    main()


