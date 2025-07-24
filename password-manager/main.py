from tkinter import *
from tkinter import messagebox
from random  import *
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def genrate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_num = [choice(numbers) for _ in range(randint(2, 4)) ]

    password_list = password_letters + password_symbols + password_num
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password) #used to copy password on clipboard for easy use in copy() we put content to be copied 
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    item = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        item: {
            "email": email,
            "password": password
        }
    }
    if len(item) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please fill all the fields before Saveing ")
    else:
        is_ok = messagebox.askokcancel(title=item,message=f"These are the details enterd : \n Email : {item} \n Password: {password}, \n is it ok to Save?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
#-----------------------------------------------------------------------#    
def find_password():
    website=website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)    
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="NO data found")
    else:
        if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website,message=f"Password is : {password} \n Email is : {email}")
        else:
            messagebox.showerror(title="Error",message=f"NO data found for {website}")
# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")
image1=PhotoImage(file="logo.png")
canvas= Canvas(width=200 , height= 200 , highlightthickness=0)
canvas.create_image(100,100,image=image1 )
canvas.grid(row = 0, column= 1)

website_label = Label(text="Website :")
website_label.grid(row=1,column=0)

website_entry = Entry(width= 25)
website_entry.grid(row=1, column= 1 , columnspan= 1)
website_entry.focus()

website_Search_button = Button(text="Search" , command= find_password) #, command=Sch , website_entry
website_Search_button.grid(row=1 , column= 2 )
website_Search_button.config(width= 15)

email_label = Label(text="Email/Username")
email_label.grid(row=2,column=0)

email_entry = Entry(width= 40)
email_entry.grid(row=2, column= 1 , columnspan= 2)
email_entry.insert(END,"example@yatharth.agarwal.com")

password_label = Label(text="Password")
password_label.grid(row=3,column=0)

password_entry = Entry()
password_entry.config(width=22)
password_entry.grid(row=3,column=1)

password_button = Button(text="Genrate password" , command=genrate_password)
password_button.grid(row=3, column=2)
password_button.config(width=15)


add_button = Button(text="Add" , width= 44 , command= save_password)
add_button.grid(row=4, column= 1, columnspan= 2)




window.mainloop()