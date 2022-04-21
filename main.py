from tabnanny import check
import tkinter
from turtle import fillcolor
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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        countdown(long_break_sec)
    elif reps %2 == 0:
        timer_label.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    else:
        timer_label.config(text="Work Time", fg=GREEN)
        countdown(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = (count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "√"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

img = tkinter.PhotoImage(file="tomato.png")

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_btn = tkinter.Button(text="Start", command=start_timer, bg=YELLOW, highlightthickness=0)
start_btn.grid(row=2, column=0)

reset_btn = tkinter.Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_btn.grid(row=2, column=2)

timer_label = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 55))
timer_label.grid(row=0, column=1)

check_mark = tkinter.Label(bg=YELLOW, fg=GREEN)
check_mark.grid(row=3, column=1)




window.mainloop()