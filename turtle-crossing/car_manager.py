from turtle import Turtle
from  random import *

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
       self.all_cars=[]

    def create_car(self):
        newcar= Turtle("Square")
        newcar.shapesize(stretch_len=1, stretch_wid=2)
        newcar.penup()
        newcar.color(random.choice(COLORS))
        car_y = randint(-250,250)
        newcar.goto(300,car_y)
        self.all_cars.append(newcar)

   # def move_car(self);
     #   for car in self.all_cars:
    #        car.backward(STARTING_MOVE_DISTANCE)

            