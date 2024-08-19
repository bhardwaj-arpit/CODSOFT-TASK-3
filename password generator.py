import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Please enter a positive number.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a number.")
        return

    password = generate_password(length)
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)
    listbox_history.insert(tk.END, password)

def create_gui():
    root = tk.Tk()
    root.title("Password Generator")

    # Password length input
    tk.Label(root, text="Password Length:").pack(pady=5)
    global entry_length
    entry_length = tk.Entry(root)
    entry_length.pack(pady=5)

    # Generate button
    tk.Button(root, text="Generate Password", command=on_generate).pack(pady=10)

    # Generated password display
    tk.Label(root, text="Generated Password:").pack(pady=5)
    global entry_password
    entry_password = tk.Entry(root, width=30)
    entry_password.pack(pady=5)

    # Password history
    tk.Label(root, text="Password History:").pack(pady=5)
    global listbox_history
    listbox_history = tk.Listbox(root, width=30, height=10)
    listbox_history.pack(pady=5)

    # Exit button
    tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
