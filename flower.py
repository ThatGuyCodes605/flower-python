#!/usr/bin/env python

import turtle
import random
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)

def draw_random():
    colors = ["yellow", "red", "blue", "green", "white", "pink", "purple", "lime", "magenta", "#0000FF", "orange", "gray"]
    t.pencolor(random.choice(colors))

    for i in range(150):
        t.circle(190-i,90)
        t.lt(90)
        t.circle(190-i,90)
        t.lt(18)

    t.clear()


def stop_drawing():
    turtle.bye()

s.listen()
s.onkey(stop_drawing, "q")

while True:
    draw_random()
