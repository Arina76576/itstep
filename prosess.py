# ПОЛІМОРФІЗМ
"""
class Animal:
    def sound(self):
        pass
class Cat(Animal):
    def sound(self):
        return 'Кішка - мявчить'
class Dog(Animal):
    def sound(self):
        return 'Собака - гавкає'
class Bird(Animal):
    def sound(self):
        return 'Птичка - чірікає'
def speak(anim):
    print(anim.sound())

a1=Cat()
a2=Dog()
a3=Bird()
speak(a1)
speak(a2)
speak(a3)
"""

"""
class Pay:
    def system(self, money):
        pass
class Cash(Pay):
    def system(self, money):
        return 'Оплата '+str(money)+'₴ була здійснена через готівку'
class Credit(Pay):
    def system(self, money):
        return 'Оплата '+str(money)+'₴ була здійснена через кредитну картку'
class Online(Pay):
    def system(self, money):
        return 'Оплата '+str(money)+'₴ була здійснена через онлайн систему'
payList=[Cash(), Credit(),  Online()]
for k in payList:
    print(k.system(125))
"""

#ІНКАПСУЛЯЦІЯ
#модифікатори доступу

"""
#1) public
class Dog:
    def __init__(self, name):
        self.name=name
dog1=Dog('Бакс')
print(dog1.name)
"""

"""
#2) private
class Dog:
    def __init__(self, name):
        self.__age=1
    def infoAge(self):
        return self.__age
dog1=Dog('Бакс')
print(dog1.infoAge())
#print(dog1.__age) #помилка у доступі, він приватний
"""

"""
#3) protected
class Dog:
    def __init__(self, name):
        self._breed='Лабрадор'
    class Puppy(Dog):
        def info(self):
            return 'Це щеня породи '+self._breed
dog1=Puppy('Бані')
print(dog1.info())
"""

"""
class Person:
    def __init__(self, name, age, salary):
        self.name=name #публічний атрибут
        self._age=age #захищений
        self.__salary=salary #приватний

    def info(self):
        print('Вітаю! Мене звати', self.name)
        self._infoAge()
        self.__infoSalary()

    def _infoAge(self):
        print('Мій вік', self._age)
    def __infoSalary(self):
        print('Моя ЗП', self.__salary)

class Employee(Person):
    def __init__(self, name, age, salary, pos):
        super().__init__(name, age, salary)
        self.pos=pos
    def infoEmp(self):
        print(self.name,'займає посаду',self.pos)
        self._infoAge()
        #self.__infoSalary()
        print('Вік', self._age)
        #print('ЗП:', self.__salary)

p1=Person('Олександр', 25, 35000)
e1=Employee('Олена', 32, 41000, 'дизайнер')

print(p1.name)
p1.info()
print(e1.name)
e1.infoEmp()
print(e1._Person__salary)
"""