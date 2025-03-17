#Завдання 1
class Car:
    count=0
    def __init__(self, year, model, make):
        self.year=year
        self.model=model
        self.make=make
        Car.count+=1
    def info(self):
        print('Рік авто:',self.year)
        print('Модель авто:', self.model)
        print('Марка авто:', self.make)

year=int(input("> "))
model=input("> ")
make=input("> ")
auto2=Car(year,model,make)
auto2.info()

#Завдання 2