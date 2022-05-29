import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
h=6
for i in range(350):#150
	c=colorsys.hls_to_rgb(h, 0.5,0.8)
	t.pencolor(c)
	h+= 0.05#0.005
	t.right(i-1)#i+1
	t.circle(20, i)
	t.forward(i-1)
	for j in range(1):#5
		t.forward(i-1)#i+1
		t.right(90)

t.hideturtle()
turtle.done()