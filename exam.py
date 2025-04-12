import requests as r
from bs4 import BeautifulSoup as bs

class Minfin:
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
        valute=[]
        valuteTag=self.soup.find_all('tr',class_='sc-1x32wa2-4 dKDsVV')[1:6]
        if not valuteTag:
            print('Не вдалося знайти необхідний тег/атрибут')
            return valute
        for i in valuteTag:
            nameValute=i.find('a',class_='sc-1x32wa2-7 ciClTw')
            name=nameValute.text.strip() if nameValute else 'Назва валюти відсутня'
            Valutee=i.find_all('td')
            #print(Valute)
            buy='Курс купівлі відсутній'
            sell='Курс продажу відсутній'
            if len(Valutee) > 2:
                buyValute=Valutee[1]
                buy=buyValute.text.strip() #if buyValute else 'Курс купівлі відсутній'
                sellValute=Valutee[2]
                sell=sellValute.text.strip() #if sellValute else 'Курс продажі відсутній'
            valute.append({
                'Назва':name,
                'Купівля':buy,
                'Продаж':sell
            })
        return valute

    def showInfo(self,txt):
        print('\033[31m№\t','НАЗВА','\t'*5,'КУПІВЛЯ','\t'*5,'ПРОДАЖ')
        print('-'*100,'\033[0m]')
        num=1
        for i in txt:
            print(num, i['Назва'] + ': Купівля - ', i['Купівля'] + ' грн, Продаж - ', i['Продаж'] + ' грн')
            num+=1

url='https://minfin.com.ua/ua/currency/'
obj=Minfin(url)
obj.auditSite()
txt=obj.getInfo()
obj.showInfo(txt) if txt else print('Жодної інформації не знайдено')

print('\033[36m\033[1mВиберіть дію:')
print('1 - Купити')
print('2 - Продати')
currencies = { 
    '1': 'USD',
    '2': 'EUR',
    '3': 'PLN',
    '4': 'CHF',
    '5': 'GBP'
}
ans = input(':')
if ans == '1':
    print('Виберіть валюту (введіть номер із списку):')
    currency_number = input(':') 
    if currency_number in currencies:
        print('Ваша валюта:', currencies[currency_number])
        print('Введіть суму:')
        sum = int(input(':'))
        print('Ваша сума:', sum)
        print('Ви хочете купити:', currencies[currency_number], 'на', sum, 'грн')