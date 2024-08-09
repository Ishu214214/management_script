import turtle



colors = ['red', 'blue', 'green', 'orange', 'yellow', 'purple']
wn = turtle.Screen()
wn.title("Turtel progamming")
wn.bgcolor("black")
skk = turtle.Pen()

for i in range(360):
    skk.pencolor(colors[i%6])
    skk.width(i//100 + 1)
    skk.forward(i)
    skk.left(59)