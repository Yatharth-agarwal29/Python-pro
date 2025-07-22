from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#60fa00"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = "00:00")
    label_.config(text = "Timer")
    label_1.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps 
    reps +=1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        label_.config(text="LONG BREAK", font=(FONT_NAME,40,"bold") , fg= RED , bg= YELLOW )
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        label_.config(text="SHORT BREAK", font=(FONT_NAME,40,"bold") , fg= PINK , bg= YELLOW )
    else :
        count_down(WORK_MIN)
        label_.config(text="WORk", font=(FONT_NAME,40,"bold") , fg= GREEN , bg= YELLOW )

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10 :
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text , text = f"{count_min}:{count_sec}" )
    if count >0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔  "
            label_1.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady= 50 , bg= YELLOW)
label_= Label(text="Timer", font=(FONT_NAME,40,"bold") , fg= GREEN , bg= YELLOW )
label_.grid(row=0 , column= 1)

tomato_img=PhotoImage(file="tomato.png")
canvas= Canvas(width=200 , height= 224 , bg= YELLOW , highlightthickness=0)
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="White",font=(FONT_NAME,28,"bold"))
canvas.grid(row=1 , column= 1)


Start_button=Button(text="Start" , command= start_timer )
Start_button.grid(row=2 , column= 0)
Reset_button = Button(text="Reset" , command = reset_timer )
Reset_button.grid(row=2 , column= 2)
label_1= Label(text="" , highlightthickness=0 )
label_1.grid(row=3 , column= 1)




window.mainloop()