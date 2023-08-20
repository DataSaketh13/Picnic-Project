#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 11:03:47 2023

@author: saketh
"""

from tkinter import *
import random

root=Tk()
root.title("Picnic Bag List")
root.geometry("400x400")

label1 = Label(root)
label2 = Label(root)

listed_items = ['tiffin', 'chocolate', 'cricket bat', 'toy', 'candy', 'car', 'hanky', 'compass']
label1["text"] = "Listed Items:" + str(listed_items)

def Picnic():
    random_list = random.sample(range(0, 8), 1)
    label2["text"] = "Put item no.: " + str(random_list) + "in bag"
    
label1.place(relx=0.5, rely=0.4, anchor=CENTER)

btn=Button(root, text="Which item to put in bag?", command=Picnic, bg="orange", fg="white")
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

label2.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()




