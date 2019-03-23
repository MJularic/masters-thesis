import tkinter as tk
from tkinter import *
from been_pwned import BeenPwned
from calculate_probability import CalculateProbability
from tkinter import messagebox


class TestFlow():

    def __init__(self, root):
        self.root = root
        self.username_entry_var = StringVar()
        self.password_entry_var = StringVar()
        self.display = None

    def start(self):
        self.display = tk.Toplevel(self.root)
        self.display.geometry("400x300")
        self.display.resizable(False, False)

        username_label = Label(self.display, text="Username", width=30)
        username_label.pack(pady=10)
        username_entry = Entry(self.display, text=self.username_entry_var, width=30)
        username_entry.pack(pady=10)

        password_label = Label(self.display, text="Password", width=30)
        password_label.pack(pady=10)
        password_entry = Entry(self.display, text=self.password_entry_var, width=30, show="*")
        password_entry.pack(pady=10)

        test_button = Button(self.display, text="Test password", command=self.test_password)
        test_button.pack(pady=10)

    def test_password(self):

        username = self.username_entry_var.get()
        password = self.password_entry_var.get()

        if username in password:
            messagebox.showwarning("Change password", "Username contained in password! Change password!")
            return

        bp = BeenPwned(password)
        number_of_occurences = bp.is_pwned()

        if number_of_occurences > 0:
            messagebox.showwarning("Change password", "Your password has been mentioned in the haveibeenpwned database "
                                + str(number_of_occurences) + " times! Change password!")

            return

        cp = CalculateProbability("/home/mj/diplomski-rad/database/n-gram.db")
        score = cp.calculate_probability(password)

        if score < 60:
            messagebox.showinfo("Password strength!", "Weak password!")
            return
        if score > 60 and score < 80:
            messagebox.showinfo("Password strength!", "Medium password!")
            return
        if score > 80:
            messagebox.showinfo("Password strength!", "Strong password!")
            return
