import random as r
class Student:
    def __init__(self, name="Яна"):
        self.name=name
        self.money=r.randint(100,1000)
        self.happy=r.randint(50,100)
        self.progress=r.randint(1,12)
        self.isStudy=True

    def study(self):
        print('Час для навчання')
        self.happy-=r.randint(10,50)
        self.progress+=r.randint(1,5)
        self.money-=r.randint(100,1000)

    def chill(self):
        print('Час для відпочинку')
        self.happy += r.randint(10, 50)
        self.progress -= r.randint(2, 5)
        self.money -= r.randint(100, 1000)

    def work(self):
        print('Треба працювати!')
        self.happy -= r.randint(10, 50)
        self.progress += r.randint(1, 12)
        self.money += r.randint(100, 1000)

    def sleep(self):
        print('Час для сну')
        self.happy+=r.randint(1,20)
        self.progress-=r.randint(1,5)
        self.money-=r.randint(100,1000)

    def isLife(self):
        if self.progress>6:
            print('Все добре з навчанням!',end='')
            if 7<=self.progress<10:
                print('Але можна трішки підтянути навчання')
            else:
                print('Відмінно вчишся!')
        elif 4<=self.progress<=6:
            print('Ти на грані відрахування...')
        else:
            print('Тебе відрахували із закладу')
            self.isStudy=False

    def isWork(self):
        if self.money>1000:
            print('Грошей достатньо!',end='')
            if 300<=self.progress<500:
                print('Треба більше працювати')
            else:
                print('Грошей хватає!')
        elif 100<=self.progress<=300:
            print('Не вистачає грошей')
        else:
            print('У тебе немає грошей')
            self.isStudy=False

    def everyday(self):
        print('Рівень щастя:',self.happy)
        print('Прогрес навчання:',self.progress)
        print('Кількість грошей:',self.money)

    def studyLife(self,day):
        day='\n\033[36mДень №'+str(day)+'\033[0m'
        print(day)
        res=r.randint(1,4)
        if res==1:
            self.chill()
        elif res==2:
            self.sleep()
        elif res==3:
            self.study()
        else:
            self.work()
            self.everyday()
            self.isLife()
            self.isWork()

st1=Student()
print('\033[46mЖиття студента:', st1.name,'\033[0m')
# print(st1.progress)
for k in range(1,8):
    if st1.isStudy==False:
        break
    st1.studyLife(k)
print()
st2=Student('Саша')
print('\033[46mЖиття студента:', st2.name,'\033[0m')
# print(st1.progress)
for k in range(1,8):
    if st2.isStudy==False:
        break
    st2.studyLife(k)