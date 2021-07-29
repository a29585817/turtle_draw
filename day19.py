from turtle import Turtle, Screen
import random

is_goal = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color")
colors = ["red", "orange", "blue", "purple", "yellow", "green"]
turtle_name = []

for x in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + x * 40)
    turtle_name.append(new_turtle)

if user_bet:
    is_goal = True

while is_goal:

    for turtle in turtle_name:
        if turtle.xcor() > 230:
            is_goal = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win. winner is {winning_color}")
            else:
                print(f"You lost. winner is {winning_color}")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()