import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")  # Set background color

        self.tasks = []

        # Entry for adding tasks
        self.task_entry = tk.Entry(self.root, width=50, font=("Arial", 12), bd=2)
        self.task_entry.pack(pady=20)

        # Add Task button
        add_task_button = tk.Button(self.root, text="Add Task", width=48, font=("Arial", 12, "bold"), bg="#4caf50", fg="#ffffff", command=self.add_task)
        add_task_button.pack(pady=5)

        # Task Listbox
        self.task_listbox = tk.Listbox(self.root, width=50, height=15, font=("Arial", 12), bd=2)
        self.task_listbox.pack(pady=10)

        # Delete Task button
        delete_task_button = tk.Button(self.root, text="Delete Task", width=48, font=("Arial", 12, "bold"), bg="#f44336", fg="#ffffff", command=self.delete_task)
        delete_task_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index]
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
