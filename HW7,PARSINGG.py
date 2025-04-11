# Завдання 1
import requests as r
from bs4 import BeautifulSoup as bs


class Books:
    def __init__(self,url):
        self.url=url
        self.header={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup=None
    def auditSite(self):
        response=r.get(self.url,headers=self.header)
        if response.status_code==200:
            self.soup=bs(response.text,'html.parser')
        else:
            print('Не вдалося підключитися до сайту')
            return

    def getInfo(self):
        books=[]
        booksTag=self.soup.find_all('article',class_='product_pod')[:8]
        for book in booksTag:
            nameBooks=book.find('h3')
            name=nameBooks.text.strip() if nameBooks else 'Назва відсутня'
            priceBooks=book.find('p', class_='price_color')
            price=priceBooks.text.strip() if priceBooks else 'Ціна відсутня'
            ratingBooks=book.find('p', class_='star-rating')
            rating=ratingBooks.get('class')[1] if ratingBooks else 'Рейтинг відсутній'
            if rating=='One':
                rating='1'
            elif rating=='Two':
                rating='2'
            elif rating=='Three':
                rating='3'
            elif rating=='Four':
                rating='4'
            elif rating=='Five':
                rating='5'
            else:
                rating='0'
            books.append({
                'Назва':name,
                'Ціна':price,
                'Рейтинг':rating,
            })
        return books

    def showInfo(self,txt):
        print('\033[31m№\t','НАЗВА','\t'*5,'ЦІНА','\t'*5,'РЕЙТИНГ')
        print('-'*100,'\033[0m]')
        num=1
        for i in txt:
            print(num,i['Назва'],i['Ціна'],i['Рейтинг'])
            num+=1

url='http://books.toscrape.com/'
obj=Books(url)
obj.auditSite()
txt=obj.getInfo()
obj.showInfo(txt) if txt else print('Жодної інформації не знайдено')
# Завдання 2
import requests as r
from bs4 import BeautifulSoup as bs


class Ctrs:
    def __init__(self, url):
        self.url = url
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup = None

    def auditSite(self):
        response = r.get(self.url, headers=self.header)
        if response.status_code == 200:
            self.soup = bs(response.text, 'html.parser')
        else:
            print('Не вдалося підключитися до сайту')
            return

    def getInfo(self):
        phone = []
        phoneTag = self.soup.find_all('div',
                                      class_='pr MainProductCard-module__root___hxD6L CatalogProductList_card__AJzS0')[
                   :8]
        if not phoneTag:
            print('Не вдалося знайти необхідний тег/атрибут')
            return phone
        for i in phoneTag:
            namePh = i.find('span', class_='line-clamp-2 break-word MainProductCard-module__title___3fVuF')
            name = namePh.text.strip() if namePh else 'Назва відсутня'
            pricePh = i.find('span', class_='medium MainProductCard-module__price___34KIa')
            price = pricePh.text.strip() if namePh else 'Ціна відсутня'
            cashbackPh = i.find('span', class_='dib MainProductCard-module__cashbackValue___nzcmF')
            cashback = cashbackPh.text.strip() if namePh else 'Кешбек відсутній'
            phone.append({
                'Назва': name,
                'Ціна': price,
                'Кешбек': cashback
            })
        return phone

    def showInfo(self, txt):
        print('\033[31m№\t', 'НАЗВА', '\t' * 5, 'ЦІНА', '\t' * 5, 'КЕШБЕК')
        print('-' * 100, '\033[0m]')
        num = 1
        for i in txt:
            print(num, i['Назва'], i['Ціна'] + '₴', i['Кешбек'] + '₴')
            num += 1


url = 'https://www.ctrs.com.ua/smartfony/brand-samsung/'
obj = Ctrs(url)
obj.auditSite()
txt = obj.getInfo()
obj.showInfo(txt) if txt else print('Жодної інформації не знайдено')