from tkinter import *
import random
from tkinter import messagebox


###

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)



def password_generator():
    password_list = []
    for char in range(nr_letters):
        password_list.append(random.choice(letters))
    for char in range(nr_symbols):
        password_list += random.choice(symbols)
    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)



def save():
    website= website_entry.get()
    email= email_entry.get()
    password= password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Alcuni campi sono vuoti!")
    else:
        is_ok= messagebox.askokcancel(title=website, message=f"stai salvando {password} come password per il sito {website} realtivo alla mail {email}. Confermi?" )

    if is_ok == True:
        with open("data.txt", "a") as data:
            data.write(f"{website} | {email} | {password} \n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            pyperclip.copy(generate_password)





###
window=Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)


canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "mymail@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(column=2, row=3)
add_button= Button(text="Add", width=31, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

