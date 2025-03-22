'''
--------Звязок між класами---------
class Human:
    count=0
    def __init__(self, name='Петя'):
        self.name=name
        Human.count+=1
class Auto:
    def __init__(self,brand):
        self.brand=brand
        self.passenger=[]
    def add(self,*pas): #необмежена кіл аргументів
        for p in pas:
            self.passenger.append(p)
    def info(self):
        if self.passenger==[]:
            print('Маршрутка бренду',self.brand,'немає пасажирів')
        else:
            print('Маршрутка бренду', self.brand, 'має пасажирів')
            for p in self.passenger:
                print(p.name)

pas1=Human()
pas2=Human('Таня')
pas3=Human('Саша')
car=Auto('Богдан')
#car.add(pas1)
#car.add(pas2)
#car.add(pas3)
car.add(pas1,pas2,pas3)
car.info()
print('Кіл пасажирів:',Human.count)
'''


'''
# ------НАСЛІДУВАННЯ КЛАСІВ-------
class Human:
    def __init__(self, name,age,height,national,city,weight):
        self.name=name
        self.age=age
        self.height=height
        self.national=national
        self.city=city
        self.weight=weight
    def __str__(self):
        return 'Вітаю! Я ' +self.name+' з міста ' +self.city+ ' мені ' +str(self.age)+ ' років. Мій зріст ' +str(self.height)+ ' та вага ' +str(self.weight) +'. Я - ' +self.national
class Pupil(Human):
    def __init__(self,name,age,height,national,city,weight,school,clas):
        super().__init__(name,age,height,national,city,weight)
        self.school=school
        self.clas=clas
    def __str__(self):
        return super().__str__()+ ' навчаюся у школі №'+str(self.school)+' в '+str(self.clas)+' класі'
# робітник
class Labourer(Human):
    def __init__(self,name,age,height,national,city,weight,job,experience):
        super().__init__(name,age,height,national,city,weight)
        self.job=job
        self.experience=experience
    def __str__(self):
        return super().__str__()+ ' моя праця ' (self.job)+' мій стаж праці '+str(self.experience)+' років'

woman=Human('Марина',20, 166,'вірменка','Запоріжжя',55)
print(woman) #1
p=Pupil(' Сашко', 11, 125, 'українець', 'Дніпро', 35, 42, 6)
print(str(p)) #2
L=Labourer('Михайло', 25, 180, 'українець', 'Київ', 80, 'програміст', 5)
print(str(L))
'''
'''
class PC:
    def __init__(self):
        super().__init__()
        self.model='Apple'
        self.memory=256

class Display:
    def __init__(self):
        super().__init__()
        self.resol='4k'

class Smart(PC,Display):
    def info(self):
        print('Смартфон моделі',self.model,"має параметри: об'м пам'яті", self.memory, 'а розширення екрану',self.resol)
'''
class Device:
    def __init__(self):
        super().__init__()
        self.name='Планшет'

class Portable:
    def __init__(self):
        super().__init__()
        self.weight=500

class Tablet(Device,Portable):
    def info(self):
        print('Пристрій', self.name, 'важіть', self.weight, ' гр.')

#tel=Smart()
#tel.info()
pl=Tablet()
pl.info()