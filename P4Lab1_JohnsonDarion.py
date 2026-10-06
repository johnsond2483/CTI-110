# CTI-110
# P4Lab1 - Turtle
# Darion J
# 10/6/26

# Set up your turtle 
import turtle

screen = turtle.Screen()
screen.setup(800,600)
screen.title("P4LAB1")
screen.bgcolor("cyan4") # change this if you want

t = turtle.Turtle() # variable "t" now holds our turtle
# Set these to your preference
t.color("blue")
t.shape("turtle") # turtle, square, circle, triangle...
t.pencolor("blue")
t.fillcolor("orange")
t.pensize(3)

# Draw with t (your code here)
sides = 4
angle = 360 / sides
length = 100
# example 1 - while loop
with t.fill():
    while sides > 0:
        t.forward(length)
        t.right(angle)
        sides = sides - 1 

# example 2 - for loop
t.teleport(-200, 0)
sides = 4
t.begin_fill()
for side in range(sides):
    t.forward(length)
    t.right(angle)
t.end_fill()

# put a roof on the house?
sides = 3
t.fillcolor("black")
t.begin_fill()
for side in range(sides):
    t.forward(100)
    t.left(120)
t.end_fill()

# put a star in the sky
t.penup()
t.goto(200, 180)        # a place in the sky, above and right of the house
t.pendown()

t.fillcolor("gold")
t.pencolor("gold")
t.begin_fill()
for point in range(5):
    t.forward(80)
    t.right(144)        # the only big change: 90 became 144
t.end_fill()




# End - keep window open
turtle.done()