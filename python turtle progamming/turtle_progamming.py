import turtle
import time

wn =turtle.Screen()
wn.bgcolor("green")
wn.title("Turtle Progamming")

skk = turtle.Turtle()

for i in range(360):
    skk.forward(1)
    skk.right(1)

for i in range(360):
    skk.forward(1)
    skk.left(1)
turtle.done()



