# Pomodoro Study Timer
# Author >>> Yago Goltara
# ----------------------------- MODULES -------------------------------- #
from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
GREY = "#2C2E43"
YELLOW = "#FFD523"
WHITE = "#FDFAF6"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer
    root.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text='00:00')
    checkmark.config(text='')


# -------------------------- TIMER MECHANISM ---------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 2 == 1:
        count_down(WORK_MIN * 60)
    elif reps % 8 == 0:
        reps = 0
        checkmark.config(text='')
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, timer

    minutes = floor(count / 60)
    seconds = count % 60
    if reps == 7:
        checkmark.config(text='✓✓✓✓')
    elif reps == 5:
        checkmark.config(text='✓✓✓')
    elif reps == 3:
        checkmark.config(text='✓✓')
    elif reps == 1:
        checkmark.config(text='✓')
    else:
        pass

    if count > 0:
        if minutes < 10 and seconds < 10:
            canvas.itemconfig(timer_text, text=f'0{minutes}:0{seconds}')
        elif minutes < 10:
            canvas.itemconfig(timer_text, text=f'0{minutes}:{seconds}')
        elif seconds < 10:
            canvas.itemconfig(timer_text, text=f'{minutes}:0{seconds}')
        else:
            canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
        timer = root.after(1000, count_down, count-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# Screen
root = Tk()
root.minsize(width='600', height='600')
root.title('Pomodoro Pineapple')
root.config(bg=GREY)
root.resizable(False, False)

# Canvas
canvas = Canvas(root, width=512, height=512, bg=GREY, highlightthickness=0)
canvas_image = PhotoImage(file='pineapple.png')
canvas.create_image(256, 256, image=canvas_image)
canvas.place(x=44, y=44)

# Timer Label
title_label = Label(text='Pomodoro Timer', font=(FONT_NAME, 18, 'bold'), bg=GREY, fg=YELLOW)
title_label.place(x=20, y=10)

# Start Button
start_button = Button(text='start', font=(FONT_NAME, 10), bg=YELLOW, fg=GREY, command=start_timer)
start_button.place(x=25, y=550)

# Reset Button
reset_button = Button(text='reset', font=(FONT_NAME, 10), bg=YELLOW, fg=GREY, command=reset_timer)
reset_button.place(x=525, y=550)

# Timer
timer_text = canvas.create_text(256, 300, text='00:00', font=(FONT_NAME, 40, 'bold'), fill=WHITE)

# Checkmark
checkmark = Label(text='', font=(FONT_NAME, 18, 'bold'), bg=GREY, fg=YELLOW)
checkmark.place(x=250, y=560)

root.mainloop()
