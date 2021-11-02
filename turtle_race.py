from turtle import Turtle, Screen
from random import randint

is_race_on = False


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the bet? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []

y_coor = 100


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-220, y=y_coor)
    all_turtles.append(new_turtle)
    y_coor -= 40


if user_bet:
    is_race_on = True
    turtle_win = False
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>250:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You won! Winner is {winning_color}")
            else:
                print(f"You lose. Winner is {winning_color}")
        else:
            rand_distance = randint(0, 10)
            turtle.forward(rand_distance)



screen.exitonclick()
