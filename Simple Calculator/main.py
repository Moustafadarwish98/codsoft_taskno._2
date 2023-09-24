"""Importing Tkinter to use in the GUI design"""
from tkinter import *

"""Constants"""
BG_COLOR = "#17161b"
BUTTON_COLOR = "#2a2d36"
BUTTON_TEXT = "#fff"

"""Checking if there any previously saved results. if yes read it."""
try:
    with open(file="./saved_answers.txt", mode="r") as file:
        answer = file.read()
except FileNotFoundError:
    answer = ""

calculation = ""


def calculate(operation):
    """Writes the calculation that the user types to the Text widget, if the user wants to work
    with previous answer it writes to a file."""
    global calculation
    screen_result.delete(1.0, END)
    calculation += operation
    screen.delete(1.0, END)
    screen.insert(1.0, calculation)


def evaluation():
    """Evaluates the entered calculation (if possible) and write result in the result
    text widget on the right side. displays an error message if the calculation is not possible.
    Since it is a simple basic calculator it is safe to use the eval() function."""
    global calculation
    global answer
    try:
        result = str(eval(calculation))
        answer = result
        with open(file="saved_answers.txt", mode="w") as file:
            file.write(answer)
        screen_result.tag_config("right", justify="right")
        screen_result.insert(1.0, result)
        screen_result.tag_add("right", "1.0", "end")
    except:
        clear()
        screen.insert(1.0, "Error")


def clear():
    """Clears both screens"""
    global calculation
    calculation = ""
    screen.delete(1.0, END)
    screen_result.delete(1.0, END)


def delete():
    """delete last character element and use slicing to update the calculation"""
    global calculation
    calculation = calculation[:-1]
    screen.delete("end-2c")


"""Window setup"""
window = Tk()
window.geometry("335x268")
window.resizable(False, False)
window.title("Calculator")
window.config(bg=BG_COLOR)

"""Screens setup"""
screen = Text(window, width=22, height=1, font=("Arial", 20), highlightthickness=0)
screen.focus()
screen.grid(columnspan=5, row=0, sticky="w")
screen_result = Text(window, width=22, height=1, font=("Arial", 20), highlightthickness=0)
screen_result.grid(columnspan=5, row=1, sticky="w")

"""Buttons setup"""

""" Using lambda: in the commands to refer to the wanted function and be able to give the required 
 parameters."""
button_7 = Button(window, text="7", width=5, font=("Arial", 14),
                  command=lambda: calculate("7"), bg=BUTTON_COLOR,
                  fg=BUTTON_TEXT)
button_7.grid(row=2, column=0)
button_8 = Button(window, text="8", width=5, font=("Arial", 14),
                  command=lambda: calculate("8"), bg=BUTTON_COLOR,
                  fg=BUTTON_TEXT)
button_8.grid(row=2, column=1)
button_9 = Button(window, text="9", width=5, font=("Arial", 14),
                  command=lambda: calculate("9"), bg=BUTTON_COLOR,
                  fg=BUTTON_TEXT)
button_9.grid(row=2, column=2)
button_6 = Button(window, text="6", width=5, font=("Arial", 14),
                  command=lambda: calculate("6"), bg=BUTTON_COLOR,
                  fg=BUTTON_TEXT)
button_6.grid(row=3, column=0)
button_5 = Button(window, text="5", width=5, font=("Arial", 14),
                  command=lambda: calculate("5"), bg=BUTTON_COLOR,
                  fg=BUTTON_TEXT)
button_5.grid(row=3, column=1)
button_4 = Button(window, text="4", width=5, font=("Arial", 14),
                  command=lambda: calculate("4"), bg=BUTTON_COLOR,
                  fg=BUTTON_TEXT)
button_4.grid(row=3, column=2)
button_3 = Button(window, text="3", width=5, font=("Arial", 14),
                  command=lambda: calculate("3"), bg=BUTTON_COLOR,
                  fg=BUTTON_TEXT)
button_3.grid(row=4, column=0)
button_2 = Button(window, text="2", width=5, font=("Arial", 14),
                  command=lambda: calculate("2"), bg=BUTTON_COLOR,
                  fg=BUTTON_TEXT)
button_2.grid(row=4, column=1)
button_1 = Button(window, text="1", width=5, font=("Arial", 14),
                  command=lambda: calculate("1"), bg=BUTTON_COLOR,
                  fg=BUTTON_TEXT)
button_1.grid(row=4, column=2)
button_add = Button(window, text="+", width=5, font=("Arial", 14),
                    command=lambda: calculate("+"), bg=BUTTON_COLOR,
                    fg=BUTTON_TEXT)
button_add.grid(row=4, column=3)
button_subs = Button(window, text="-", width=5, font=("Arial", 14),
                     command=lambda: calculate("-"), bg=BUTTON_COLOR,
                     fg=BUTTON_TEXT)
button_subs.grid(row=4, column=4)
button_mult = Button(window, text="x", width=5, font=("Arial", 14),
                     command=lambda: calculate("*"), bg=BUTTON_COLOR,
                     fg=BUTTON_TEXT)
button_mult.grid(row=3, column=3)
button_div = Button(window, text="÷", width=5, font=("Arial", 14),
                    command=lambda: calculate("/"), bg=BUTTON_COLOR,
                    fg=BUTTON_TEXT)
button_div.grid(row=3, column=4)
button_right_bracket = Button(window, text="(", width=5, font=("Arial", 14),
                              command=lambda: calculate("("), bg=BUTTON_COLOR,
                              fg=BUTTON_TEXT)
button_right_bracket.grid(row=2, column=3)
button_left_bracket = Button(window, text=")", width=5, font=("Arial", 14),
                             command=lambda: calculate(")"), bg=BUTTON_COLOR,
                             fg=BUTTON_TEXT)
button_left_bracket.grid(row=2, column=4)
button_0 = Button(window, text="0", width=5, font=("Arial", 14),
                  command=lambda: calculate("0"), bg=BUTTON_COLOR,
                  fg=BUTTON_TEXT)
button_0.grid(row=5, column=0)
button_point = Button(window, text=".", width=5, font=("Arial", 14),
                      command=lambda: calculate("."), bg=BUTTON_COLOR,
                      fg=BUTTON_TEXT)
button_point.grid(row=5, column=1)
button_answer = Button(window, text="Ans", width=5, font=("Arial", 14),
                       command=lambda: calculate(answer), fg=BUTTON_TEXT,
                       bg=BUTTON_COLOR)
button_answer.grid(row=5, column=2)
button_clear = Button(window, text="AC", width=5, font=("Arial", 14),
                      command=lambda: clear(), fg=BUTTON_TEXT,
                      bg="#3498DB")
button_clear.grid(row=5, column=3)
button_equal = Button(window, text="=", width=30, font=("Arial", 14),
                      command=lambda: evaluation(), bg="#52BE80",
                      fg=BUTTON_TEXT)
button_equal.grid(row=6, column=0, columnspan=5)
button_delete = Button(window, text="DEL", width=5, font=("Arial", 14),
                       command=lambda: delete(), bg="#3498DB",
                       fg=BUTTON_TEXT)
button_delete.grid(row=5, column=4)

window.mainloop()

