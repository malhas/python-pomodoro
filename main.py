import time
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
window_count = ""

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global window_count
    reps = 0
    window.after_cancel(window_count)
    timer_label.config(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_clicked(running=False):
    global reps
    reps += 1

    if not running and window_count != "":
        window.after_cancel(window_count)

    if reps % 8 == 0:
        timer_label.config(text="Break", font=(FONT_NAME, 35, "bold"), fg=RED, bg=YELLOW)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_label.config(text="Break", font=(FONT_NAME, 35, "bold"), fg=PINK, bg=YELLOW)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
        count_down(WORK_MIN*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time_value):
    global reps
    global window_count
    minutes = math.floor(time_value/60)
    seconds = time_value % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if time_value > 0:
        window_count = window.after(1, count_down, time_value-1)
    else:
        start_clicked(True)
        if reps % 2 == 0:
            num_checks = CHECK_MARK * int(reps/2)
            print(num_checks)
            check_label.config(text=num_checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

check_label = Label(font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_clicked)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

window.mainloop()