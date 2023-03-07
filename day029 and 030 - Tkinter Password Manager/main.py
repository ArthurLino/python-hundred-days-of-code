import json
from tkinter import messagebox
from tkinter import *
from pyperclip import copy as copy_to_clipboard
from password_generator import generate_password


def get_new_password():
    new_password = generate_password()
    password_input.insert(0, new_password)
    copy_to_clipboard(new_password)


def save_data():
    website = website_input.get().strip()
    login = login_input.get().strip()
    password = password_input.get().strip()

    for value in [website, login, password]:
        if value.strip() == "":
            messagebox.showerror(title="Oops", message="Please, make sure you haven't left any fields empty.")
            return

    new_data = {website: {"login": login, "password": password}}

    try:
        with open("data.json", "r") as data_file:
            existing_data = json.load(data_file)
    except FileNotFoundError:
        existing_data = new_data
    else:
        existing_data.update(new_data)

    with open("data.json", "w") as data_file:
        json.dump(existing_data, data_file, indent=4)

        website_input.delete(0, END)
        login_input.delete(0, END)
        password_input.delete(0, END)

        messagebox.showinfo(title="Ready!", message="Your data has been saved successfully!")


def find_data():
    try:
        with open("data.json", "r") as data_file:
            existing_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="It looks like you haven't saved any passwords.")
    else:
        website = website_input.get().strip()
        if website in existing_data:
            login_data = existing_data[website]
            messagebox.showinfo(title="Ready!", message=f"Here is your login for {website}:\n"
                                                        f"login: {login_data['login']}\n"
                                                        f"password: {login_data['password']}")
        else:
            messagebox.showerror(title="Oops", message=f"There is no info for: {website}.")


window = Tk()
window.title("Password Manager")
window.config(padx=24, pady=24)
window.resizable("false", "false")

logo_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1, padx=(80, 0))

# ---------- labels ----------

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="w", padx=8)

login_label = Label(text="Login:")
login_label.grid(row=2, column=0, sticky="w", padx=8)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="w", padx=8)

# ---------- inputs ----------

website_input = Entry()
website_input.focus()
website_input.grid(row=1, column=1, columnspan=1, sticky="ew")

login_input = Entry()
login_input.grid(row=2, column=1, columnspan=2, sticky="ew", pady=4)

password_input = Entry()
password_input.grid(row=3, column=1, sticky="nsew", pady=2)

# ---------- buttons ----------

search_button = Button(command=find_data, text="Search", borderwidth=0.5)
search_button.grid(row=1, column=2, sticky="nsew", padx=(16, 0), pady=2)

gen_password_button = Button(command=get_new_password, text="Generate Password", borderwidth=0.5)
gen_password_button.grid(row=3, column=2, sticky="nsew", padx=(16, 0), pady=2)

save_button = Button(command=save_data, text="Save")
save_button.grid(row=4, column=1, columnspan=2, sticky="ew", pady=16)

window.mainloop()
