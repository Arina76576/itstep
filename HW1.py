print("\033[36mВизначення оцінки")
print('='*17,'\033[36m\n')
ans='1'
while ans=='1':
# for i in range(3):
    mark=int(input('\033[36m\033[2mВаша оцінка:'))
    if mark >=0 and mark <=49:
        print('\033[31mНезадовільно\n')
    elif 50<=mark<=69:
        print('\033[35mЗадовільно\n')
    elif 70<=mark<=89:
        print('\033[33mДобре\n')
    elif 90<=mark<=100:
        print('\033[32mВідмінно\n')
    else:
        print('\033[31mПомилка у введені оцінки')
    ans=input('\033[36mПродовжити (1-так | 2-ні)')
# print('========= END ==========')