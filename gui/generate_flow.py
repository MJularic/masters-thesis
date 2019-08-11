import tkinter as tk
from tkinter import *
from tkinter import messagebox
from alphanumeric_markov import AlphanumericMarkov
from word_markov import WordMarkov


class GenerateFlow:

    def __init__(self, root):
        self.root = root
        self.password_len_entry_var = StringVar()
        self.display = None

        self.alpha_or_word = IntVar()
        self.alpha_or_word.set(1)

    def start(self):
        self.display = tk.Toplevel(self.root)
        self.display.geometry("400x300")
        self.display.resizable(False, False)

        length_label = Label(self.display, text="Password length", width=30)
        length_label.pack(pady=5)
        password_length_entry = Entry(self.display, text=self.password_len_entry_var, width=20)
        password_length_entry.pack(pady=5)

        method_label = Label(self.display, text="Choose method", width=30)
        method_label.pack(pady=5)

        word_radio = Radiobutton(self.display, text="Words", variable=self.alpha_or_word, value=1)
        alpha_radio = Radiobutton(self.display, text="Alphanumeric", variable=self.alpha_or_word, value=2)

        word_radio.pack()
        alpha_radio.pack()

        generate_button = Button(self.display, text="Generate password", command=self.generate)
        generate_button.pack(pady=10)

    def generate(self):

        method = self.alpha_or_word.get()
        length = int(self.password_len_entry_var.get())

        if method == 1:
            wm = WordMarkov("/home/mj/diplomski-rad/database/word.db")
            password = wm.generate_password(length)
            messagebox.showinfo("Generated password", "Password: " + password)
            return

        if method == 2:
            am = AlphanumericMarkov()
            password = am.generate_password(length)
            messagebox.showinfo("Generated password", "Password: " + password)
            return


