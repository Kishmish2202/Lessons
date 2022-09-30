import turtle

screen = turtle.getscreen()
t = turtle.Turtle()

class DrawShape:
    def draw(self,x,y,color= 'red'):
        if self.fill:
            t.color(color)
            t.begin_fill()
        t.penup()
        t.goto(0,0)
        t.goto(x,y)
        t.pendown()
        for _ in range(self.sides):
            t.forward(self.size)
            t.left(self.angle)
        if self.fill:
            t.end_fill()

class Rect(DrawShape):
    def __init__(self,size,fill=False):
        self.size = size
        self.sides = 4
        self.angle = 90
        self.fill = fill

class Circle():
    def __init__(self, fill= False):
        self.fill= fill

    def draw(self,x,y,size, color):
        t.penup()
        t.goto(x,y)
        t.pendown()
        if self.fill:
            t.color(color)
            t.begin_fill()
        t.circle(size)

        if self.fill:
            t.end_fill()
    

#gg = Gg(22,70, fill = False)
#gg.draw()
        

#rect = Rect(80,fill=True)
#rect.draw()

#rect = Rect(120,fill=True)
#rect.draw('blue')

#rect = Rect(40, fill = False)
#rect.draw()

#class Triangle(DrawShape):
#        def __init__(self,size,fill=False):
#            self.size = size
#            self.sides = 3
#            self.angle = 120
#            self.fill = fill

#triangle = Triangle(120,fill=True)
#triangle.draw('purple')

#rectangle = Rect(40,fill=True)
#rectangle.draw(0,80,color ='red')
#rectangle.draw(0,40,color ='yellow')
#rectangle.draw(0,0,color ='green')

gg = Rect(90,fill=True)
gg.draw(20,40,color= 'yellow')
gg.draw(60,40,'yellow')


oo = Circle(fill=True)
oo.draw(0,0,40,'black')
oo.draw(0,20,20,'white')
oo.draw(170,0,40,'black')
oo.draw(170,20,20,'white')




screen.mainloop()