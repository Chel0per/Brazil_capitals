import turtle
import pandas

screen = turtle.Screen()
screen.title("Brazil capitals game")

image="brazil_map.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("brazilian_capitals.csv")
data_lower=pandas.read_csv("brazilian_capitals.csv")

data_lower["Cidade"] = data_lower["Cidade"].str.lower()

guessed_states = []

while(len(guessed_states) < 27):
    answer_capital = screen.textinput(title="Guess the Capital",prompt=str(len(guessed_states))+"/27 capitals guessed correctly")
    answer_lower=answer_capital.lower()

    if(len(data_lower[data_lower.Cidade == answer_lower]) == 1 and answer_lower not in guessed_states):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        capital_data = data[data.index == data_lower[data_lower.Cidade == answer_lower].index[0]]
        t.goto(int(capital_data.x),int(capital_data.y) - 6)
        t.write(capital_data.Cidade.item())
        guessed_states.append(answer_lower)
    else:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

screen.exitonclick()

