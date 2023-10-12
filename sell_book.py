from tkinter import *
from tkinter import messagebox as msg
from tkinter.ttk import Combobox
from tkinter import Listbox
from books import load_book, load_name


books = load_book()
names = load_name(books)

### EVENT HANDLERS ###
def btn_cancel_clicked():
    txt_name.delete(0, END)
    txt_author.delete(0, END)
    txt_price.delete(0, END)
    txt_number.delete(0, END)

def lst_book_selected(event):
    # get book name from listbox
    book = lst_books.get(lst_books.curselection())
    # set book info from the dictionary
    txt_name.delete(0, END) # clear current text
    txt_name.insert(0, book) # insert new text (name of book)
    txt_author.delete(0, END)
    txt_author.insert(0, books[book][0])
    txt_price.delete(0, END)
    txt_price.insert(0, books[book][1])

def btn_ok_clicked():
    price = float(txt_price.get())
    quantity = int(txt_number.get())
    deliver_index = cbb_delivery.current()
    total = price * quantity

    if deliver_index == 0:
        total +=1
    elif deliver_index == 1:
        total +=2
    else:
        total += 3
    if cover_choice.get() == True:
        total += 2
    
    msg.showinfo('Total', f'Total: ${total}')
### CREATE WINDOW ###
window =  Tk()
window.title('Books Store')
window.geometry('500x300')

### CREATE WIDGETS ###

lbl_books = Label(window, text='Books')
lbl_books.grid(row=0, column=0, sticky=W)

lst_books = Listbox(window, height =5, selectmode=SINGLE)
lst_books.grid(row=1, column=0, rowspan=3, columnspan=2, sticky=W, padx=10)
for name in names:
    lst_books.insert(END, name)
lst_books.bind('<<ListboxSelect>>', lst_book_selected)

lbl_name = Label(window, text='Name')
lbl_name.grid(row=1, column=3, sticky=W)

txt_name = Entry(window, width=20)
txt_name.grid(row=1, column=4, columnspan=2, sticky=W)

lbl_author = Label(window, text ='Author')
lbl_author.grid(row=2, column=3, sticky=W)

txt_author = Entry(window, width=20)
txt_author.grid(row=2, column=4, columnspan=2, sticky=W)

lbl_price = Label(window, text='Price')
lbl_price.grid(row=3, column=3, sticky=W)

txt_price = Entry(window, width=20)
txt_price.grid(row=3, column=4, columnspan=2, sticky=W)

lbl_number = Label(window, text = 'Number')
lbl_number.grid(row=4, column=0,sticky=W, padx=10)

txt_number = Entry(window,width=15)
txt_number.grid(row=4, column=1, sticky=W)

lbl_delivery = Label(window, text= 'Deliver')
lbl_delivery.grid(row=5, column=0,sticky=W, padx=10)

cbb_delivery = Combobox(window, width=15)
cbb_delivery['value'] = ('Standard ($1)','Fast ($2)','Express ($5)')
cbb_delivery.grid(row=5, column=1,sticky=W)

lbl_cover = Label(window, text='Cover ($2)')
lbl_cover.grid(row=5, column=3, sticky=W)

cover_choice = IntVar()
rd_option1 = Radiobutton(window, text='Yes', value=1, variable=cover_choice)
rd_option1.grid(row=5, column=4, sticky=W)

rd_option2 = Radiobutton(window, text= 'No', value=2, variable=cover_choice)
rd_option2.grid(row=5, column=5,sticky=W)

btt_ok = Button(window, text='OK', width=5, command = btn_ok_clicked)
btt_ok.grid(row=6, column=4, sticky=W)

btn_cancel = Button(window, text='Cancel', width=5, command = btn_cancel_clicked)
btn_cancel.grid(row=5, column=6, sticky=W)

### START THE GUI ###
window.mainloop()
