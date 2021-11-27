import turtle
import time

# Set up the window
window = turtle.Screen()
window.bgcolor("tan")
window.title("Simple analog clock using turtle made by Eyob zebene")
window.setup(width=640, height=620) # set up the height and width of the canvas window
window.tracer(0)  # stores all the drawings on the turtle to the memory & helps to display at one time when it is updated

# Set up the turtle
boss = turtle.Turtle()
boss.hideturtle()
boss.speed(10)
boss.shapesize(0.5,1,1)
boss.shape("arrow")
boss.fillcolor("blue")


def clock(hour, minute, second):
    # Set up the face of the clock
    boss.pencolor("black")
    boss.penup()
    boss.goto(0, 240)
    boss.setheading(180)
    boss.fillcolor("snow")
    boss.begin_fill()
    boss.pendown()
    boss.circle(240)
    boss.end_fill()
    boss.penup()

    # Set up the clock's counters
    boss.setheading(90)
    for i in range(60):
        boss.pensize(1.4)
        boss.pencolor("black")
        boss.goto(0,0)
        boss.dot()
        boss.forward(235)
        boss.pendown()
        boss.forward(5)
        boss.penup()
        boss.right(6)
    boss.setheading(90)
    for j in range(12):
        if j % 3 == 0:
            boss.goto(0 , 0)
            boss.forward(205)
            boss.pendown()
            boss.pensize(3)
            boss.forward(35)
            boss.penup()
            boss.right(30)# 30 is the angle the counters of a clock goes for each hour
        else:
            boss.pensize(2)
            boss.goto(0,0)
            boss.forward(220)
            boss.pendown()
            boss.forward(20)
            boss.penup()
            boss.right(30)
    # Set up the hour arm
    boss.setheading(90)
    boss.goto(0,0)
    boss.pencolor("green")
    boss.pensize(3)
    angle = (hour/12) * 360  # this is the angle each hour arm makes inside a circle when 1 hour is counted
    boss.right(angle)
    boss.pendown()
    boss.forward(100)
    boss.stamp()
    boss.penup()
    # Set up the minute arm
    boss.setheading(90)
    boss.goto(0, 0)
    boss.pencolor("yellow")
    boss.pensize(2)
    angle = (minute / 60) * 360   # this is the angle each minute arm make inside a circle when 1 minute is counted
    boss.right(angle)
    boss.pendown()
    boss.forward(160)
    boss.stamp()
    boss.penup()
    # Set up the second arm
    boss.setheading(90)
    boss.goto(0, 0)
    boss.pencolor("red")
    boss.pensize(1)
    angle = (second / 60) * 360      # this is the angle each second arm makes inside a circle when 1 second is counted
    boss.right(angle)
    boss.pendown()
    boss.forward(190)
    boss.stamp()
    boss.penup()


while True:
    hour = int(time.strftime("%I"))
    minute = int(time.strftime("%M"))
    second = int(time.strftime("%S"))
    clock(hour, minute, second)
    window.update()
    time.sleep(1)
    boss.clear()


window.mainloop()
