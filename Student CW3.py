import random as r
class Student:
    def __init__(self, name="Яна"):
        self.name=name
        self.happy=r.randint(50,100)
        self.progress=r.randint(1,12)
        self.isStudy=True
    def study(self):
        print('Час для навчання')
        self.happy-=r.randint(10,50)
        self.progress+=r.randint(1,3)
    def chill(self):
        print('Час для відпочинку')
        self.happy += r.randint(10, 50)
        self.progress -= r.randint(2, 5)
    def sleep(self):
        print('Час для сну')
        self.happy+=r.randint(1,20)
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
    def everyday(self):
        print('Рівень щастя:',self.happy)
        print('Прогрес навчання',self.progress)
    def studyLife(self,day):
        day='\n\033[36mДень №'+str(day)+'\033[0m'
        print(day)
        res=r.randint(1,3)
        if res==1:
            self.chill()
        elif res==2:
            self.sleep()
        else:
            self.study()
        self.everyday()
        self.isLife()

st1=Student()
print('\033[46mЖиття студента:', st1.name,'\033[0m')
# print(st1.progress)
for k in range(1,8):
    if st1.isStudy==False:
        break
    st1.studyLife(k)
print()
st2=Student('Саша')
print('\033[46mЖиття студента:', st1.name,'\033[0m')
# print(st1.progress)
for k in range(1,8):
    if st2.isStudy==False:
        break
    st1.studyLife(k)