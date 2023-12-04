import turtle
import pandas

screen = turtle.Screen()
screen.title("US-Quiz")
img = 'blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed = []
while len(guessed) < 50:
    answer_state = screen.textinput(title=f'Guessed {len(guessed)}/50 states', prompt='Enter your guess').title()
    if answer_state == 'Exit':
        missing = [state for state in all_states if state not in guessed]
        new_data = pandas.DataFrame(missing)
        new_data.to_csv('Missed_states_csv')
        break
    if answer_state in all_states:
        guessed.append(answer_state)
        t = turtle.Turtle()

        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)




