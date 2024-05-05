import tkinter as tk
import math


def on_click_button_nums(event):
    txt = event.widget.cget("text")
    if txt == ".":
        current_text = label2.cget("text")
        if "." not in current_text:
            label2.config(text=current_text + txt)
    else:
        current_text = label2.cget("text")
        label2.config(text=current_text + txt)


def on_click_clear(event):
    if event.widget.cget("text") == "C":
        label1.config(text="")
        label2.config(text="")
    elif event.widget.cget("text") == "CE":
        label2.config(text="")
    elif event.widget.cget("text") == "⌫":
        current_text = label2.cget("text")
        if current_text:
            label2.config(text=current_text[:-1])


def percentage(num):
    label1.config(text=str(num) + "% =")
    num1 = float(num) / 100
    label2.config(text=str(num1))


def inverse(num):
    if num == 0:
        label1.config(text=f"1 / {num} =")
        label2.config(text="Can't divide zero")
    else:
        label1.config(text=f"1 / {num} =")
        label2.config(text=str(1 / num))


def square(num):
    label1.config(text=f"{num}² =")
    label2.config(text=str(num ** 2))


def square_root(num):
    label1.config(text=f"√{num} =")
    label2.config(text=str(math.sqrt(num)))


def division(num):
    label1.config(text=f"{num} /")
    label2.config(text="")


def multiplication(num):
    label1.config(text=f"{num} *")
    label2.config(text="")


def subtraction(num):
    label1.config(text=f"{num} -")
    label2.config(text="")


def addition(num):
    label1.config(text=f"{num} +")
    label2.config(text="")


def equal():
    if "." in label1.cget("text"):
        num1 = float(label1.cget("text").split()[0])
        num2 = float(label2.cget("text"))
    else:
        num1 = int(float(label1.cget("text").split()[0]))
        num2 = int(float(label2.cget("text")))

    if "/" in label1.cget("text"):
        if num2 == 0:
            label1.config(text=f"{num1} / {num2} =")
            label2.config(text="Can't divide zero")
        else:
            label1.config(text=f"{num1} / {num2} =")
            label2.config(text=str(num1 / num2))
    elif "*" in label1.cget("text"):
        label1.config(text=f"{num1} * {num2} =")
        label2.config(text=str(num1 * num2))
    elif "-" in label1.cget("text"):
        label1.config(text=f"{num1} - {num2} =")
        label2.config(text=str(num1 - num2))
    elif "+" in label1.cget("text"):
        label1.config(text=f"{num1} + {num2} =")
        label2.config(text=str(num1 + num2))


def negate(num):
    label2.config(text=str(-num))


def on_click_calc(event):
    btn = event.widget.cget("text")

    if "." in label2.cget("text"):
        num = float(label2.cget("text"))
    else:
        num = int(float(label2.cget("text")))

    if btn == "%":
        percentage(num)

    elif btn == "¹/x":
        inverse(num)

    elif btn == "x²":
        square(num)

    elif btn == "√":
        square_root(num)

    elif btn == "/":
        division(num)

    elif btn == "*":
        multiplication(num)

    elif btn == "-":
        subtraction(num)

    elif btn == "+":
        addition(num)

    elif btn == "=":
        equal()

    elif btn == "±":
        negate(num)


root = tk.Tk()
icon_image = tk.PhotoImage(file="calc.png")
root.wm_iconphoto(True, icon_image)
root.title("Calculator")
root.config(padx=20, pady=20)

# Label
label1 = tk.Label(root, text="", anchor="e", font=("Arial", 16))
label1.grid(row=0, column=0, columnspan=4, sticky="ew")

label2 = tk.Label(root, text="", anchor="e", font=("Arial", 32))
label2.grid(row=1, column=0, columnspan=4, sticky="ew")

# Buttons
buttons = [
    ("%", 2, 0), ("CE", 2, 1), ("C", 2, 2), ("⌫", 2, 3),
    ("¹/x", 3, 0), ("x²", 3, 1), ("√", 3, 2), ("/", 3, 3),
    ("7", 4, 0), ("8", 4, 1), ("9", 4, 2), ("*", 4, 3),
    ("4", 5, 0), ("5", 5, 1), ("6", 5, 2), ("-", 5, 3),
    ("1", 6, 0), ("2", 6, 1), ("3", 6, 2), ("+", 6, 3),
    ("±", 7, 0), ("0", 7, 1), (".", 7, 2), ("=", 7, 3)
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 16), width=4, height=1)
    button.grid(row=row, column=column, padx=5, pady=5, sticky="ew")
    if text in [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        button.bind("<Button-1>", on_click_button_nums)
    elif text in ["%", "¹/x", "x²", "√", "/", "*", "-", "+", "=", "±"]:
        if text == "=":
            button.bind("Button-1")
        button.bind("<Button-1>", on_click_calc)
    elif text in ["CE", "C", "⌫"]:
        button.bind("<Button-1>", on_click_clear)


root.mainloop()
