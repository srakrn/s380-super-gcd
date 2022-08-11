import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.greeting = tk.Label(text="Super GCD application!", font=("Arial", 16))

        self.frame = tk.Frame(self.parent)

        self.label_inp_1 = tk.Label(master=self.frame, text="Number 1:")
        self.entry_inp_1 = tk.Entry(master=self.frame, width=20)
        self.label_inp_1.grid(row=0, column=0)
        self.entry_inp_1.grid(row=0, column=1)


        self.label_inp_2 = tk.Label(master=self.frame, text="Number 2:")
        self.entry_inp_2 = tk.Entry(master=self.frame, width=20)
        self.label_inp_2.grid(row=1, column=0)
        self.entry_inp_2.grid(row=1, column=1)

        self.spacer = tk.Label(master=self.frame, text="")
        self.spacer.grid(row=3, column=0)

        self.btn_submit = tk.Button(master=self.frame, text="GCD \N{RIGHTWARDS BLACK ARROW}", command=self.gcd_button)
        self.label_result = tk.Label(master=self.frame, text="")
        self.btn_submit.grid(row=4, column=0, sticky="nesw")
        self.label_result.grid(row=4, column=1, sticky="nesw")

        self.greeting.pack()
        self.frame.pack()
    
    def gcd_button(self):
        print("GCD button pressed!")

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()