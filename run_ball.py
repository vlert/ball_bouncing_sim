import turtle
from ball import Simulation

def main():
    num_balls = int(input("Number of balls to simulate: "))
    turtle.speed(0)
    turtle.tracer(0)
    turtle.hideturtle()
    canvas_width = turtle.screensize()[0]
    canvas_height = turtle.screensize()[1]
    ball_radius = 0.05 * canvas_width
    turtle.colormode(255)

    simulation = Simulation(num_balls, canvas_width, canvas_height, ball_radius)

    while True:
        simulation.update()
        simulation.draw()

if __name__ == "__main__":
    main()
    turtle.done()
