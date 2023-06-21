import tkinter as tk
import subprocess
from tkinter import messagebox
from tkinter import simpledialog

# Function to execute compiler.py
def execute_compiler():
    result = subprocess.run(["python", "compiler.py"], capture_output=True, text=True)
    output_window(result.stdout)

# Function to execute tokenizer.py
def execute_tokenizer():
    result = subprocess.run(["python", "analyzer/tokenizer.py"], capture_output=True, text=True)
    output_window(result.stdout)

# Function to execute clean.py
def execute_clean():
    result = subprocess.run(["python", "analyzer/clean.py"], capture_output=True, text=True)
    output_window(result.stdout)

# Function to generate intermediate code
def generate_intermediate_code():
    result = subprocess.run(["python", "analyzer/intermediate_code_generator.py"], capture_output=True, text=True)
    output_window(result.stdout)

# Function to display output in a popup window
def output_window(output):
    window = tk.Toplevel()
    window.title("Output")
    output_text = tk.Text(window, font=("Arial", 12), wrap="word")
    output_text.insert("end", output)
    output_text.pack(fill="both", expand=True)

# Function to get user input
def get_input():
    value = simpledialog.askstring("Input", "Enter a value:")
    if value:
        messagebox.showinfo("Input Value", f"The entered value is: {value}")
    else:
        messagebox.showwarning("Input Error", "No value entered.")

# Create the main window
window = tk.Tk()
window.title("LexoSynto Compiler 😶‍🌫️")

# Set the background image
background_image = tk.PhotoImage(file="Blue and Yellow Gradient Modern Desktop Wallpaper.png")
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Customize button colors
button_bg_color = "#007acc"  # Blue color
button_fg_color = "#ffffff"  # White color

# Create buttons for each file
compiler_button = tk.Button(window, text="Execute Compiler", command=execute_compiler, font=("Arial", 20), background="yellow",fg="black")
compiler_button.pack(padx=60, pady=(340, 0))

tokenizer_button = tk.Button(window, text="Execute Tokenizer", command=execute_tokenizer, font=("Arial", 20), background="yellow",fg="black")
tokenizer_button.pack(padx=60, pady=(60, 0))

clean_button = tk.Button(window, text="Execute Clean", command=execute_clean, font=("Arial", 20), background="yellow",fg="black")
clean_button.pack(padx=60, pady=(60, 0))



# Start the GUI main loop
window.mainloop()
