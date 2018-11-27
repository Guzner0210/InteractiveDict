from tkinter import *
from tkinter.ttk import *
import json
import sqlite3
from sqlite3 import Error

root = Tk()
root.geometry("500x300")

#============================
def trans():
    search = entry.get()
    with open('data.json') as f:
        dict = json.load(f)


    def translate(search):
        return dict[search]


    answer = Label(root, text=translate(search)[0])
    answer.grid(row=1, column=1)

    if search in dict.keys():
        db = sqlite3.connect("db.sqlite3")
        cursor = db.cursor()
        cursor.execute(
            '''INSERT INTO new_words(NEW_WORDS)
            VALUES(?)''', (search,)
        )
        db.commit()
        db.close()
    else:
        print("nope")

#============================

label_1 = Label(root, text="Search your word here: ")
label_1.grid(row=0,column=0)

entry = Entry(root)
entry.grid(row=0,column=1)

search_btn = Button(root, text="Search", command=trans)
search_btn.grid(row=0, column=2, padx=10)

label_2 = Label(root, text="Your word's meaning: ")
label_2.grid(row=1, column=0)

root.mainloop()
