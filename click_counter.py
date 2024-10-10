import tkinter as tk

class ClickCounter:
    def __init__(self, master):
        self.master = master
        self.master.title("Click Counter")

        self.count = 0
        self.label = tk.Label(master, text="Count: 0", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.button = tk.Button(master, text="Click me!", command=self.increment_count, font=("Helvetica", 16))
        self.button.pack(pady=20)

    def increment_count(self):
        self.count += 1
        self.label.config(text=f"Count: {self.count}")

if __name__ == "__main__":
    root = tk.Tk()
    click_counter = ClickCounter(root)
    root.mainloop()
