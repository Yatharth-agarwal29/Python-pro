from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=300,width=500)
window.config(padx=150,pady=50)
def converter():
   miles1 = float(miles.get()) 
   km = miles1 * 1.60934
   answer_text.config(text=km , font=("Arial",12,"bold"))
   
miles = Entry(width=10)
miles.grid(column= 1, row= 0)

miles_text=Label(text = "Miles" , font=("Arial",12,"bold"))
miles_text.grid(column= 2, row= 0)

inkilo_text=Label(text = "is equal to ", font=("Arial",12,"bold"))
inkilo_text.grid(column= 0, row= 1)

answer_text = Label(text = "0" , font=("Arial",12,"bold"))
answer_text.grid(column= 1, row= 1)

kilo_text = Label(text="Km", font=("Arial",12,"bold"))
kilo_text.grid(column= 2, row= 1)



button=Button(text="Convert",font=("Arial",12,"bold") ,  command= converter  )
button.grid(column= 1, row= 3)


window.mainloop()