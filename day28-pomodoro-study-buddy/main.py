import sys, os, math, tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
BG = "#0d0f14"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
SECONDS = 60
timer = None
started = False

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global REPS, timer
    REPS = 0
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- #

# prevents multiple timers being started
def start():
    global started
    if started:
        reset_timer()
        started = False
    else:
        started = True
        start_timer()

# main timer loop
def start_timer():
    global REPS
    REPS += 1

    checkmark_label["text"] = "✓" * math.floor(REPS/2)

    if REPS % 8 == 0:
        count_down(LONG_BREAK_MIN * SECONDS)
        timer_label.config(text="Break", fg="red")
    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN * SECONDS)
        timer_label.config(text="Break", fg="red")
    else:
        count_down(WORK_MIN * SECONDS)
        timer_label.config(text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=str(f"{count_min}:{count_sec}"))
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.configure(bg=BG, padx=20, pady=20)
window.title("Pomodoro | Study Buddy")
window.minsize(width=500, height=500)

# tomato image
canvas = tk.Canvas(width=400, height=400, bg=BG, bd=0, highlightthickness=0)
canvas.grid(row=2, column=1)
tomato_img = tk.PhotoImage(file=resource_path("tomato.png"))
canvas.create_image(200, 200, image=tomato_img)
timer_text = canvas.create_text(200, 220, text="00:00", fill='#2a2f3f', font=(FONT_NAME, 30, "bold"))

# labels
checkmark_label = tk.Label(text="", fg="#4afa8a", bg=BG, padx=20, pady=20, font=(FONT_NAME, 20, "bold"))
checkmark_label.grid(row=3, column=1)

timer_label = tk.Label(text="Timer", fg="#4afa8a", bg=BG, font=(FONT_NAME, 38, "bold"))
timer_label.grid(row=1, column=1)

# buttons
start_button = tk.Button(text="Start", fg="#4afa8a", bg="#2a2f3f", bd=1, highlightthickness=0, font=(FONT_NAME, 26, "bold"), command=start)
start_button.grid(row=3, column=0)

reset_button = tk.Button(text="Reset", fg="#4afa8a", bg="#2a2f3f", bd=1, highlightthickness=0, font=(FONT_NAME, 26, "bold"), command=reset_timer)
reset_button.grid(row=3, column=2)

window.mainloop()