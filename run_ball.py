import turtle
import random
from ball import Ball

def initialize_balls(num_balls, canvas_width, canvas_height, ball_radius):
    balls = []
    for _ in range(num_balls):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        x = random.randint(-canvas_width//2 + ball_radius, canvas_width//2 - ball_radius)
        y = random.randint(-canvas_height//2 + ball_radius, canvas_height//2 - ball_radius)
        vx = random.randint(-2, 2)
        vy = random.randint(-2, 2)
        ball = Ball(color, ball_radius, x, y, vx, vy, canvas_width, canvas_height)
        balls.append(ball)
    return balls

num_balls = int(input("Number of balls to simulate: "))
turtle.speed(0)
turtle.tracer(0)
turtle.hideturtle()
canvas_width = turtle.screensize()[0]
canvas_height = turtle.screensize()[1]
ball_radius = 0.05 * canvas_width
turtle.colormode(255)

balls = initialize_balls(num_balls, canvas_width, canvas_height, ball_radius)

while True:
    turtle.clear()
    for ball in balls:
        ball.draw()
        ball.move()
    turtle.update()

turtle.done()
