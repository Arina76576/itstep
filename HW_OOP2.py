#Завдання 1
class Car:
    def __init__(self, year, model, make):
        self.year=year
        self.model=model
        self.make=make
    def info(self):
        print('Рік авто:',self.year)
        print('Модель авто:', self.model)
        print('Марка авто:', self.make)

auto=Car('2025','Velar', 'Range Rover')
auto.info()
year=int(input("> "))
model=input("> ")
make=input("> ")
auto2=Car(year,model,make)
auto2.info()

#Завдання 2
class Employee:
    def __init__(self, name="Анна", position="Програміст", salary='50.000$'):
        self.name=name
        self.position=position
        self.salary=salary
    def __str__(self):
        print('Заробітна плата')
        print("Заробітна плата:",str(self.salary),"Ім'я:",self.name,"Посада працівника:",str(self.position))
    def __bool__(self):
        return self.name!=None

p1=Employee()
p2=Employee("Максим","Програміст",'50.000$')
print(p2.__str__())
print(p1.__str__())
print(bool(p1))
print(p2.__bool__())