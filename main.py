import requests
from bs4 import BeautifulSoup as bs
import sqlite3

mode = ["F","E","M","P","A"] #моды(континенты)
country = ["RUB"]#названия валют
for urls in mode:#цикл для заполнения названия валют
    url = f"https://www.exchange-rates.org/currentRates/{urls}/RUB"#подставляем мод в ссылку
    content = requests.get(url).content #скачиваем html
    soup = bs(content,"html.parser")#передаём его в парсер
    x_table = soup.find_all("table")#находим тег 
    for i in x_table:#проходимся по таблице
        for tr in i.find_all("tr"):#проходимся по строкам в таблице
            td = tr.find_all("td", attrs = {"class": "text-rate"})#находим тег с этим классом 
            for g in td:#извлекаем текст из тега
                
                country.append(g.a.attrs["href"][10:])#записываем в список название найденной валюты

rate = dict()
for ind,i in enumerate (country):#проходимся по стране(валюте)
    for j in mode:#проходимся по моду
        print(f"{ind + 1}/{len(country)}")#выводим сколько страниц спарселя
        url = f"https://www.exchange-rates.org/currentRates/{j}/{i}"#подставляем мод и валюту
        content = requests.get(url).content
        soup = bs(content,"html.parser")
        x_table = soup.find_all("table")
        result = []
        for i in x_table:
            for tr in i.find_all("tr"):
                td = tr.find_all("td", attrs = {"class": "text-rate"}) 
                for g in td:
                    
                    rate.update([(g.a.attrs["href"][6:],g.text)])#заполняем словарь
# result1 = [x for row in result for x in row]
f = open("valute.txt", "w")
for i in rate:
    f.write(f"{i} - {rate[i]}\n")#записываем в файл



f.close()