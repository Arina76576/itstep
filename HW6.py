# Завдання 1
import random as r
class Character:
    def __init__(self, name, health=100):
        self.__name = name
        self.__health = max(0, health)
    def take_damage(self, amount):
        self.__health = max(0, self.__health - amount)
        print(self.__name, 'отримав', amount, "шкоди. Залишилося здоров'я:", self.__health)
    def get_info(self):
        return self.__name, "Здоров'я:", self.__health
    def is_alive(self):
        return self.__health > 0
class Warrior(Character):
    def __init__(self, name, health=None):
        if health is None:
            health = r.randint(75, 100)
        super().__init__(name, health)
    def attack(self, target):
        damage = r.randint(10, 20)
        print(self.get_info(), 'атакує мечем і завдає', damage, 'шкоди', target.get_info())
        target.take_damage(damage)
class Mage(Character):
    def __init__(self, name, health=None):
        if health is None:
            health = r.randint(45, 75)
        super().__init__(name, health)
    def attack(self, target):
        damage = r.randint(15, 30)
        print(self.get_info(), 'атакує магією і завдає', damage, 'шкоди', target.get_info())
        target.take_damage(damage)

warrior = Warrior("Едвард")
mage = Mage("Мерлін")
print("Початковий стан персонажів:")
print(warrior.get_info())
print(mage.get_info())
print("\nБій починається:")
warrior.attack(mage)
if mage.is_alive():
    mage.attack(warrior)
print("\nСтан персонажів після бою:")
print(warrior.get_info())
print(mage.get_info())

# Завдання 2
class LibraryItem:
    def __init__(self, title, author, item_id):
        self.__title=title
        self.__author=author
        self.__item_id=item_id
        self.__is_checked_out=False

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get__item_id(self):
        return self.__item_id

    def is_checked_out(self):
        return self.__is_checked_out

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False

    def return_item(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False

    def __eq__(self, other):
        if isinstance(other, LibraryItem):
            return self.__item_id == other.__item_id
        return False

    def display_info(self):
        pass

class Book(LibraryItem):
    def __init__(self, title, author, item_id, pages):
        super().__init__(title, author, item_id)
        self.__pages=pages
    def get_pages(self):
        return self.__pages
    def display_info(self):
        print('Книга', self.get_title(), 'Автор', self.get_author(), 'Сторінки', self.get_pages())

class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number):
        super().__init__(title, author, item_id)
        self.__issue_number=issue_number
    def get_issue_number(self):
        return self.__issue_number
    def display_info(self):
        print('Журнал', self.get_title(), 'Автор', self.get_author(), 'Номер випуску', self.__issue_number)

class Audiobook(LibraryItem):
    def __init__(self, title, author, item_id, duration):
        super().__init__(title, author, item_id)
        self.__duration=duration
    def get_duration(self):
        return self.__duration
    def display_info(self):
        print('Аудіокнига', self.get_title(), 'Автор', self.get_author(), 'Тривалість', self.__duration)

items=[
    Book('Властелин колец', 'Джон Р. Р. Толкин', 'B434E', 700),
    Magazine("National Geographic", "Редакція", 'K007', 200),
    Audiobook('Гаррі Поттер і Напівкровний Принц', "Дж. К. Ролінг", 'A001', 8.5)
]
for item in items:
    item.display_info()
    print("-" * 50)

if items[0].check_out():
    print(items[0].get_title(), 'успішно взято.')
else:
    print(items[0].get_title(), 'вже взято.')
if items[0].return_item():
    print(items[0].get_title(), 'успішно повернуто.')
else:
    print(items[0].get_title(), 'вже доступне.')