from tkinter import *
from tkinter import messagebox as msg 

### EVENT HANDLERS ###
def btn_calculate_clicked():
    n_nights = int(txt_nights.get())
    total = n_nights *  100
    if breakfast_checked.get():
        total += n_nights * 5
    if late_checked.get():
        total += 20

    lbl_payment['text'] = f'Payment: ${total}'

### CREATE WINDOW ###
window = Tk()
window.title('Hello GUI App')
window.geometry('300x200')

### CREATE WIDGETS ###
lbl_title = Label(window, text = 'Room Booking Service')
lbl_title.grid(row=0, column=0, columnspan=3)

lbl_nights = Label(window, text='Nights ($100)')
lbl_nights.grid(row=1, column=0)

txt_nights = Entry(window, width=10)
txt_nights.grid(row=1, column=1, columnspan=2, sticky=W)

lbl_extras = Label(window, text='Extras')
lbl_extras.grid(row=2, column=0)

breakfast_checked = BooleanVar()
chk_breakfast = Checkbutton(window, text='Breakfast ($5)', command=btn_calculate_clicked)
chk_breakfast.grid(row=2, column=1, columnspan=2, sticky=W)

late_checked = BooleanVar()
chk_late = Checkbutton(window, text='Late Checkout ($20)', command=btn_calculate_clicked)
chk_late.grid(row=3, column=1, columnspan=2, sticky=W)

lbl_payment = Label(window, text='Payment: $0')
lbl_payment.grid(row=4, column=0, columnspan=2)

btn_calculate = Button(window, text='Calculate', command=btn_calculate_clicked)
btn_calculate.grid(row=4, column=2)

### START THE GUI ###
window.mainloop()