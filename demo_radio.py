from tkinter import *
from tkinter import messagebox as msg
question = [['What is the capital of France?', 'Paris', 'London', 'Berlin', 'Madrid', 1],
            ['What is the capital of Germany?', 'Paris', 'London', 'Berlin', 'Madrid', 3],
            ['What is the capital of Spain?', 'Paris', 'London', 'Berlin', 'Madrid', 4],
            ['What is the capital of England?', 'Paris', 'London', 'Berlin', 'Madrid', 2]]

curr_question = 0 

def load_question(question_index):
    lbl_quiz['text'] = question[question_index][0]
    rd_option1['text'] = question[question_index][1]
    rd_option2['text'] = question[question_index][2]
    rd_option3['text'] = question[question_index][3]
    rd_option4['text'] = question[question_index][4]
    

### EVENT HANDLERS ###
def btn_answer_clicked():   
    global curr_question
    if curr_question > len(question):
        msg.showinfo('No More Question')
        return
    correct_answer = question[curr_question][5]
    if correct_answer == answer_choice.get():
        msg.showinfo("Quiz", "Correct Answer!")
    else:
        msg.showerror("Quiz", "Wrong Answer!")

    curr_question += 1
    load_question(curr_question)

### CREATE WINDOW & WIDGETS ###

window = Tk()
window.title('Radio Demo')
window.geometry("300x200")

lbl_quiz = Label(window, text='Ai la nguoi ngu nhat vietnam?')
lbl_quiz.grid(row=0, column=0, columnspan=2)

answer_choice = IntVar()
rd_option1 = Radiobutton(window, text='Tung Doan', value=1, variable=answer_choice)
rd_option1.grid(row=1, column=1, sticky=W)

rd_option2 = Radiobutton(window, text='Quang Tung Phu Lo', value=2, variable=answer_choice)
rd_option2.grid(row=2, column=1, sticky=W)

rd_option3 = Radiobutton(window, text='Doan Quang Tung', value=3,variable=answer_choice)
rd_option3.grid(row=3,column=1, sticky=W)

rd_option4 = Radiobutton(window, text='Cau Doanh', value=4, variable=answer_choice)
rd_option4.grid(row=4, column=1, sticky=W)

btn_answer = Button(window, text='Answer', command= btn_answer_clicked)
btn_answer.grid(row=5, column=0, sticky=W)

### START THE GUI ###

window.mainloop()