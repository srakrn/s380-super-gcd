import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        greeting = tk.Label(text="Super GCD application!", font=("Arial", 16))

        frame = tk.Frame(self.parent)

        label_inp_1 = tk.Label(master=frame, text="Number 1:")
        entry_inp_1 = tk.Entry(master=frame, width=20)
        label_inp_1.grid(row=0, column=0)
        entry_inp_1.grid(row=0, column=1)


        label_inp_2 = tk.Label(master=frame, text="Number 2:")
        entry_inp_2 = tk.Entry(master=frame, width=20)
        label_inp_2.grid(row=1, column=0)
        entry_inp_2.grid(row=1, column=1)

        spacer = tk.Label(master=frame, text="")
        spacer.grid(row=3, column=0)

        btn_submit = tk.Button(master=frame, text="GCD \N{RIGHTWARDS BLACK ARROW}")
        label_result = tk.Label(master=frame, text="")
        btn_submit.grid(row=4, column=0, sticky="nesw")
        label_result.grid(row=4, column=1, sticky="nesw")

        greeting.pack()
        frame.pack()

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()