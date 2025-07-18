import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.create_car()
    carManager.move_car()

#finding colision 
    for car in carManager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
#finding crossing
    if player.is_at_Finish_line():
            player.goto_start()
            carManager.level_up()
            scoreboard.increase_level()


screen.exitonclick()