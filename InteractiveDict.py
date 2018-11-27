from tkinter import *
from tkinter.ttk import *
import json
import sqlite3
from difflib import get_close_matches

root = Tk()
root.geometry("500x100")

#============================
def trans():
    search = entry.get()
    with open('data.json') as f:
        dict = json.load(f)


    def translate(search):
        return dict[search]


    if search in dict.keys():
        answer = Label(root, text=translate(search)[0] + "|")
        answer.grid(row=2, column=1, columnspan="2", sticky="w")
        db = sqlite3.connect("db.sqlite3")
        cursor = db.cursor()
        cursor.execute(
            '''INSERT INTO new_words(NEW_WORDS)
            VALUES(?)''', (search,)
        )
        db.commit()
        db.close()
    else:
        close_match = get_close_matches(search, dict.keys())
        suggestion_1 = Button(root, text=close_match[0])
        suggestion_1.grid(row=1, column=0, sticky="w")
        suggestion_2 = Button(root, text=close_match[1])
        suggestion_2.grid(row=1, column=1, sticky="w")
        suggestion_3 = Button(root, text=close_match[2])
        suggestion_3.grid(row=1, column=2, sticky="w")
        # answer = Label(root, text="That word is not in this dictionary, sorry!|")
        # answer.grid(row=1, column=1, sticky="w")

#============================

label_1 = Label(root, text="Search your word here: ")
label_1.grid(row=0,column=0)

entry = Entry(root)
entry.grid(row=0,column=1)

search_btn = Button(root, text="Search", command=trans)
search_btn.grid(row=0, column=2, padx=10)

label_2 = Label(root, text="Your word's meaning: ")
label_2.grid(row=2, column=0)

root.mainloop()
