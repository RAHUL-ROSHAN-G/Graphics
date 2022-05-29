import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
h=6
for i in range(150):
	c=colorsys.hls_to_rgb(h, 0.5,0.8)
	t.pencolor(c)
	h+= 0.05
	t.right(i)
	t.circle(20, i)
	t.forward(i)
	for j in range(5):
		t.forward(i)
		t.right(90)

t.hideturtle()
turtle.done()