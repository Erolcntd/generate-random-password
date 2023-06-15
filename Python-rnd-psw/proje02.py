import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    numbers = entry_numbers.get()
    letters = entry_letters.get()
    punctuation = entry_punctuation.get()

    invalid_chars = []
    for char in numbers:
        if char.isalpha() or char in punctuation:
            invalid_chars.append(char)
    for char in letters:
        if char.isdigit() or char in punctuation:
            invalid_chars.append(char)
    for char in punctuation:
        if char.isalpha() or char.isdigit():
            invalid_chars.append(char)

    if invalid_chars:
        messagebox.showerror("Error", "Invalid characters: {}".format(', '.join(invalid_chars)))
        return
    
    combined = numbers + letters + punctuation
    shuffled = random.sample(combined, len(combined))
    password = ''.join(shuffled)
    listbox_passwords.insert(tk.END, password)

window = tk.Tk()
window.title("Password Generator")
window.configure(bg="white")

frame = tk.Frame(window, bg="white")
frame.pack(pady=20)

label_numbers = tk.Label(frame, text="Numbers:", font=("Helvetica", 12), bg="white")
label_numbers.grid(row=0, column=0, sticky="w")
entry_numbers = tk.Entry(frame, font=("Helvetica", 12))
entry_numbers.grid(row=0, column=1)

label_letters = tk.Label(frame, text="Letters:", font=("Helvetica", 12), bg="white")
label_letters.grid(row=1, column=0, sticky="w")
entry_letters = tk.Entry(frame, font=("Helvetica", 12))
entry_letters.grid(row=1, column=1)

label_punctuation = tk.Label(frame, text="Punctuation:", font=("Helvetica", 12), bg="white")
label_punctuation.grid(row=2, column=0, sticky="w")
entry_punctuation = tk.Entry(frame, font=("Helvetica", 12))
entry_punctuation.grid(row=2, column=1)

button_generate = tk.Button(window, text="Generate Password", command=generate_password, font=("Helvetica", 14), bg="gray", fg="white", activebackground="black", activeforeground="white")
button_generate.pack(pady=10)

listbox_passwords = tk.Listbox(window, font=("Helvetica", 12), width=40, height=10)
listbox_passwords.pack()

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox_passwords.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_passwords.yview)

window.mainloop()
