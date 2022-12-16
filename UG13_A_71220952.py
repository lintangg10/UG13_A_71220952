import turtle
s=turtle.Screen()


#turtle objek
t=turtle.Turtle()
t.speed(speed=0)

#D
t.penup()
t.goto(-330,-70)
t.pendown()
t.left(90)
t.forward(200)
t.penup()
t.left(90)
t.circle(100,180)
t.pendown()
t.circle(100,180)

#9
t.penup()
t.goto(-180,25)
t.pendown()
t.circle(-40)
t.penup()
t.circle(-40,270)
t.pendown()
t.forward(90)
t.circle(-35,180)
t.penup()

#5
t.penup()
t.goto(-120,55)
t.pendown()
t.forward(60)
t.right(90)
t.forward(90)
t.penup()
t.goto(-120,55)
t.pendown()
t.forward(35)
t.circle(-55,180)
t.forward(35)

#2
t.penup()
t.goto(0,90)
t.pendown()
t.right(90)
t.circle(-50,200)
t.right(20)
t.forward(120)
t.left(120)
t.forward(120)

#L
t.penup()
t.goto(180,130)
t.pendown()
t.right(90)
t.forward(180)
t.left(90)
t.forward(120)


s.exitonclick()

