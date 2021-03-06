import tkinter as tk
from tkinter import ttk
#from tkinter import PhotoImage
import sys
from datetime import datetime as dt

class GUI:
    def __init__(self, master):
        self.master = master
        self.test_button = tk.Button(self.master, command=self.tb_click)
        self.test_button.configure(
            text="Start", background="Grey",
            padx=50
            )
        self.test_button.pack(side=tk.TOP)

    def progress(self):
        self.prog_bar = ttk.Progressbar(
            self.master, orient="horizontal",
            length=200, mode="indeterminate"
            )
        self.prog_bar.pack(side=tk.TOP)

    def tb_click(self):
        self.progress()
        self.prog_bar.start()
        # Simulate long running process
        t = threading.Thread(target=time.sleep, args=(5,))
        t.start()
        t.join()
        self.prog_bar.stop()

root = tk.Tk()
root.title("Test Button")
main_ui = GUI(root)
root.mainloop()
