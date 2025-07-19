import turtle
import pandas as pd 

def U_S_states_game():
    screen=turtle.Screen()
    screen.title("U.S states game ")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    data = pd.read_csv("50_states.csv")
    all_states = data.state.to_list()
    guessed_states = []
    while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 guessed items", prompt="Whats another states name?").title()
        if answer_state=="Exit":
            missing_state =[]
            for state in all_states:
                if state not in guessed_states:
                    missing_state.append(state)
            new_data = pd.DataFrame(missing_state)
            new_data.to_csv("missing states to learn ")
            break
        if  answer_state in all_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(answer_state)


def indian_states_game():
    screen=turtle.Screen()
    screen.title("Indian states game ")
    image = "indian_map.gif"
    screen.addshape(image)
    turtle.shape(image)
    data = pd.read_csv("indian_states_coordinates.csv")
    all_states = data.state.to_list()
    guessed_states = []
    while len(guessed_states) < 32:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/32 guessed items", prompt="Whats another states name?").title()
        if answer_state=="Exit" or answer_state == None:
            missing_state =[]
            for state in all_states:
                if state not in guessed_states:
                    missing_state.append(state)
            new_data = pd.DataFrame(missing_state)
            new_data.to_csv("missing states to learn ")
            break
        if answer_state in all_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(answer_state)

screen=turtle.Screen()
screen.title("WHICH STATE GAME DO U WANT TO PLAY ? ")
answer = screen.textinput(title="WHICH GAME DO U WANT TO PLAY ? ", prompt="INDIA or U.S ").title()
if answer == "India":
    indian_states_game()
else:
    U_S_states_game()


# screen.exitonclick()

# listx_y=[]
# # Function to handle mouse click and print coordinates
# # def get_mouse_click_coor(x, y):
# #     x_y = (x,y)
    
# #     listx_y.append(x_y)
# #     print(f"Clicked at: ({x}, {y})")
# #     print(listx_y)
# # # Set up the screen and bind the click event
# # screen = turtle.Screen()
# # screen.onscreenclick(get_mouse_click_coor)

# # # Keep the window open
# # turtle.mainloop()
# # print(listx_y)
