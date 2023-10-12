from tkinter import *

### EVENT HANDLERS ###
def btn_generate_receipt():
    name = lbl_name.get()
    total = 0
    selected_workshops = []

    if workshop_A.get():
        total += 50
        selected_workshops.append("Workshop A - Python Basics")
    if workshop_B.get():
        total += 100
        selected_workshops.append("Workshop B - Machine Learning")
    if workshop_C.get():
        total += 75
        selected_workshops.append("Workshop C - Web Development")
    if workshop_D.get():
        total += 60
        selected_workshops.append("Workshop D - Data Visualization")

    if name:
        lbl_payment['text'] = f'Total Fee: ${total}'
        lbl_selected_workshops['text'] = '\n'.join(selected_workshops)

### CREATE WINDOW ###

window = Tk()
window.title('Event Registration')
window.geometry('300x250')

### CREATE WIDGETS ###

lbl_title = Label(window, text = 'Event Registration Form')
lbl_title.grid(row=0, column=0)

lbl_name = Entry(window, width=40)
lbl_name.grid(row=1, column=0)

workshop_A = BooleanVar()
chk_workshop_A = Checkbutton(window, text = 'Workshop A - Python Basics ($50)', variable= workshop_A, command = btn_generate_receipt)
chk_workshop_A.grid(row=2, column=0)


workshop_B = BooleanVar()
chk_workshop_B = Checkbutton(window, text= 'Workshop B - Machine Learning ($100)',  command= btn_generate_receipt)
chk_workshop_B.grid(row=3, column=0)

workshop_C = BooleanVar()
chk_workshop_C = Checkbutton(window, text= 'Workshop C - Web Development ($75)',  command= btn_generate_receipt)
chk_workshop_C.grid(row=4, column=0)

workshop_D = BooleanVar()
chk_workshop_D = Checkbutton(window, text= 'Workshop D - Data Visualization ($60) ' ,command= btn_generate_receipt)
chk_workshop_D.grid(row=5, column=0)

lbl_user = Label(window, text='Receipt for')
lbl_user.grid(row=7, column= 0, sticky=W)

btn_calculate = Button(window, text='Generate Receipt', command= btn_generate_receipt)
btn_calculate.grid(row=6, column=0)

lbl_selected_workshops = Label(window, text ='')
lbl_selected_workshops.grid(row=8, column=0, sticky= W)

lbl_payment = Label(window, text='Total Fee: $0')
lbl_payment.grid(row=9, column=0, sticky= W)




### START THE GUI ###

window.mainloop()