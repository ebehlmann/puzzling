import turtle

wn = turtle.Screen()

class Point:
    def __init__(self, xpos, ypos, xvel, yvel):
        self.xpos = xpos
        self.ypos = ypos
        self.xvel = xvel
        self.yvel = yvel

    def advance():
        self.xpos = self.xpos + self.xvel
        self.ypos = self.ypos + self.yvel

    def 



a = turtle.Turtle()
a.ht()
a.penup()
a.setpos(90, 10)
a.dot(size=2)

b = turtle.Turtle()
b.ht()
b.penup()
b.setpos(70, 0)
b.dot(size=2)

c = turtle.Turtle()
c.ht()
c.penup()
c.setpos(30, -20)
c.stamp()

wn.exitonclick()