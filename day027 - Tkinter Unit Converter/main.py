from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=32, pady=32)

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles").grid(column=2, row=0)

equals_label = Label(text="is equal to").grid(column=0, row=1)
conversion_value_label = Label(text="0")
conversion_value_label.grid(column=1, row=1)
km_label = Label(text="Km").grid(column=2, row=1)


def calculate():
    miles = float(miles_input.get())
    kms = 1.60934 * miles
    conversion_value_label.config(text=f"{round(kms, 2)}")


conversion_button = Button(text="Calculate", command=calculate).grid(column=1, row=2)

window.mainloop()
