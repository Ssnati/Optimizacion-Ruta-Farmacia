import tkinter as tk


class Button:
    def __init__(self, frame, text, width, height, bg="white", fg="black", command=None):
        self.button = tk.Button(frame, text=text, width=width, height=height, bg=bg, fg=fg, command=command)

    def pack(self, side, fill):
        self.button.pack(side=side, fill=fill)

    def grid(self, row, column):
        self.button.grid(row=row, column=column)

    def place(self, x, y):
        self.button.place(x=x, y=y)

    def destroy(self):
        self.button.destroy()

    def config(self, text, width, height, bg, fg, command):
        self.button.config(text=text, width=width, height=height, bg=bg, fg=fg, command=command)

    def get(self):
        return self.button
