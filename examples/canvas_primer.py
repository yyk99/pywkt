#!/usr/bin/env python3
# -*- Coding: UTF-8 -*-

# Tkinter documentation
# https://tkdocs.com/index.html
#

from tkinter import *
from tkinter import ttk


class Sketchpad(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.bind("<Button-1>", self.save_posn)
        self.bind("<B1-Motion>", self.add_rectangle)

    def save_posn(self, event):
        self.lastx, self.lasty = event.x, event.y

    def add_rectangle(self, event):
        self.create_rectangle((self.lastx, self.lasty, event.x, event.y))
        #self.save_posn(event)


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

sketch = Sketchpad(root, width=1000, height=600, background='gray75')
sketch.grid(column=0, row=0, sticky=(N, W, E, S))

root.mainloop()
