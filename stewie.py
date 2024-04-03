import turtle

d = turtle.Turtle()
d.pensize(10)
d.speed(0)
d.shape("turtle")

#name
d.penup()
d.goto(0,600)
d.pendown()
d.color("#FFDAB9")
style = ("Ariel",30,"italic")
d.write("Stewie", font = style,move = True, align = "right")

#head
d.penup()
d.goto(-380,100)
d.lt(70)
d.pendown()
d.pencolor("black")
d.circle(-450,120)
d.penup()
d.goto(-360,90)
d.rt(170)
d.pendown()
d.circle(30,90)
d.circle(70,10)
d.circle(20,70)
d.circle(70,30)

turtle.done()