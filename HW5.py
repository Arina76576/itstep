# Завдання 1
class Animal:
    def __init__(self, title, age, size):
        self.title=title
        self.size=size
        self.age=age
    def __str__(self):
        return 'Тварини мають: назву, наприклад: ' +self.title+ ' має ' +self.size+ ' розмір та вік ' +str(self.age)+ ' років.'
class Dog(Animal):
    def __init__(self, title, age, size, name, weight):
        super().__init__(title, age, size)
        self.name=name
        self.weight=weight
    def __str__(self):
        return super().__str__() + " Ім'я " +self.name+ " та вагу " +str(self.weight)+ " кг"
class Cat(Animal):
    def __init__(self, title, age, size, name, weight, color, sound):
        super().__init__(title, age, size)
        self.name=name
        self.weight=weight
        self.color=color
        self.sound=sound
    def __str__(self):
        return super().__str__() + " Ім'я " +self.name+ " та вагу " +str(self.weight)+ " кг. Його окрас " +self.color+ " та ще він видає звук " +self.sound+ "."

any = Animal('жирафа', 7, 'великий')
print(any)
d = Dog('Собака', 5, 'середній', 'Шарік', 7)
print(str(d))
c = Cat('Кот', 3, 'малий', 'Мурка', 5, 'рижий', 'мяу')
print(str(c))

# Завдання 2
class Vehicle:
    def __init__(self, name, speed, move):
        self.name=name
        self.speed=speed
        self.move=move
    def __str__(self):
        return self.name+ ' має швидкість: ' +str(self.speed)+ ' км/ч. Його переміщення є ' +self.move+'.'
class Bicycle(Vehicle):
    def __init__(self, name, speed, move, weight, type):
        super().__init__(name, speed, move)
        self.weight=weight
        self.type=type
    def __str__(self):
        return super().__str__()+ " Вага " +str(self.weight)+ " кг, тип: " +self.type+"."
class Car(Vehicle):
    def __init__(self, name, speed, move, brand, year,):
        super().__init__(name, speed, move)
        self.brand=brand
        self.year=year
    def __str__(self):
        return super().__str__()+ ' Марка ' +self.brand+ ' рік випуску машини ' +str(self.year)+'.'

moto=Vehicle('Мотоцикл', 150, 'дорожнім')
print(moto)
b=Bicycle('Велосипед', '75', 'дорожнім', '30', 'електро-велосипед')
print(str(b))
c=Car('Автомобіль', 280, 'дорожнім', 'Range Rover', 2025)
print(str(c))