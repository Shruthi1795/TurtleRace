import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput("Turtle Race - Make your bet!","Which turtle will win the race? Enter the colour: ")
color = ["red","orange","yellow","green","blue","purple"]
all_turtles = []

v = -100
for i in color:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(i)
    v += 30
    new_turtle.goto(x=-230, y=v)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in all_turtles:
        if i.xcor()>230:
            is_race_on = False
            winning_color = i.pencolor()
            if winning_color == user_bet:
                print("You've won!")
            else:
                print(f"You lose !! The {winning_color} turtle is the winner")
        dis = random.randint(0,10)
        i.forward(dis)

screen.exitonclick()
