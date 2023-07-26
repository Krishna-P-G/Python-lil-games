import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2.5)
            new_car.penup()
            new_car.color(random.choices(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_forward(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT

