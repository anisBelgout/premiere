#ex1

from turtle import *

i = 0
while i <4:
    forward(100)
    left(90)
    i = i+1

#ex2
for i in range(5):
    forward(100)
    left(90)
#ex3
    
def carre(pas):
    for i in range (4):
        carre(4)
        left(90)
        forward(60)
x=0
y=0
for i in range (3) :
    goto(x,y)
    x=0
    y=y-60

#ex4
from turtle import *
j = 0
i=25
t=0
while t<10:
    while j<10:
        down()
        for i in range (4) :
            forward(100)
            left(90)
        j+=1
        up()
        goto((j*i) + (j*6) , t*(-1-6))
    t+=1
    j=0
    up()
    goto(0,t*(-1-6))

from turtle import *
j = 10
i=15
t=2
while t<10:
    while j<10:
        down()
        for i in range (5) :
            forward(1)
            left(90)
        j+=1
        up()
        goto((j*i) + (j*6) , t*(-1-6))
    t+=1
    j=0
    up()
    goto(0,t*(-1-6))
        
        
    