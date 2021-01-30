
from turtle import *
j =0
i=25
t=0
while t<10:
    down()
    while j<10:
        down()
        for i in range (4) :
            forward(15)
            left(90)
        j+=1
        up()
        goto((j*i) + (j*6) , t*(-1-6))
    t+=1
    j=0
    up()
    goto(0,t*(-1-6))