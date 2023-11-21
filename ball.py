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
class Simulation:
    def __init__(self, num_balls, canvas_width, canvas_height, ball_radius):
        self.balls = []
        for _ in range(num_balls):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            x = random.randint(-canvas_width//2 + ball_radius, canvas_width//2 - ball_radius)
            y = random.randint(-canvas_height//2 + ball_radius, canvas_height//2 - ball_radius)
            vx = random.randint(-2, 2)
            vy = random.randint(-2, 2)
            ball = Ball(color, ball_radius, x, y, vx, vy, canvas_width, canvas_height)
            self.balls.append(ball)

    def update(self):
        for ball in self.balls:
            ball.move()

    def draw(self):
        turtle.clear()
        for ball in self.balls:
            ball.draw()
        turtle.update()