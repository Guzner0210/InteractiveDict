# import os
# from difflib import get_close_matches
# import json
# import sys
#
# with open('data.json') as f:
#     dict = json.load(f)
#
#
# def translate(search):
#     if type(dict[search]) == list:
#         for i in dict[search]:
#             print("The word " + search + " means: " + i)
#     elif type(dict[search]) == str:
#         print("The word " + search + " means: " + dict[search])
#     else:
#         print("There's an error!")
#         # more work on this section is on the way...
#
#
# if __name__ == "__main__":
#
#     while True:
#         search = input("What word are you looking for? ")
#         translate(search)
#         yon = input("Do you want to look for other words as well? [Yn] ")
#         if yon.lower() == "y" or yon.lower() == "yes":
#             continue
#         elif yon.lower() == "n" or yon.lower() == "no":
#             break
#         else:
#             print("Sorry, I don't understand what you want.")
#             break
#
#     sys.exit()

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
