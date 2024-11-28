from turtle import Turtle
from random import randrange, randint

oren = Turtle()
oren.color('brown')
oren.shape('turtle')

eashen = Turtle()
eashen.color('#484a2a')
eashen.shape('turtle')

tony = Turtle()
tony.color('#8426ff')
tony.shape('turtle')

krish = Turtle()
krish.color('blue')
krish.shape('turtle')



oren.penup()
oren.goto(-160, 100)
oren.pendown()

eashen.penup()
eashen.goto(-160, 70)
eashen.pendown()

tony.penup()
tony.goto(-160, 40)
tony.pendown()

krish.penup()
krish.goto(-160, 10)
krish.pendown()


oran = randint(450,550)
eran = randint(430,540)
tran = randint(450,550)
kran = randint(450,550)

for movement in range(100):
    oren.forward(randint(100,oran)/100)
    eashen.forward(randint(100,eran)/100)
    tony.forward(randint(100,tran)/100)
    krish.forward(randint(100,kran)/100)

list = [["oren",oren.pos()[0]],["eashen",eashen.pos()[0]],["tony",tony.pos()[0]],["krish",krish.pos()[0]]]
biggest = 0
for i in range(4):
    if biggest < list[i][1]:
        biggest = list[i][1]
for i in range(4):
    if biggest == list[i][1]:
        print(list[i][0],"is first!")
smallest = 100000
for i in range(4):
    if smallest > list[i][1]:
        smallest = list[i][1]
for i in range(4):
    if smallest == list[i][1]:
        print(list[i][0],"is last")
