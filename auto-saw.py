import tkinter as tk
import time
import threading
import keyboard
from tkinter import ttk  

root = tk.Tk()
root.title("Woofplayz Auto-saw Macro")
root.geometry("400x300")  

is_active = False
selected_key = '2'  

def start_program():
    global is_active
    if not is_active:
        is_active = True
        update_ui_colors("green", "Active")
        threading.Thread(target=press_key_every_10_seconds).start()

def stop_program():
    global is_active
    if is_active:
        is_active = False
        update_ui_colors("red", "Inactive")

def press_key_every_10_seconds():
    global selected_key
    while is_active:
        keyboard.press_and_release(selected_key)
        print(f"Pressed '{selected_key}'")
        time.sleep(10)

def update_ui_colors(color, status_text):
    """Update the UI colors based on the active status."""
    status_label.config(text=status_text, fg="white", bg=color)
    title_label.config(bg=color)
    instructions_label.config(bg=color)
    key_label.config(bg=color)
    root.config(bg=color) 

root.config(bg="red")  

title_label = tk.Label(root, text="Woofplayz Auto-saw Macro", font=("Helvetica", 18), bg="red", fg="white")
title_label.pack(pady=20)

status_label = tk.Label(root, text="Inactive", font=("Helvetica", 24), bg="red", fg="white", width=12)
status_label.pack(pady=10)

instructions_label = tk.Label(root, text="Press Ctrl+B to start, Ctrl+N to stop", font=("Helvetica", 14), bg="red", fg="white")
instructions_label.pack(pady=10)

key_label = tk.Label(root, text="Select a key (1-7):", font=("Helvetica", 14), bg="red", fg="white")
key_label.pack(pady=10)

key_combobox = ttk.Combobox(root, values=[str(i) for i in range(1, 8)], state="readonly")  # Options from 1 to 7
key_combobox.set(selected_key)  
key_combobox.pack(pady=10)

def update_selected_key(event):
    global selected_key
    selected_key = key_combobox.get()
    print(f"Selected key: {selected_key}")

key_combobox.bind("<<ComboboxSelected>>", update_selected_key) 

def listen_for_keys():
    keyboard.add_hotkey('ctrl+b', start_program)
    keyboard.add_hotkey('ctrl+n', stop_program)
    keyboard.wait()

threading.Thread(target=listen_for_keys, daemon=True).start()

root.mainloop()