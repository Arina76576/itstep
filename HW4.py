# Завдання 1
class Product:
    count=0
    def __init__(self, name='Товар', price=0, stock=0):
        self.name=name
        self.price=price
        self.stock=stock
        Product.count+=1
class Cart:
    def __init__(self):
        self.items=[]
    def add(self, *products):
        for product in products:
            if product.stock > 0:
                self.items.append(product)
                product.stock -= 1
                print('Товар', product.name, 'додано у кошик.')
            else:
                print('Товар', product.name, 'закінчився!')
    def remove(self, product):
        if product in self.items:
            self.items.remove(product)
            product.stock += 1
            print('Товар', product.name, 'видалено з кошика.')
        else:
            print('Товар', product.name, 'немає у кошику.')
    def total_price(self):
        return sum(item.price for item in self.items)
    def info(self):
        if not self.items:
            print("Кошик порожній.")
        else:
            print("Товари у кошику:")
            for item in self.items:
                print(item.name, item.price, 'грн')
            print('Загальна сума:', self.total_price(), 'грн')

prod1 = Product("Яблуко", 10, 5)
prod2 = Product("Банан", 15, 3)
prod3 = Product("Молоко", 35, 2)
cart = Cart()
cart.add(prod1, prod2, prod3)
cart.info()
cart.remove(prod1)
cart.info()
print("Загальна кількість товарів у магазині:", Product.count)

# Завдання 2
class BankAccount:
    def __init__(self, name, number, balance=0):
        self.name=name
        self.number=number
        self.balance=balance
    def deposit(self, amount):
        if amount>0:
            self.balance+=amount
            print('Поповнено', amount, 'грн. Новий баланс:', self.balance, 'грн.')
        else:
            print("Сума поповнення має бути більшою за 0.")
    def withdraw(self, amount):
        if amount>0:
            if self.balance>=amount:
                self.balance-=amount
                print('Знято', amount, 'грн. Новий баланс:', self.balance, 'грн.')
            else:
                print("Недостатньо коштів на рахунку.")
        else:
            print("Сума зняття має бути більшою за 0.")
    def __str__(self):
        return "Рахунок " + str(self.number) + " (" + self.name + "): " + str(self.balance) + " грн."
class Bank:
    def __init__(self):
        self.accounts = []
    def add_account(self, account):
        self.accounts.append(account)
        print('Рахунок', account.number, 'додано до банку.')
    def transfer(self, from_account, to_account, amount):
        if from_account in self.accounts and to_account in self.accounts:
            if amount>0:
                if from_account.balance>=amount:
                    from_account.balance-=amount
                    to_account.balance+=amount
                    print('Переказано', amount, 'грн з рахунку', from_account.number, 'на рахунок', to_account.number,'.')
                else:
                    print("Недостатньо коштів для переказу.")
            else:
                print("Сума переказу має бути більшою за 0.")
        else:
            print("Один або обидва рахунки не знайдено в банку.")
    def show_accounts(self):
        if not self.accounts:
            print("У банку немає рахунків.")
        else:
            print("Рахунки у банку:")
            for account in self.accounts:
                print(account)

acc1 = BankAccount("Дмитро", 1001, 5000)
acc2 = BankAccount("Олена", 1002, 3000)
acc3 = BankAccount("Іван", 1003, 10000)
bank = Bank()
bank.add_account(acc1)
bank.add_account(acc2)
bank.add_account(acc3)
bank.show_accounts()
acc1.deposit(2000)
acc2.withdraw(500)
bank.transfer(acc1, acc2, 1500)
bank.show_accounts()