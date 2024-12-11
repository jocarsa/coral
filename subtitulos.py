import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def clean_srt_to_text(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as srt_file:
            lines = srt_file.readlines()
        
        cleaned_lines = []
        for line in lines:
            if line.strip().isdigit() or '-->' in line:
                continue
            cleaned_line = line.strip()
            if cleaned_line:
                cleaned_lines.append(cleaned_line)
        
        plain_text = ' '.join(cleaned_lines)

        with open(output_file, 'w', encoding='utf-8') as output:
            output.write(plain_text)

        messagebox.showinfo("Success", f"Plain text saved to {output_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def select_input_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("SRT Files", "*.srt"), ("All Files", "*.*")]
    )
    if file_path:
        input_file_var.set(file_path)


def select_output_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        output_file_var.set(file_path)


def process_files():
    input_file = input_file_var.get()
    output_file = output_file_var.get()

    if not input_file:
        messagebox.showwarning("Input File Missing", "Please select an input file.")
        return
    if not output_file:
        messagebox.showwarning("Output File Missing", "Please specify an output file.")
        return

    clean_srt_to_text(input_file, output_file)


# GUI Setup
app = ttk.Window(themename="cosmo", title="SRT to Plain Text Converter")
app.geometry("400x300")

app.style.configure("TButton", background="#FF7F50", foreground="white")  # Coral color
app.style.configure("TLabel", foreground="#FF7F50")  # Coral color for labels

# Variables for file paths
input_file_var = tk.StringVar()
output_file_var = tk.StringVar()

# Input file selection
ttk.Label(app, text="Input SRT File:").pack(pady=10, anchor="w", padx=20)
ttk.Entry(app, textvariable=input_file_var, state="readonly").pack(fill="x", padx=20, pady=5)
ttk.Button(app, text="Select File", command=select_input_file).pack(pady=5)

# Output file selection
ttk.Label(app, text="Output Text File:").pack(pady=10, anchor="w", padx=20)
ttk.Entry(app, textvariable=output_file_var, state="readonly").pack(fill="x", padx=20, pady=5)
ttk.Button(app, text="Select File", command=select_output_file).pack(pady=5)

# Process Button
ttk.Button(app, text="Convert", command=process_files).pack(pady=20)

# Start the application
app.mainloop()
