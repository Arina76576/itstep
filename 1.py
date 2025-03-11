print('\033[36m\033[1mПідтвердження особистості')
print('='*25,'\033[0m\n')
# ans='1'
# while ans=='1':
for kol in range(3):
    age=int(input('Ваш вік:'))
    print('\033[36m\033[1m')
    if age >=0 and age <14:
        print('Свідоцтво про народження')
    elif 14<=age<=35:
        print('id-паспорт')
    elif 35<age<=110:
        print('Паспорт старого зразку')
    else:
        print('Помилка у введені віку')
    print('\033[0m')
    # ans=input('Продовжити (1-так | 2-ні)')
print('========= END ==========')