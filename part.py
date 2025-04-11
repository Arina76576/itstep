# шаблон для парсингу
'''
import requests as r
from bs4 import BeautifulSoup as bs

class Name:
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
        pass
    def showInfo(self,txt):
        pass
url='посилання'
obj=Name(url)
obj.auditSite()
txt=obj.getInfo()
obj.showInfo(txt) if txt else print('Жодної інформації не знайдено')
'''

import requests as r
from bs4 import BeautifulSoup as bs

class Eldorado:
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
        tablet=[]
        tabletTag=self.soup.find_all('article',class_='iBdafB')[:5]
        if not tabletTag:
            print('Не вдалося знайти необхідний тег/атрибут')
            return tablet
        for i in tabletTag:
            nameTab=i.find('span',class_='bDXGew')
            name=nameTab.text.strip() if nameTab else 'Назва відсутня'
            priceTab=i.find('span', class_='ui-library-subtitle1Bold-399e')
            price=priceTab.text.strip() if nameTab else 'Ціна відсутня'
            tablet.append({
                'Назва':name,
                'Ціна':price,
            })
        return tablet

    def showInfo(self,txt):
        print('\033[31m№\t','НАЗВА','\t'*15,'ЦІНА')
        print('-'*80,'\033[0m]')
        num=1
        for i in txt:
            print(num,i['Назва'],i['Ціна']+'₴')
            num+=1

url='https://eldorado.ua/uk/tablet_pc/c1039006/'
obj=Eldorado(url)
obj.auditSite()
txt=obj.getInfo()
obj.showInfo(txt) if txt else print('Жодної інформації не знайдено')