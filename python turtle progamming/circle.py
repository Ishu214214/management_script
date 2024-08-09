import turtle



colors = ['red', 'blue', 'green', 'orange', 'yellow', 'purple']
wn = turtle.Screen()
wn.title("Turtel progamming")
wn.bgcolor("black")
skk = turtle.Pen()

for i in range(100): 
	skk.pencolor(colors[i%6])
	skk.circle(5*i) 
	skk.circle(-5*i) 
	skk.left(i) 

