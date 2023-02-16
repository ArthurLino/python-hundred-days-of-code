import turtle
import pandas

states = pandas.read_csv("50_states.csv")
all_states = list(states.state)
guessed_states = list()

screen = turtle.Screen()
screen.title("U.S. States Game")

states_img_path = "blank_states_img.gif"
screen.addshape(states_img_path)
turtle.shape(states_img_path)

game_is_on = True
while game_is_on:

    user_guess = screen.textinput(
        title=f"{len(guessed_states)}/50 States Guessed",
        prompt="Try guessing any state's name:"
    ).title()

    if user_guess == "Exit":
        missing_states = list()
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("last_missing_states.csv")
        break

    if user_guess in all_states and user_guess not in guessed_states:
        guessed_states.append(user_guess)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        index = all_states.index(user_guess)
        t.goto(states["x"][index], states["y"][index])
        t.write(user_guess)

screen.exitonclick()
