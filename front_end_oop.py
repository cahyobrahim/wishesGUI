from tkinter import *
from back_end import Database
from datetime import datetime

database = Database("wishes.db")

class Window(object):

    def __init__(self , window):

        self.window = window

        self.window.wm_title("Wishes")

        l1 = Label(window , text = "Wish")
        l1.grid(row = 0 , column = 0)

        l2 = Label(window , text = "Date")
        l2.grid(row = 0 , column = 1)

        l3 = Label(window , text = "Target")
        l3.grid(row = 0 , column = 2)

        l4 = Label(window , text = "Status")
        l4.grid(row = 0 , column = 3)

        self.wish_text = StringVar()
        self.e1 = Entry(window , textvariable = self.wish_text)
        self.e1.grid(row = 1 , column = 0)

        self.date_text = StringVar()
        self.e2 = Entry(window , textvariable = self.date_text)
        self.e2.grid(row = 1 , column = 1)

        self.target_text = StringVar()
        self.e3 = Entry(window , textvariable = self.target_text)
        self.e3.grid(row = 1 , column = 2)

        self.status_text = StringVar()
        self.e4 = Entry(window , textvariable = self.status_text)
        self.e4.grid(row = 1 , column = 3)

        self.list1 = Listbox(window , height = 8 , width = 55)
        self.list1.grid(row = 2 , column = 0 , rowspan = 6 , columnspan = 3)

        sb1 = Scrollbar(window)
        sb1.grid(row = 2 , column = 3 , rowspan = 6)

        self.list1.configure(yscrollcommand = sb1.set)
        sb1.configure(command = self.list1.yview)

        self.list1.bind('<<ListboxSelect>>' , self.get_selected_row)

        b1 = Button(window , text = "View All" , command = self.view_command)
        b1.grid(row = 8 , column = 0)

        b2 = Button(window , text = "Search" , command = self.search_command)
        b2.grid(row = 8 , column = 1)

        b3 = Button(window , text = "Add" , command = self.add_command)
        b3.grid(row = 8 , column = 2)

        b4 = Button(window , text = "Update" , command = self.update_command)
        b4.grid(row = 8 , column = 3)

        b5 = Button(window , text = "Delete" , command = self.delete_command)
        b5.grid(row = 9 , column = 1 , columnspan = 2)

    def get_selected_row(self , event):
        try:
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.e1.delete(0 , END)
            self.e1.insert(END , self.selected_tuple[1])
            self.e2.delete(0 , END)
            self.e2.insert(END , self.selected_tuple[2])
            self.e3.delete(0 , END)
            self.e3.insert(END , self.selected_tuple[3])
            self.e4.delete(0 , END)
            self.e4.insert(END , self.selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0 , END)
        for row in database.view():
            self.list1.insert(END , row)

    def search_command(self):
        self.list1.delete(0 , END)
        for row in database.search(self.wish_text.get() , self.date_text.get() , self.target_text.get() , self.status_text.get()):
            self.list1.insert(END , row)

    def add_command(self):
        if self.date_text.get() == "":
            database.insert(self.wish_text.get() , datetime.now().strftime("%d/%m/%Y") , self.target_text.get() , self.status_text.get())
            self.list1.delete(0 , END)
            for row in database.view():
                self.list1.insert(END , row)
        else:
            database.insert(self.wish_text.get() , self.date_text.get() , self.target_text.get() , self.status_text.get())
            self.list1.delete(0 , END)
            for row in database.view():
                self.list1.insert(END , row)

    def delete_command(self):
        database.delete(self.selected_tuple[0])

    def update_command(self):
        try:
            database.update(self.selected_tuple[0] , self.wish_text.get() , self.date_text.get() , self.target_text.get() , self.status_text.get())
        except:
            pass

window = Tk()
Window(window)
window.mainloop()    
