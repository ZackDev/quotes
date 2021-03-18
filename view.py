__author__ = 'ZackDev'

from tkinter import Label, Frame, StringVar, PhotoImage, Tk
from abc import ABC, abstractmethod


class GridView(Tk):
    def __init__(self, controller):
        super().__init__()
        self.title('Stoic Quotes')
        self.geometry('1100x480')
        self.controller = controller

        self.content = Frame(self)
        self.content.grid(column=0, row=0, columnspan=2, rowspan=2)

        self.quote = StringVar()
        quote_label = Label(self.content, textvariable=self.quote)
        quote_label.config(font=('1942 Report', 32), wraplength=700)
        quote_label.grid(column=1, row=0, sticky='NE', padx=10, pady=10)

        self.author = StringVar()
        auth_label = Label(self.content, textvariable=self.author)
        auth_label.config(font=('Photograph Signature', 44))
        auth_label.grid(column=1, row=1, sticky='SE', padx=10, pady=10)

        self.image_label = Label(self.content)
        self.image_label.grid(column=0, row=0, rowspan=2)
        self.bind("<Button 1>", self.on_window_click)

    def main(self):
        self.controller.get_quote()
        self.mainloop()

    def on_window_click(self, event):
        self.controller.get_quote()

    def update_quote(self, quote):
        self.quote.set(quote)

    def update_author(self, author):
        self.author.set(author)

    def update_image(self, image):
        img = PhotoImage(file=image)
        self.image_label.configure(image=img)
        self.image_label.image = img


class AnotherStoicView:
    pass
