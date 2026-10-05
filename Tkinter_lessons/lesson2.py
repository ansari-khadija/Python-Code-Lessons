import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime
import random


# ==========================================
# ✦ GLOSSY Y2K COLOR PALETTE ✦
# ==========================================

BG = "#EAF6FF"
ICE_BLUE = "#D8F0FF"
BABY_BLUE = "#BFE4F7"
BLUE = "#A9D7EF"

SILVER = "#D9DCE3"
LIGHT_SILVER = "#F7F8FB"
DARK_SILVER = "#AEB5C2"
PURE_WHITE = "#FFFFFF"

LILAC = "#DCD0F2"
LIGHT_LILAC = "#EEE8FA"
PURPLE = "#BBA9DD"
DARK_PURPLE = "#8975AA"

TEXT = "#454458"
SOFT_TEXT = "#77768A"

FILE_NAME = "tasks.json"


# ==========================================
# ✦ INSPIRATIONAL QUOTES ✦
# ==========================================

quotes = [
    "You are doing better than you think. ♡",
    "Small steps still move you forward. ✦",
    "Believe in your little dreams. ୨୧",
    "You don't have to rush. ☁",
    "Make today a little brighter. ☆",
    "Progress, not perfection. ♡",
    "Your future self will thank you. ✧",
    "Be proud of every small achievement. ♡",
    "One thing at a time. You got this! ✦",
    "Keep going, lovely. ୨୧",
    "Your effort matters. ♡",
    "Slow days are okay too. ☁"
]


# ==========================================
# ✦ LOAD TASKS ✦
# ==========================================

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


tasks = load_tasks()


# ==========================================
# ✦ SAVE TASKS ✦
# ==========================================

def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# ==========================================
# ✦ UPDATE COUNTER ✦
# ==========================================

def update_counter():

    remaining = sum(
        1 for task in tasks
        if not task["completed"]
    )

    counter_label.config(
        text=f"✦ {remaining} task"
             f"{'s' if remaining != 1 else ''} remaining ♡"
    )


# ==========================================
# ✦ DISPLAY TASKS ✦
# ==========================================

def display_tasks():

    for widget in task_frame.winfo_children():
        widget.destroy()

    if not tasks:

        empty_label = tk.Label(
            task_frame,
            text="✧ no little tasks yet ✧\nadd something lovely ♡",
            font=("Arial", 10, "italic"),
            bg=LIGHT_SILVER,
            fg=SOFT_TEXT,
            justify="center"
        )

        empty_label.pack(pady=45)

    for index, task in enumerate(tasks):

        # Chrome outer border
        task_outer = tk.Frame(
            task_frame,
            bg=DARK_SILVER,
            padx=1,
            pady=1
        )

        task_outer.pack(
            fill="x",
            pady=5
        )

        # Glossy inner frame
        task_row = tk.Frame(
            task_outer,
            bg=LIGHT_SILVER,
            padx=7,
            pady=6
        )

        task_row.pack(fill="x")

        # Checkbox
        if task["completed"]:
            symbol = "☑"
            task_color = "#A3A0AB"
        else:
            symbol = "□"
            task_color = TEXT

        check_button = tk.Button(
            task_row,
            text=symbol,
            font=("Arial", 15),
            bg=LIGHT_SILVER,
            fg=PURPLE,
            activebackground=LIGHT_SILVER,
            activeforeground=PURPLE,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=lambda i=index: toggle_task(i)
        )

        check_button.pack(side="left")

        # Task text
        task_label = tk.Label(
            task_row,
            text=task["text"],
            font=("Arial", 10),
            bg=LIGHT_SILVER,
            fg=task_color,
            anchor="w",
            wraplength=210
        )

        task_label.pack(
            side="left",
            fill="x",
            expand=True,
            padx=5
        )

        # Delete button
        delete_button = tk.Button(
            task_row,
            text="×",
            font=("Arial", 13, "bold"),
            bg=LIGHT_SILVER,
            fg=PURPLE,
            activebackground=LIGHT_SILVER,
            activeforeground=DARK_PURPLE,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=lambda i=index: delete_task(i)
        )

        delete_button.pack(side="right")

    update_counter()


# ==========================================
# ✦ ADD TASK ✦
# ==========================================

def add_task():

    task_text = task_entry.get().strip()

    if task_text == "":
        messagebox.showwarning(
            "✧ Little Reminder ✧",
            "Please enter a task first ♡"
        )
        return

    tasks.append({
        "text": task_text,
        "completed": False
    })

    task_entry.delete(0, tk.END)

    save_tasks()
    display_tasks()


# ==========================================
# ✦ TOGGLE TASK ✦
# ==========================================

def toggle_task(index):

    tasks[index]["completed"] = not tasks[index]["completed"]

    save_tasks()
    display_tasks()


# ==========================================
# ✦ DELETE TASK ✦
# ==========================================

def delete_task(index):

    del tasks[index]

    save_tasks()
    display_tasks()


# ==========================================
# ✦ CLEAR COMPLETED ✦
# ==========================================

def clear_completed():

    global tasks

    tasks = [
        task for task in tasks
        if not task["completed"]
    ]

    save_tasks()
    display_tasks()


# ==========================================
# ✦ CHANGE QUOTE ✦
# ==========================================

def change_quote():

    new_quote = random.choice(quotes)

    quote_label.config(
        text=f"“{new_quote}”"
    )


# ==========================================
# ✦ MAIN WINDOW ✦
# ==========================================

window = tk.Tk()

window.title("My Little To-Do ✧")
window.geometry("900x650")
window.configure(bg=BG)



# ==========================================
# ✦ TOP GLITTER ✦
# ==========================================

top_glitter = tk.Label(
    window,
    text="✦ ˚₊‧ ✧ ‧₊˚ ✦  💿  ✦ ˚₊‧ ✧ ‧₊˚ ✦",
    font=("Arial", 11),
    bg=BG,
    fg=PURPLE
)

top_glitter.pack(pady=(10, 4))


# ==========================================
# ✦ GLOSSY HEADER ✦
# ==========================================

header_outer = tk.Frame(
    window,
    bg=DARK_SILVER,
    padx=2,
    pady=2
)

header_outer.pack(
    fill="x",
    padx=35
)


header = tk.Frame(
    header_outer,
    bg=LIGHT_SILVER,
    height=105
)

header.pack(fill="x")


shine = tk.Label(
    header,
    text="━━━━━━━━ ✧ ━━━━━━━━",
    font=("Arial", 8),
    bg=LIGHT_SILVER,
    fg=PURE_WHITE
)

shine.pack(pady=(8, 0))


title = tk.Label(
    header,
    text="♡ My Little To-Do ♡",
    font=("Arial", 25, "bold"),
    bg=LIGHT_SILVER,
    fg=TEXT
)

title.pack(pady=2)


subtitle = tk.Label(
    header,
    text="a tiny planner for your everyday dreams",
    font=("Arial", 10, "italic"),
    bg=LIGHT_SILVER,
    fg=SOFT_TEXT
)

subtitle.pack()


header_deco = tk.Label(
    header,
    text="✧ ୨୧ ✦ 💿 ✦ ୨୧ ✧",
    font=("Arial", 10),
    bg=LIGHT_SILVER,
    fg=PURPLE
)

header_deco.pack(pady=5)


# ==========================================
# ✦ DATE ✦
# ==========================================

date_label = tk.Label(
    window,
    text="♡ " + datetime.now().strftime(
        "%A  •  %d %B %Y"
    ) + " ♡",
    font=("Arial", 10, "bold"),
    bg=BG,
    fg=SOFT_TEXT
)

date_label.pack(pady=10)


# ==========================================
# ✦ MAIN TWO-COLUMN AREA ✦
# ==========================================

main_area = tk.Frame(
    window,
    bg=BG
)

main_area.pack(
    fill="both",
    expand=True,
    padx=35
)


# ==========================================
# ✦ LEFT SIDE - TASKS ✦
# ==========================================

left_outer = tk.Frame(
    main_area,
    bg=DARK_SILVER,
    padx=2,
    pady=2
)

left_outer.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 10)
)


left_panel = tk.Frame(
    left_outer,
    bg=LIGHT_SILVER
)

left_panel.pack(
    fill="both",
    expand=True
)


left_heading = tk.Label(
    left_panel,
    text="✧ Today's Little Things",
    font=("Arial", 14, "bold"),
    bg=LIGHT_SILVER,
    fg=TEXT
)

left_heading.pack(
    anchor="w",
    padx=18,
    pady=(15, 8)
)


# ==========================================
# ✦ ADD TASK ✦
# ==========================================

input_outer = tk.Frame(
    left_panel,
    bg=DARK_SILVER,
    padx=1,
    pady=1
)

input_outer.pack(
    fill="x",
    padx=15
)


input_frame = tk.Frame(
    input_outer,
    bg=PURE_WHITE
)

input_frame.pack(fill="x")


task_entry = tk.Entry(
    input_frame,
    font=("Arial", 10),
    bg=PURE_WHITE,
    fg=TEXT,
    insertbackground=PURPLE,
    relief="flat",
    bd=0
)

task_entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=9,
    padx=8
)


add_button = tk.Button(
    input_frame,
    text="✦ ADD",
    font=("Arial", 9, "bold"),
    bg=LILAC,
    fg=TEXT,
    activebackground=PURPLE,
    activeforeground=PURE_WHITE,
    relief="flat",
    bd=0,
    padx=12,
    pady=7,
    cursor="hand2",
    command=add_task
)

add_button.pack(
    side="right",
    padx=4,
    pady=4
)


# ==========================================
# ✦ TASK FRAME ✦
# ==========================================

task_frame = tk.Frame(
    left_panel,
    bg=LIGHT_SILVER
)

task_frame.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=8
)


# ==========================================
# ✦ LEFT BOTTOM ✦
# ==========================================

left_bottom = tk.Frame(
    left_panel,
    bg=LIGHT_SILVER
)

left_bottom.pack(
    fill="x",
    padx=15,
    pady=(3, 15)
)


counter_label = tk.Label(
    left_bottom,
    text="✦ 0 tasks remaining ♡",
    font=("Arial", 9),
    bg=LIGHT_SILVER,
    fg=SOFT_TEXT
)

counter_label.pack(side="left")


clear_button = tk.Button(
    left_bottom,
    text="Clear completed",
    font=("Arial", 8),
    bg=BABY_BLUE,
    fg=TEXT,
    activebackground=BLUE,
    relief="flat",
    bd=0,
    padx=8,
    pady=5,
    cursor="hand2",
    command=clear_completed
)

clear_button.pack(side="right")


# ==========================================
# ✦ RIGHT SIDE - QUOTES ✦
# ==========================================

right_outer = tk.Frame(
    main_area,
    bg=DARK_SILVER,
    padx=2,
    pady=2
)

right_outer.pack(
    side="right",
    fill="both",
    expand=True,
    padx=(10, 0)
)


right_panel = tk.Frame(
    right_outer,
    bg=LIGHT_LILAC
)

right_panel.pack(
    fill="both",
    expand=True
)


# ==========================================
# ✦ QUOTE TITLE ✦
# ==========================================

quote_title = tk.Label(
    right_panel,
    text="✦ A Little Reminder ✦",
    font=("Arial", 15, "bold"),
    bg=LIGHT_LILAC,
    fg=TEXT
)

quote_title.pack(pady=(20, 10))


# ==========================================
# ✦ QUOTE CARD ✦
# ==========================================

quote_outer = tk.Frame(
    right_panel,
    bg=PURPLE,
    padx=2,
    pady=2
)

quote_outer.pack(
    fill="x",
    padx=20
)


quote_card = tk.Frame(
    quote_outer,
    bg=PURE_WHITE,
    height=120
)

quote_card.pack(fill="x")


quote_label = tk.Label(
    quote_card,
    text="“Small steps still move you forward. ✦”",
    font=("Arial", 12, "italic"),
    bg=PURE_WHITE,
    fg=TEXT,
    wraplength=300,
    justify="center"
)

quote_label.pack(
    pady=28,
    padx=15
)


# ==========================================
# ✦ NEW QUOTE BUTTON ✦
# ==========================================

quote_button = tk.Button(
    right_panel,
    text="♡ another little quote",
    font=("Arial", 9, "bold"),
    bg=BABY_BLUE,
    fg=TEXT,
    activebackground=BLUE,
    relief="flat",
    bd=0,
    padx=12,
    pady=6,
    cursor="hand2",
    command=change_quote
)

quote_button.pack(pady=12)


# ==========================================
# ✦ KAWAII STICKER AREA ✦
# ==========================================

sticker_title = tk.Label(
    right_panel,
    text="୨୧ little happy corner ୨୧",
    font=("Arial", 11, "bold"),
    bg=LIGHT_LILAC,
    fg=DARK_PURPLE
)

sticker_title.pack(pady=(8, 8))


sticker_row1 = tk.Label(
    right_panel,
    text="☁   ♡   ✦   ☆   ♡   ☁",
    font=("Arial", 22),
    bg=LIGHT_LILAC,
    fg=PURPLE
)

sticker_row1.pack(pady=5)


sticker_row2 = tk.Label(
    right_panel,
    text="૮ ˶ᵔ ᵕ ᵔ˶ ა    ♡    (｡•ᴗ•｡)",
    font=("Arial", 13),
    bg=LIGHT_LILAC,
    fg=SOFT_TEXT
)

sticker_row2.pack(pady=8)


sticker_row3 = tk.Label(
    right_panel,
    text="✧ ୨୧  💿  ୨୧ ✧",
    font=("Arial", 16),
    bg=LIGHT_LILAC,
    fg=PURPLE
)

sticker_row3.pack(pady=5)


# ==========================================
# ✦ MINI MESSAGE ✦
# ==========================================

mini_message = tk.Label(
    right_panel,
    text="☁ take a breath\n♡ you are doing okay\n✦ keep going",
    font=("Arial", 10),
    bg=LIGHT_LILAC,
    fg=SOFT_TEXT,
    justify="center"
)

mini_message.pack(pady=15)


# ==========================================
# ✦ BOTTOM GLITTER ✦
# ==========================================

bottom_glitter = tk.Label(
    window,
    text="✦ ˚₊‧ ✧ ‧₊˚  ♡  ˚₊‧ ✧ ‧₊˚ ✦",
    font=("Arial", 10),
    bg=BG,
    fg=PURPLE
)

bottom_glitter.pack(pady=7)


# ==========================================
# ✦ FOOTER ✦
# ==========================================

footer = tk.Label(
    window,
    text="♡ stay organized • stay gentle with yourself ♡",
    font=("Arial", 9, "italic"),
    bg=BG,
    fg=SOFT_TEXT
)

footer.pack(pady=(0, 4))


small_footer = tk.Label(
    window,
    text="✧ made with Python ✧",
    font=("Arial", 8),
    bg=BG,
    fg="#9B99A9"
)

small_footer.pack(pady=(0, 7))


# ==========================================
# ✦ DISPLAY SAVED TASKS ✦
# ==========================================

display_tasks()


# ==========================================
# ✦ ENTER KEY ✦
# ==========================================

window.bind(
    "<Return>",
    lambda event: add_task()
)


# ==========================================
# ✦ START ✦
# ==========================================

window.mainloop()
