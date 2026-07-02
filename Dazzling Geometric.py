import turtle
import random
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Python Artistry: Kaleidoscope")

t = turtle.Turtle()
t.speed(0)
t.width(2)

colors = ["red", "cyan", "yellow", "magenta", "green", "blue", "orange"]
def draw_kaleidoscope():
    for i in range(36):
        t.color(random.choice(colors))
        
        for j in range(6):
            t.forward(100)
            t.right(60)
        
        t.right(10)

for i in range(20):
    draw_kaleidoscope()
    t.right(18)

turtle.done()