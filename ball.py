import turtle
import random

class Ball:
    def __init__(self, color, size, x, y, vx, vy, canvas_width, canvas_height):
        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

    def draw(self):
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if abs(self.x + self.vx) > (self.canvas_width - self.size):
            self.vx = -self.vx

        if abs(self.y + self.vy) > (self.canvas_height - self.size):
            self.vy = -self.vy
