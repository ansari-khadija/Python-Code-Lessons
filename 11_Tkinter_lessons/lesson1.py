
import tkinter as tk
from tkinter import messagebox
import random



BG = "#0F172A"          # Slate Black
CYAN = "#06B6D4"        # Cyber Cyan
FUCHSIA = "#D946EF"     # Neon Fuchsia
IVORY = "#FFFFF0"       # Ivory
GRAY = "#94A3B8"        # Slate Gray
GREEN = "#22C55E"
RED = "#EF4444"
DARK = "#020617"




questions = [
    {
        "question": "What is the correct way to create a variable?",
        "options": [
            "x = 10",
            "int x = 10",
            "var x = 10",
            "x := 10"
        ],
        "answer": "x = 10"
    },

    {
        "question": "What does len() do?",
        "options": [
            "Deletes an item",
            "Counts items",
            "Adds numbers",
            "Sorts a list"
        ],
        "answer": "Counts items"
    },

    {
        "question": "Which symbol is used for a comment?",
        "options": [
            "//",
            "/*",
            "#",
            "<!--"
        ],
        "answer": "#"
    },

    {
        "question": "What is the output of: print(5 + 3)?",
        "options": [
            "53",
            "8",
            "2",
            "15"
        ],
        "answer": "8"
    },

    {
        "question": "Which keyword is used to create a function?",
        "options": [
            "function",
            "func",
            "define",
            "def"
        ],
        "answer": "def"
    }
]



player_name = ""
course_name = ""
subject_name = ""

current_question = 0
score = 0
xp = 0
coins = 0
lives = 3




window = tk.Tk()

window.title("Python Learning Adventure")
window.geometry("700x600")
window.configure(bg=BG)





def clear_screen():
    for widget in window.winfo_children():
        widget.destroy()




def start_page():

    clear_screen()

    heading = tk.Label(
        window,
        text="🐍 PYTHON LEARNING ADVENTURE",
        font=("Arial", 24, "bold"),
        fg=CYAN,
        bg=BG
    )

    heading.pack(pady=(40, 10))


    subtitle = tk.Label(
        window,
        text="Learn Python • Complete Challenges • Level Up!",
        font=("Arial", 12),
        fg=GRAY,
        bg=BG
    )

    subtitle.pack(pady=(0, 35))


    # Player name

    name_label = tk.Label(
        window,
        text="👤 Player Name",
        font=("Arial", 12, "bold"),
        fg=IVORY,
        bg=BG
    )

    name_label.pack()

    global name_entry

    name_entry = tk.Entry(
        window,
        font=("Arial", 13),
        width=32,
        bg=IVORY,
        fg=DARK
    )

    name_entry.pack(pady=(5, 20))


    # Course

    course_label = tk.Label(
        window,
        text="📚 Course",
        font=("Arial", 12, "bold"),
        fg=IVORY,
        bg=BG
    )

    course_label.pack()

    global course_entry

    course_entry = tk.Entry(
        window,
        font=("Arial", 13),
        width=32,
        bg=IVORY,
        fg=DARK
    )

    course_entry.pack(pady=(5, 20))


    # Subject

    subject_label = tk.Label(
        window,
        text="🧠 Subject",
        font=("Arial", 12, "bold"),
        fg=IVORY,
        bg=BG
    )

    subject_label.pack()

    global subject_entry

    subject_entry = tk.Entry(
        window,
        font=("Arial", 13),
        width=32,
        bg=IVORY,
        fg=DARK
    )

    subject_entry.pack(pady=(5, 35))


    # Start button

    start_button = tk.Button(
        window,
        text="▶ START ADVENTURE",
        font=("Arial", 13, "bold"),
        fg=IVORY,
        bg=FUCHSIA,
        activebackground=CYAN,
        activeforeground=BG,
        padx=30,
        pady=12,
        relief="flat",
        cursor="hand2",
        command=start_game
    )

    start_button.pack()




def start_game():

    global player_name
    global course_name
    global subject_name
    global current_question
    global score
    global xp
    global coins
    global lives

    player_name = name_entry.get().strip()
    course_name = course_entry.get().strip()
    subject_name = subject_entry.get().strip()

    if not player_name or not course_name or not subject_name:
        messagebox.showwarning(
            "Missing Information",
            "Please enter your name, course and subject."
        )
        return

    current_question = 0
    score = 0
    xp = 0
    coins = 0
    lives = 3

    show_question()




def show_question():

    clear_screen()

    if current_question >= len(questions):
        finish_game()
        return


    question_data = questions[current_question]


    # Header

    header = tk.Frame(
        window,
        bg=BG
    )

    header.pack(fill="x", padx=30, pady=(25, 10))


    player_label = tk.Label(
        header,
        text=f"👤 {player_name.title()}",
        font=("Arial", 12, "bold"),
        fg=IVORY,
        bg=BG
    )

    player_label.pack(side="left")


    stats_label = tk.Label(
        header,
        text=f"⭐ XP: {xp}    🪙 Coins: {coins}    ❤️ {lives}",
        font=("Arial", 12, "bold"),
        fg=CYAN,
        bg=BG
    )

    stats_label.pack(side="right")


    # Progress

    progress_text = tk.Label(
        window,
        text=f"Challenge {current_question + 1} / {len(questions)}",
        font=("Arial", 11),
        fg=GRAY,
        bg=BG
    )

    progress_text.pack(pady=(20, 10))


    # Question

    question_label = tk.Label(
        window,
        text=question_data["question"],
        font=("Arial", 18, "bold"),
        fg=IVORY,
        bg=BG,
        wraplength=600,
        justify="center"
    )

    question_label.pack(pady=20)


    # Answer buttons

    global answer_buttons

    answer_buttons = []


    for option in question_data["options"]:

        button = tk.Button(
            window,
            text=option,
            font=("Arial", 12, "bold"),
            width=35,
            fg=IVORY,
            bg=DARK,
            activebackground=CYAN,
            activeforeground=BG,
            relief="solid",
            borderwidth=1,
            cursor="hand2",
            pady=8,
            command=lambda answer=option: check_answer(answer)
        )

        button.pack(pady=5)

        answer_buttons.append(button)




def check_answer(selected_answer):

    global current_question
    global score
    global xp
    global coins
    global lives


    correct_answer = questions[current_question]["answer"]


    # Disable buttons

    for button in answer_buttons:
        button.config(state="disabled")


    if selected_answer == correct_answer:

        score += 1
        xp += 50
        coins += 10

        feedback = tk.Label(
            window,
            text="✅ Correct! +50 XP  +10 Coins",
            font=("Arial", 14, "bold"),
            fg=GREEN,
            bg=BG
        )

        feedback.pack(pady=15)


    else:

        lives -= 1

        feedback = tk.Label(
            window,
            text=f"❌ Wrong! Correct answer: {correct_answer}",
            font=("Arial", 14, "bold"),
            fg=RED,
            bg=BG
        )

        feedback.pack(pady=15)


        if lives <= 0:

            messagebox.showinfo(
                "Game Over",
                f"You ran out of lives!\n\n"
                f"Score: {score}/{len(questions)}\n"
                f"XP: {xp}\n"
                f"Coins: {coins}"
            )

            finish_game()
            return


    next_button = tk.Button(
        window,
        text="⏭ NEXT CHALLENGE",
        font=("Arial", 12, "bold"),
        fg=BG,
        bg=CYAN,
        activebackground=FUCHSIA,
        activeforeground=IVORY,
        padx=25,
        pady=10,
        relief="flat",
        cursor="hand2",
        command=next_question
    )

    next_button.pack(pady=10)




def next_question():

    global current_question

    current_question += 1

    show_question()



def finish_game():

    clear_screen()


    heading = tk.Label(
        window,
        text="🏆 ADVENTURE COMPLETE!",
        font=("Arial", 25, "bold"),
        fg=CYAN,
        bg=BG
    )

    heading.pack(pady=(60, 30))


    welcome = tk.Label(
        window,
        text=f"Great job, {player_name.title()}!",
        font=("Arial", 18, "bold"),
        fg=IVORY,
        bg=BG
    )

    welcome.pack(pady=10)


    result = tk.Label(
        window,
        text=(
            f"📚 Course: {course_name.title()}\n"
            f"🧠 Subject: {subject_name.title()}\n\n"
            f"🎯 Score: {score}/{len(questions)}\n"
            f"⭐ XP Earned: {xp}\n"
            f"🪙 Coins Earned: {coins}"
        ),
        font=("Arial", 14),
        fg=GRAY,
        bg=BG,
        justify="center"
    )

    result.pack(pady=20)


    if score == len(questions):

        message = "👑 PERFECT! Python Master!"

    elif score >= 3:

        message = "🔥 Excellent work! Keep learning!"

    else:

        message = "💪 Good attempt! Practice makes perfect!"


    message_label = tk.Label(
        window,
        text=message,
        font=("Arial", 15, "bold"),
        fg=FUCHSIA,
        bg=BG
    )

    message_label.pack(pady=15)


    play_again = tk.Button(
        window,
        text="🔄 PLAY AGAIN",
        font=("Arial", 13, "bold"),
        fg=IVORY,
        bg=FUCHSIA,
        activebackground=CYAN,
        activeforeground=BG,
        padx=30,
        pady=10,
        relief="flat",
        cursor="hand2",
        command=start_page
    )

    play_again.pack(pady=20)


    exit_button = tk.Button(
        window,
        text="❌ EXIT",
        font=("Arial", 11, "bold"),
        fg=IVORY,
        bg=RED,
        activebackground=FUCHSIA,
        relief="flat",
        cursor="hand2",
        command=window.destroy
    )

    exit_button.pack()


start_page()

window.mainloop()
