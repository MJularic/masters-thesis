import tkinter as tk
from tkinter import filedialog
from tkinter import *
from get_statistic import GetStatistic
from tkinter import messagebox
from tkinter import ttk


class TrainFlow:

    def __init__(self, root):
        self.root = root
        self.db_entry_var = StringVar()
        self.txt_entry_var = StringVar()
        self.num_gram = IntVar()
        self.num_gram.set(1)
        self.progress_var = DoubleVar()
        self.progress_var.set(0)
        self.progress_bar = None
        self.display = None

    def start(self):
        self.display = tk.Toplevel(self.root)
        self.display.geometry("500x400")
        self.display.resizable(False, False)

        db_entry = Entry(self.display, text=self.db_entry_var, width=30)
        choose_db_button = tk.Button(self.display, text="Choose DB file", command=self.choose_db_file)
        db_entry.pack(pady=5)
        choose_db_button.pack(pady=5)

        txt_entry = Entry(self.display, text=self.txt_entry_var, width=30)
        choose_txt_button = tk.Button(self.display, text="Choose password txt file", command=self.choose_txt_file)
        txt_entry.pack(pady=5)
        choose_txt_button.pack(pady=5)

        unigram_radio = Radiobutton(self.display, text="1-gram", variable=self.num_gram, value=1)
        bigram_radio = Radiobutton(self.display, text="2-gram", variable=self.num_gram, value=2)
        trigram_radio = Radiobutton(self.display, text="3-gram", variable=self.num_gram, value=3)

        unigram_radio.pack()
        bigram_radio.pack()
        trigram_radio.pack()
        train_generator_button = Button(self.display, text="Train generator")
        train_generator_button.pack(side=tk.RIGHT, padx=15)
        train_meter_button = Button(self.display, text="Train meter", command=self.train_meter)
        train_meter_button.pack(side=tk.LEFT, padx=15)

        self.progress_bar = ttk.Progressbar(self.display, variable=self.progress_var,orient='horizontal', maximum=100, length=500)
        self.progress_bar.pack(side=tk.BOTTOM, pady=10)

        text_label = Label(self.display, text= "PROGRESS BAR")
        text_label.pack(side=tk.BOTTOM, pady=10)

    def choose_db_file(self):
        self.display.filename = filedialog.askopenfilename(initialdir="/home", title="Select sqlite3 db file",
                                                        filetypes=[("Sqlite3 db", "*.db")])
        self.db_entry_var.set(self.display.filename)

    def choose_txt_file(self):
        self.display.filename = filedialog.askopenfilename(initialdir="/home",
                                                        title="Select password file",
                                                        filetypes=[("Text file", "*.txt")])
        self.txt_entry_var.set(self.display.filename)

    def train_meter(self):
        db_path = self.db_entry_var.get()
        txt_path = self.txt_entry_var.get()
        num_gram = self.num_gram.get()

        gs = GetStatistic(txt_path, db_path)

        gs.create_statistic(num_gram, self.progress_var, self.progress_bar)

        messagebox.showinfo("Info", "Training is done!")
        self.progress_var.set(0)
