from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    password = password_entry.get()
    email = email_username_entry.get()
    is_ok = False
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title='Oops', message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', mode='r') as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open('data.json', mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', mode='w') as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showwarning(title='Oops', message="Please don't leave essentials fields empty!")
    else:
        try:
            with open('data.json', mode='r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showwarning(title='Error', message="No Data File Found.")
        else:
            if website in data:
                email = data[website]['email']
                password_data = data[website]['password']
                messagebox.showinfo(title=website, message=f'Email: {email}\n'
                                                               f'Password: {password_data}')
            else:
                messagebox.showwarning(title='Error', message=f'No details for {website} exists.')

        




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

lbl_website = Label(text='Website:')
lbl_website.grid(column=0, row=1)

website_entry = Entry(width=20)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=1)

lbl_email_username = Label(text='Email/Username:')
lbl_email_username.grid(column=0, row=2)

email_username_entry = Entry(width=38)
email_username_entry.insert(0, 'yehor@email.com')
email_username_entry.grid(row=2, column=1, columnspan=2)

lbl_password = Label(text='Password:')
lbl_password.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text='Generate Password', width=13, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', width=13, command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()