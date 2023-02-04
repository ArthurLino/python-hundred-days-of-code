import turtle
import random

screen = turtle.Screen()
screen.setup(height=400, width=800)
user_bet = screen.textinput(title="Make your bets", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
for index in range(len(colors)):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[index])
    turtles.append(new_turtle)

for index, turtle in enumerate(screen.turtles(), 1):
    turtle.penup()
    turtle.goto(x=-350, y=160 - 40 * index)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 350:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 20)
        turtle.forward(rand_distance)

screen.exitonclick()
