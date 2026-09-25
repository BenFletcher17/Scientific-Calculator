# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 13:48:05 2026

@author: bendf
"""

import customtkinter as ctk
import math

app = ctk.CTk()

app.title("Scientific Calculator")
app.geometry("410x520")

app.resizable(False, False)

# Output section

display = ctk.CTkEntry(
    app,
    width=370,
    height=70,
    font=("Arial", 28),
    justify="right"
)

display.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=20,
    pady=20
)


# Button functions

def button_click(value):
    """
    Adds a number or symbol to the display.
    """
    display.insert("end", str(value))


def clear_display():
    """
    Clears the calculator.
    """
    display.delete(0, "end")


def backspace():
    """
    Deletes the last character.
    """
    current = display.get()

    if current:
        display.delete(0, "end")
        display.insert(0, current[:-1])


def calculate():
    """
    Calculates the expression.
    """
    expression = display.get()

    try:
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")

        answer = eval(expression)

        if isinstance(answer, float) and answer.is_integer():
            answer = int(answer)

        display.delete(0, "end")
        display.insert(0, str(answer))

    except:
        display.delete(0, "end")
        display.insert(0, "Error")


# Trig functions

def sine():
    try:
        number = float(display.get())

        answer = math.sin(math.radians(number))

        display.delete(0, "end")
        display.insert(0, str(round(answer, 10)))

    except:
        display.delete(0, "end")
        display.insert(0, "Error")


def cosine():
    try:
        number = float(display.get())

        answer = math.cos(math.radians(number))

        display.delete(0, "end")
        display.insert(0, str(round(answer, 10)))

    except:
        display.delete(0, "end")
        display.insert(0, "Error")


def tangent():
    try:
        number = float(display.get())

        answer = math.tan(math.radians(number))

        display.delete(0, "end")
        display.insert(0, str(round(answer, 10)))

    except:
        display.delete(0, "end")
        display.insert(0, "Error")


# Button creations

button_width = 80
button_height = 55


# Row 1

sin_button = ctk.CTkButton(
    app,
    text="sin",
    width=button_width,
    height=button_height,
    fg_color="#969433",
    command=sine
)

sin_button.grid(row=1, column=0, padx=5, pady=5)


cos_button = ctk.CTkButton(
    app,
    text="cos",
    width=button_width,
    height=button_height,
    fg_color="#969433",
    command=cosine
)

cos_button.grid(row=1, column=1, padx=5, pady=5)


tan_button = ctk.CTkButton(
    app,
    text="tan",
    width=button_width,
    height=button_height,
    fg_color="#969433",
    command=tangent
)

tan_button.grid(row=1, column=2, padx=5, pady=5)


clear_button = ctk.CTkButton(
    app,
    text="C",
    width=button_width,
    height=button_height,
    command=clear_display
)

clear_button.grid(row=1, column=3, padx=5, pady=5)


# Row 2 

open_bracket = ctk.CTkButton(
    app,
    text="(",
    width=button_width,
    height=button_height,
    fg_color="#B5752B",
    command=lambda: button_click("(")
)

open_bracket.grid(row=2, column=0, padx=5, pady=5)


close_bracket = ctk.CTkButton(
    app,
    text=")",
    width=button_width,
    height=button_height,
    fg_color="#B5752B",
    command=lambda: button_click(")")
)

close_bracket.grid(row=2, column=1, padx=5, pady=5)


backspace_button = ctk.CTkButton(
    app,
    text="⌫",
    width=button_width,
    height=button_height,
    fg_color="#963340",
    command=backspace
)

backspace_button.grid(row=2, column=2, padx=5, pady=5)


divide_button = ctk.CTkButton(
    app,
    text="÷",
    width=button_width,
    height=button_height,
    fg_color="#7C3396",
    command=lambda: button_click("÷")
)

divide_button.grid(row=2, column=3, padx=5, pady=5)


# Row 3

button_7 = ctk.CTkButton(
    app,
    text="7",
    width=button_width,
    height=button_height,
    command=lambda: button_click(7)
)

button_7.grid(row=3, column=0, padx=5, pady=5)


button_8 = ctk.CTkButton(
    app,
    text="8",
    width=button_width,
    height=button_height,
    command=lambda: button_click(8)
)

button_8.grid(row=3, column=1, padx=5, pady=5)


button_9 = ctk.CTkButton(
    app,
    text="9",
    width=button_width,
    height=button_height,
    command=lambda: button_click(9)
)

button_9.grid(row=3, column=2, padx=5, pady=5)


multiply_button = ctk.CTkButton(
    app,
    text="*",
    width=button_width,
    height=button_height,
    fg_color="#7C3396",
    command=lambda: button_click("*")
)

multiply_button.grid(row=3, column=3, padx=5, pady=5)


# Row 4

button_4 = ctk.CTkButton(
    app,
    text="4",
    width=button_width,
    height=button_height,
    command=lambda: button_click(4)
)

button_4.grid(row=4, column=0, padx=5, pady=5)


button_5 = ctk.CTkButton(
    app,
    text="5",
    width=button_width,
    height=button_height,
    command=lambda: button_click(5)
)

button_5.grid(row=4, column=1, padx=5, pady=5)


button_6 = ctk.CTkButton(
    app,
    text="6",
    width=button_width,
    height=button_height,
    command=lambda: button_click(6)
)

button_6.grid(row=4, column=2, padx=5, pady=5)


minus_button = ctk.CTkButton(
    app,
    text="-",
    width=button_width,
    height=button_height,
    fg_color="#7C3396",
    command=lambda: button_click("-")
)

minus_button.grid(row=4, column=3, padx=5, pady=5)


# Row 5

button_1 = ctk.CTkButton(
    app,
    text="1",
    width=button_width,
    height=button_height,
    command=lambda: button_click(1)
)

button_1.grid(row=5, column=0, padx=5, pady=5)


button_2 = ctk.CTkButton(
    app,
    text="2",
    width=button_width,
    height=button_height,
    command=lambda: button_click(2)
)

button_2.grid(row=5, column=1, padx=5, pady=5)


button_3 = ctk.CTkButton(
    app,
    text="3",
    width=button_width,
    height=button_height,
    command=lambda: button_click(3)
)

button_3.grid(row=5, column=2, padx=5, pady=5)


plus_button = ctk.CTkButton(
    app,
    text="+",
    width=button_width,
    height=button_height,
    fg_color="#7C3396",
    command=lambda: button_click("+")
)

plus_button.grid(row=5, column=3, padx=5, pady=5)


# Row 6

button_0 = ctk.CTkButton(
    app,
    text="0",
    width=button_width,
    height=button_height,
    command=lambda: button_click(0)
)

button_0.grid(row=6, column=0, padx=5, pady=5)


decimal_button = ctk.CTkButton(
    app,
    text=".",
    width=button_width,
    height=button_height,
    command=lambda: button_click(".")
)

decimal_button.grid(row=6, column=1, padx=5, pady=5)


equals_button = ctk.CTkButton(
    app,
    text="=",
    width=button_width,
    height=button_height,
    fg_color="#4A9633",
    command=calculate
)

equals_button.grid(row=6, column=2, padx=5, pady=5)

# Watermark
app.grid_rowconfigure(7, weight=1)

credit_text = ctk.CTkLabel(
    app,
    text="Ben Fletcher",
    font=("Arial", 8),
    text_color="gray"
)

credit_text.grid(
    row=7,
    column=3,
    sticky="se",
    padx=5,
    pady=2
)
app.mainloop()

"""
References:
https://customtkinter.tomschimansky.com/
https://www.geeksforgeeks.org/python/python-grid-method-in-tkinter/
https://developer-service.blog/customtkinter-a-complete-tutorial/
"""
