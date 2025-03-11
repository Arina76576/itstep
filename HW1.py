print("\033[36mВизначення оцінки")
print('='*17,'\033[36m\n')
mark=int(input('Ваша оцінка:'))
print('\033[33m\033[2m')
if mark >=0 and mark <=49:
    print('\033[31mНезадовільно')
elif 50<=mark<=69:
    print('\033[35mЗадовільно')
elif 70<=mark<=89:
    print('\033[33mДобре')
elif 90<=mark<=100:
    print('\033[32mВідмінно')
else:
    print('\033[31mПомилка у введені оцінки')