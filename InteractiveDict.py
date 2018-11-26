from tkinter import *
from tkinter.ttk import *
import json

root = Tk()
root.geometry("500x300")

#============================
def retur():
    search = entry.get()
    with open('data.json') as f:
        dict = json.load(f)


    def translate(search):
        return dict[search]


    answer = Label(root, text=translate(search)[0], width=40)
    answer.columnconfigure(0, pad=0)
    answer.grid(row=1, column=0)
    # print(translate(search))

#============================

guide_1 = Label(root, text="Search you word here: ")
guide_1.grid(row=0,column=0)

entry = Entry(root)
entry.grid(row=0,column=1)

search_btn = Button(root, text="Search", command=retur)
search_btn.grid(row=0, column=2, padx=10)


root.mainloop()
