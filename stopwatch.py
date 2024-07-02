import tkinter as tk

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("500x200")
        self.root.resizable(False, False)

        self.root.configure(bg="#f0f0f0")  # Set background color

        self.counter = 0
        self.running = False

        self.label = tk.Label(self.root, text="00:00:00", font=("Arial", 36), bg="#ffffff", fg="#333333", width=10)
        self.label.pack(pady=20)

        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack()

        self.start_button = tk.Button(button_frame, text="Start", width=10, font=("Arial", 12, "bold"), bg="#4caf50", fg="#ffffff", command=self.start_stopwatch)
        self.start_button.grid(row=0, column=0, padx=10, pady=10)

        self.stop_button = tk.Button(button_frame, text="Stop", width=10, font=("Arial", 12, "bold"), bg="#f44336", fg="#ffffff", state=tk.DISABLED, command=self.stop_stopwatch)
        self.stop_button.grid(row=0, column=1, padx=10, pady=10)

        self.reset_button = tk.Button(button_frame, text="Reset", width=10, font=("Arial", 12, "bold"), bg="#2196f3", fg="#ffffff", command=self.reset_stopwatch)
        self.reset_button.grid(row=0, column=2, padx=10, pady=10)

    def start_stopwatch(self):
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.NORMAL)
        self.update_counter()

    def stop_stopwatch(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def reset_stopwatch(self):
        self.running = False
        self.counter = 0
        self.label.config(text="00:00:00")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def update_counter(self):
        if self.running:
            hours = self.counter // 3600
            minutes = (self.counter // 60) % 60
            seconds = self.counter % 60
            time_string = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
            self.label.config(text=time_string)
            self.counter += 1
            self.root.after(1000, self.update_counter)

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
