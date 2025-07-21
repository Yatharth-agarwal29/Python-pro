from tkinter import * 
window = Tk()
window.title("trial window ")
window.minsize(height=300,width=500)




my_lable = Label(text="i am a lable ",font=("Arial",24,"bold"))
my_lable.pack()

def button_clicked():
    new_text =inputt.get()
    my_lable.config(text= new_text)

button= Button(text="click me " , background="Blue", command=button_clicked)
button.pack()
inputt = Entry(textvariable="enter something")
inputt.pack()
print(inputt.get()) 



window.mainloop()