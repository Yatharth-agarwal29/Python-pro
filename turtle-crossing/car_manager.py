from turtle import Turtle
import random 

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
       self.all_cars=[]
       self.car_speed= STARTING_MOVE_DISTANCE

    def create_car(self):
        random_int= random.randint(1,6)
        if random_int==1:
              newcar= Turtle('square')
              newcar.shapesize( stretch_wid=1,stretch_len=2)
              newcar.penup()
              newcar.color(random.choice(COLORS))
              car_y = random.randint(-250,250)
              newcar.goto(300,car_y)
              self.all_cars.append(newcar)

    def move_car(self):
        for car in self.all_cars:
          car.backward(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    

            