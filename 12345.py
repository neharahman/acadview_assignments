from Tkinter import *

import tkMessageBox
#import tkinter.font
import backend
#from PIL import Image, ImageTk


def view():
    listing.delete(0, END)
    for row in backend.view():
        listing.insert(END, row)

def search():
    print("hello")
def add():
    #print("hey")
    backend.insert(title_text.get(),
                    author_text.get(),
                    year_text.get(), 
                    isbn_text.get())
    listing.delete(0, END)
    listing.insert(END, 
                    (title_text.get(), 
                    author_text.get(), 
                    year_text.get(), 
                    isbn_text.get()))
def update():
    print("update")
    
def delete():
    print("hey there")
    
    
r=Tk()
r.geometry("1000x1000")
label1 = Label(r, text = "Title")
label1.grid(row = 0, column = 0)

label2 = Label(r, text = "Author")
label2.grid(row = 1, column = 0)

label3 = Label(r, text = "Year")
label3.grid(row = 2, column = 0)

label4 = Label(r, text = "ISBN")
label4.grid(row = 3, column = 0)

title_text = StringVar()
entry1 = Entry(r, textvariable = title_text)
entry1.grid(row = 0, column = 1)

author_text = StringVar()
entry2 = Entry(r, textvariable = author_text)
entry2.grid(row = 1, column = 1)

year_text = StringVar()
entry3 = Entry(r, textvariable = year_text)
entry3.grid(row = 2, column = 1)

isbn_text = StringVar()
entry4 = Entry(r, textvariable = isbn_text)
entry4.grid(row = 3, column = 1)

listing = Listbox(r, height = 6, width= 100)
listing.grid(row = 7, column = 0, rowspan = 6, columnspan = 2)

scroller = Scrollbar(r)
scroller.grid(row = 7, column = 2, rowspan = 6)
 
listing.configure(yscrollcommand = scroller.set)
scroller.configure(command = listing.yview)

#listing.bind('<<ListboxSelect>>', get_selected_row)


button1 = Button(r, 
                text = "View All", 
                width = 12,command=view)
button1.grid(row = 20, column = 0)

button2 = Button(r, 
                text = "Search Entry", 
                width = 12,command=search)
button2.grid(row = 21, column = 0)

button3 = Button(r, 
                text = "Add Entry", 
                width = 12,command=add)
button3.grid(row = 22, column = 0)

button4 = Button(r, 
                text = "Update Selected", 
                width = 12,command=update)
button4.grid(row = 23, column = 0)

button5 = Button(r,text = "Delete Selected",   width = 12,command=delete )
button5.grid(row = 24, column = 0)

button6 = Button(r, 
                text = "Close", 
                width = 12, 
                command = r.destroy)
button6.grid(row = 25, column = 0)

r.mainloop()