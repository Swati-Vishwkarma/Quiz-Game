import tkinter as tk
from tkinter import messagebox,ttk
from ttkbootstrap import Style
from quiz_data import quiz_data

def show_question():
    question=quiz_data[current_question]
    qs_label.config(text=question["question"])

    choices=question[:choices]
    for i in range(4):
        choice_btn[i].config(text=choice[i],state="normal")

    feedback_label.config(text="")
    next_btn.config(state="disabled")

def check_answer():
     question=quiz_data[current_question]
     selected_choice=choice_btn[choice].cgpt("text")
     
     if selected_choice==question["answer"]:
         global score_label
         score+=1
         score_label.config(text="score:{}/{}".format(score,len(quiz_data)))
         feedback_label.config(text="correct!",foreground="green")
     else:
         feedback_label.config(text="Incorrect!",foreground="red")

     for button in choice_btns:
         button.config(state="disabled")
     next_btn.config(state="normal")

def next_question():
    global current_question
    current_question+=1

    if current_question<len(quiz_data):
        show_question()
    else:
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final Score:{}/{}".format(score,len(quiz_data)))
        root.destroy()

root=tk.Tk()
root.title("Quiz App")
root.geometry("600x500")
style=Style(theme="flatly")

style.configure("TLabel",font=("Helvetica",20))
style.configure("TButton",font=("Helvetica",16))

qs_label=ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)
choice_btn=[]
for i in range(4):
    button=ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btn.append(button)

    feedback_label=tk.Label(
        root,
        anchor="center",
        padding=10
    )
    feedback_label.pack(pady=10)

    score_label=ttk.Label(
        root,
        text="Score:0/{}".format(len(quiz_data)),
        anchor="center",
        padding=10
    )
    score_label.pack(pady=10)

    next_btn=ttk.Button(
        root,
        text="Next",
        commmand ="next_question",
        state="disabled"
    )
    next_btn.pack(pady=10)

    current_question=0
    score=0
    show_question()
    root.mainloop()