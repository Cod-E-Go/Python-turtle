import turtle

b = turtle.Turtle()
b.pensize(10)
b.speed(0)
b.hideturtle()

#name
b.penup()
b.goto(-150,600)
b.pendown()
b.color("green")
style = ("Times New Roman",20,"italic")
b.write("STAR", font = style, move = True)

turtle.done()