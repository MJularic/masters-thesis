import tkinter as tk
from gui.train_flow import TrainFlow


def train_button_click():
    tf = TrainFlow(root)
    tf.start()


root = tk.Tk()

root.title("Master's deegre project")
root.geometry('500x245')

root.update()

root.resizable(False, False)

buttons_frame = tk.Frame(root, height="250", width="250", background="blue")
buttons_frame.pack(side=tk.LEFT)

text_frame = tk.Frame(root, width="250", height="250", background="green")
text_frame.pack()

train_button = tk.Button(buttons_frame, text="Train", width=30, height=4, command=train_button_click)
test_pass_button = tk.Button(buttons_frame, text="Test password", width=30, height=4)
generate_pass_button = tk.Button(buttons_frame, text="Generate password", width=30, height=4)

text = tk.Label(text_frame, text="Generate, store\n and classify passwords! \n\n"
                                 "Master's deegree\n project by Matej Jularić."
                                 "\n\nMentor: Željko Ilić"
                                 "\n\nCreated using python3, tkinter,"
                                 "\nsqlite3 and nltk."
                                 "\n\nFER, Zagreb 2019.")
text.grid(sticky=tk.NW)


train_button.grid(row=0, column=0)
test_pass_button.grid(row=1, column=0)
generate_pass_button.grid(row=2, column=0)

root.mainloop()
