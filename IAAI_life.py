# -*- coding: cp1252 -*-
from tkinter import *
from time import sleep
#from threading import Thread
from random import randint

#******************************************************************************************
#    LICENSE :
#
#    IAAI_life
#    Copyright (C) 2018  Sebastien SILVANO
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.
#
#    If not, see <https://www.gnu.org/licenses/>.
#******************************************************************************************

class AI():
    def __init__(self,name,sex):
        self.name = name
        self.age = 0
        if sex == 'female':
            self.sex = sex
            self.color = 'hot pink'
        else:
            self.sex = sex
            self.color = 'blue'
        self.health = 100 #%
        self.happyness = 50 #%
        self.hunger = 100 #%
        self.thirst = 100 #%
        self.love = 50 #%
        self.loveHope = 0 #%
        self.couple = 'nobody'
        self.x = randint(10,maxl-50)
        self.y = randint(10,maxh-80)
        self.spd = 5
        self.childCnt = 0

class IAAI:
    def __init__(self):
        self.key = ''
        self.l = None
A = IAAI()
def getKey(k):
    A.key = k.char

def getReturn(k):
    A.key = 'return'

def getInput():
    sleep(0.4)
    e = Entry(world)
    e.pack()
    e.bind('<Return>',getReturn)
    A.key = ''
    while not (A.key == 'return'):
        e.focus_set()
        refresh()
    text = e.get()
    e.destroy()
    c.focus_set()
    return text

def text(t):
    print(t + " {at " + time + "}")
    A.l.destroy()
    A.l = Label(world,text=t + " {at " + time + "}",background='light blue')
    A.l.pack()

def checkLoveAble():
    if len(pop) < 2:
        return False
    temp1 = pop[0].sex
    for a in pop:
        if a.sex != temp1:
            return True
    return False

def check100meters(a,b):
    if not ( (pop[a].x+40 < pop[b].x-100 or pop[a].x > pop[b].x+140) or (pop[a].y+70 < pop[b].y-100 or pop[a].y > pop[b].y+170) ):
        return True
    return False

def refresh():
    c.delete(ALL)
    for a in lakes:
        if strokes:
            c.create_line(a[0]-40,a[1]-40,
                          a[0]+40,a[1]-40,
                          a[0]+40,a[1]+40,
                          a[0]-40,a[1]+40,
                          a[0]-40,a[1]-40,fill='light blue')
        c.create_rectangle(a[0]-20,a[1]-20,a[0]+20,a[1]+20,fill='light blue',outline='light blue')
    for a in plants:
        if strokes:
            c.create_line(a[0]-20,a[1]-20,
                          a[0]+20,a[1]-20,
                          a[0]+20,a[1]+20,
                          a[0]-20,a[1]+20,
                          a[0]-20,a[1]-20,fill='chartreuse')
        c.create_rectangle(a[0]-10,a[1]-10,a[0]+10,a[1]+10,fill='chartreuse',outline='chartreuse')
    for a in pop:
        c.create_rectangle(a.x,a.y,a.x+40,a.y+70,fill=a.color,outline='forest green')
        c.create_rectangle(a.x+5,a.y+10,a.x+35,a.y+15,fill='red4',outline='red4') #health
        c.create_rectangle(a.x+5,a.y+10,a.x+5+(30*a.health/100),a.y+15,fill='red',outline='red')
        c.create_rectangle(a.x+5,a.y+20,a.x+35,a.y+25,fill='grey15',outline='gray15') #age
        c.create_rectangle(a.x+5,a.y+20,a.x+5+(30*a.age/100),a.y+25,fill='gray55',outline='gray55')
        c.create_rectangle(a.x+5,a.y+30,a.x+35,a.y+35,fill='green4',outline='green4') #happyness
        c.create_rectangle(a.x+5,a.y+30,a.x+5+(30*a.happyness/100),a.y+35,fill='green2',outline='green2')
        c.create_rectangle(a.x+5,a.y+40,a.x+35,a.y+45,fill='saddle brown',outline='saddle brown') #hunger
        c.create_rectangle(a.x+5,a.y+40,a.x+5+(30*a.hunger/100),a.y+45,fill='dark orange',outline='dark orange')
        c.create_rectangle(a.x+5,a.y+50,a.x+35,a.y+55,fill='steel blue',outline='steel blue') #thirst
        c.create_rectangle(a.x+5,a.y+50,a.x+5+(30*a.thirst/100),a.y+55,fill='deep sky blue',outline='deep sky blue')
        c.create_rectangle(a.x+5,a.y+60,a.x+35,a.y+65,fill='DeepPink4',outline='DeepPink4') #love
        c.create_rectangle(a.x+5,a.y+60,a.x+5+(30*a.love/100),a.y+65,fill='deep pink',outline='deep pink')
        if strokes:
            c.create_line(a.x-100,a.y-100,
                          a.x+140,a.y-100,
                          a.x+140,a.y+170,
                          a.x-100,a.y+170,
                          a.x-100,a.y-100,fill=a.color)
        if a.couple != 'nobody':
            temp1 = 'died?'
            for b in pop:
                if a.couple == b.name:
                    temp1 = b.x
                    temp2 = b.y
                    temp3 = b.couple
                    break
            if temp1 != 'died?': #if partner found (x value set)
                if temp3 == a.name: #if this partner love me too
                    c.create_line(a.x+20,a.y+68,temp1+20,temp2+68,fill='red')
                else:
                    c.create_line(a.x+20,a.y+2,temp1+20,temp2+68,fill='yellow')
    A.key = ''
    c.update()
    sleep(1/fps)

#init
A.key = ''
maxl = 990
maxh = 640
fps = 60
world = Tk()
world.title('IAAI[0.0.1]')
c = Canvas(world,width=maxl-1,height=maxh-1,background='SpringGreen3')
c.bind('<KeyPress>',getKey)
c.focus_set()
c.pack()
A.l = Label(world,text="World created !",background='light blue')
A.l.pack()

deltaX = maxl-40
deltaY = maxh-40
divP = 7 #7^2 div for plants (49 chunks)
sizeP = [deltaX/divP,deltaY/divP]
divL = 7
sizeL = [deltaX/divL,deltaY/divL]
plants = []
for x in range(divP):
    for y in range(divP):
        plants.append([x*sizeP[0]+randint(0,int(sizeP[0]-1)),y*sizeP[1]+randint(0,int(sizeP[1]-1)),randint(1,4)]) #x, y, %/15day
lakes = []
for x in range(divL):
    for y in range(divL):
        lakes.append([x*sizeL[0]+randint(0,int(sizeL[0]-1)),y*sizeL[1]+randint(0,int(sizeL[1]-1))]) #x, y
pop = []

pop = [
    AI('Mathis'    ,'male'  ),
    AI('Elena'     ,'female'),
    AI('Adam'      ,'male'  ),
    AI('Eve'       ,'female'),
    AI('Nathalie'  ,'female'),
    AI('Eléonore'  ,'female'),
    AI('Sylvain'   ,'male'  ),
    AI('Etienne'   ,'male'  ),
    AI('Henry'     ,'male'  ),
    AI('Benoit'    ,'male'  ),
    AI('Stéphanie' ,'female'),
    AI('Candice'   ,'female'),
    AI('Anaïs'     ,'female'),
    AI('Arthur'    ,'male'  ),
    AI('Enzo'      ,'male'  ),
    AI('Mélissa'   ,'female'),
    AI('Ludivine'  ,'female'),
    AI('Frederic'  ,'male'  ),
    AI('Pedro'     ,'male'  ),
    AI('Axel'      ,'male'  ),
    AI('Marcel'    ,'male'  ),
    AI('Adrien'    ,'male'  ),
    AI('Lydia'     ,'female'),
    AI('Lucie'     ,'female'),
    AI('Stella'    ,'female'),
    AI('Emilie'    ,'female'),
    AI('Quentin'   ,'male'  ),
    AI('Rose'      ,'female'),
    AI('Camille'   ,'female'),
    AI('Antoine'   ,'male'  ),
    AI('Paul'      ,'male'  ),
    AI('Victoria'  ,'female'),
    AI('Elisa'     ,'female'),
    AI('Alexandre' ,'male'  ),
    AI('Loick'     ,'male'  ),
    AI('Denis'     ,'male'  ),
    AI('Thomas'    ,'male'  ),
    AI('Jeremy'    ,'male'  ),
    AI('Remi'      ,'male'  ),
    AI('Cynthia'   ,'female'),
    AI('Murielle'  ,'female'),
    AI('Clementine','female'),
    AI('Nathan'    ,'male'  )
]

timeSpd = 61 #days per real seconds
time = ''
timeDays = 0
timeMonths = 0
timeYears = 0
MATRICULE = 1
strokes = False
update = True
stand = True
while stand: #main
    timeDays += 10*timeSpd/fps
    if timeDays > 30:
        timeMonths += 1
        timeDays -= 30
    if timeMonths == 12:
        timeYears += 1
        timeMonths = 0
    time = '{0}y:{1}m:{2}d'.format(timeYears,timeMonths,int(round(timeDays,0)))
    if A.key == 'a' or A.key == 'A':
        text("===Create===\nChoose a name :")
        temp1 = getInput()
        text("Choose a sex : (male/female)")
        temp2 = getInput()
        pop.append(AI(temp1,temp2))
        text("AI created !")
    elif A.key == 's' or A.key == 'S':
        strokes = not strokes
    elif A.key == 'p' or A.key == 'P':
        text("====Pause===\nEnter anything to continue.")
        temp1 = getInput()
    elif A.key == 'c' or A.key == 'C':
        text("====Love====\nChoose someone :")
        temp1 = getInput()
        text("with an other one :")
        temp2 = getInput()
        for a in pop:
            if a.name == temp1:
                a.couple = temp2
        text("{0} fall in love with {1}.".format(temp1,temp2))
    elif A.key == 'u' or A.key == 'U':
        text("===Unlove===\nChoose someone :")
        temp1 = getInput()
        for a in pop:
            if a.name == temp1:
                temp2 = a.couple
                a.couple = 'nobody'
        text("{0} stop love {1}.".format(temp1,temp2))
    elif A.key == 'q' or A.key == 'Q':
        stand = False
    elif A.key == 't' or A.key == 'T':
        text("Actually :") # + " {at #time#}" set automaticaly (with text())
    for a in range(len(pop)):
        pop[a].age += (6*timeSpd/fps)/365.25 #every real second, earn 6 day (of age)
        if (pop[a].age > 80 and randint(0,500) == 300) or pop[a].age > 100:
            text(pop[a].name + ' die. (Too old)')
            del pop[a]
            break
        #hunger
        hunger = True
        for b in plants:
            if not( (pop[a].x+40 < b[0]-20 or pop[a].x > b[0]+20) or (pop[a].y+70 < b[1]-20 or pop[a].y > b[1]+20) ): #if pop[a] is near a plant (about 10px)
                hunger = False
        if hunger:
            pop[a].hunger -= (timeSpd/fps)/30 #every 30 days, lost 1% of hunger
        else:
            pop[a].hunger += (b[2]*timeSpd/fps)/15 #every 15 days, earn ?% of hunger (depending of the plant)
            pop[a].spd = 5 #immediately stop exciting himself when finally found food
        #thirst
        thirst = True
        for b in lakes:
            if not( (pop[a].x+40 < b[0]-40 or pop[a].x > b[0]+40) or (pop[a].y+70 < b[1]-40 or pop[a].y > b[1]+40) ): #if pop[a] is near a lake (about 20px)
                thirst = False
        if thirst:
            pop[a].thirst -= (timeSpd/fps)/15 #every 15 days, lost 1% of thirst
        else:
            pop[a].thirst += (3*timeSpd/fps)/10 #every 10 days, earn 3% of thirst
            pop[a].spd = 5 #immediately stop exciting himself when finally found water
        #love
        if checkLoveAble():
            married = False
            if pop[a].couple == 'nobody':
                if randint(0,50) == 25: # "Coup de foudre"
                    temp1 = randint(0,len(pop)-1)
                    if temp1 != a and pop[a].sex != pop[temp1].sex and check100meters(a,temp1): #if (it's not me) and (has the oposite sex) and (is next to me)
                        pop[a].couple = pop[temp1].name
                        pop[a].loveHope = 183 #% yes I know, it's > 100
                        text("{0} fall in love with {1}.".format(pop[a].name,pop[temp1].name))
            else:
                pop[a].loveHope -= (timeSpd/fps) #every day lost 1% love attachment (on 183%(days) <=> 1/2 year to stop love somebody that don't want you) 
                for b in pop: #check if the person you love loves you too
                    if pop[a].couple == b.name and b.couple == pop[a].name:
                        married = True
                        pop[a].loveHope = 183 #never forgive his/her love so regenerate the hope
            if pop[a].loveHope <= 0: #give up (he/she don't loves you)
                pop[a].couple = 'nobody'
            if not married:
                pop[a].love -= (timeSpd/fps)/(365.25*2) #every 20 day, lost 1% of love
                pop[a].happyness -= (1.2*timeSpd/fps)/15 #every 15 days, lost 1.2% of happyness
                pop[a].childCnt -= (timeSpd/fps)/10 #every 10 days lost 1 of childCnt
            else:
                pop[a].childCnt += (2*timeSpd/fps)/10 #every 10 days earn 2 of childCnt
                if pop[a].childCnt >= randint(65,80): #borning
                    MATRICULE += 1
                    pop[a].childCnt = 0
                    for b in range(len(pop)):
                        if pop[a].couple == pop[b].name:
                            pop[b].childCnt = 0
                            temp1 = pop[b].name
                    if randint(0,1):
                        sex = 'female'
                    else:
                        sex = 'male'
                    pop.append(AI(pop[a].name[:4]+temp1[len(temp1)-4:]+str(MATRICULE),sex))
                    if randint(0,100) == 5:
                        pop.append(AI(pop[a].name[:4]+temp1[len(temp1)-4:]+str(MATRICULE),sex))
                    text("{0} is born of {1} and {2} !\nCongratulations !".format(pop[a].name[:4]+temp1[len(temp1)-4:]+str(MATRICULE),pop[a].name,temp1))
                pop[a].love += (3*timeSpd/fps)/5 #every 5 days, earn 3% of love
                pop[a].happyness += (2*timeSpd/fps)/5 #every 5 days, earn 2% of happyness
        #health
        if pop[a].hunger < 45 or pop[a].thirst < 55:
            pop[a].health -= (timeSpd/fps)/20 #every 20 days, lost 1% of health
        if pop[a].thirst > 85 and pop[a].hunger > 85:
            pop[a].health += (2*timeSpd/fps)/5 #every 5 days, earn 2% of health
            pop[a].happyness += (3*timeSpd/fps)/10 #every 10 days, earn 3% of happyness
        if pop[a].health < 60:
            if pop[a].spd < 39:
               pop[a].spd += 1
            if pop[a].health < 30:
                pop[a].happyness -= (timeSpd/fps)/15 #every 15 days, lost 1% of happyness
        else:
            if pop[a].spd > 5:
                pop[a].spd -= 1
        #speed and moving
        if randint(0,75-pop[a].spd) < 8:
            if randint(0,1):
                pop[a].x += randint(-7*(pop[a].spd-4),7*(pop[a].spd-4))
            else:
                pop[a].y += randint(-7*(pop[a].spd-4),7*(pop[a].spd-4))
            if pop[a].x < 10:
                pop[a].x = 10
            elif pop[a].x > maxl-50:
                pop[a].x = maxl-50
            if pop[a].y < 10:
                pop[a].y = 10
            elif pop[a].y > maxh-80:
                pop[a].y = maxh-80
        #critical status
        if pop[a].health < 0:
            text(pop[a].name + " die. (Too sick)")
            del pop[a]
            break
        if pop[a].hunger < 0:
            text(pop[a].name + " die. (Too hungry)")
            del pop[a]
            break
        if pop[a].thirst < 0: 
            text(pop[a].name + " die. (Too thirsty)")
            del pop[a]
            break
        if pop[a].happyness < 0:
            pop[a].happyness = 0
        if pop[a].love < 0:
            pop[a].love = 0
        if pop[a].childCnt < 0:
            pop[a].childCnt = 0
        #super status
        if pop[a].health > 100:
            pop[a].health = 100
        if pop[a].happyness > 100:
            pop[a].happyness = 100
        if pop[a].hunger > 100:
            pop[a].hunger = 100
        if pop[a].thirst > 100:
            pop[a].thirst = 100
        if pop[a].love > 100:
            pop[a].love = 100
        if pop[a].childCnt > 100:
            pop[a].childCnt = 100
    refresh()
