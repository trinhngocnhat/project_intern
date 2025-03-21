import tkinter as tk
from tkinter import ttk

def translate_text():
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Translated text goes here")

def select_detected_language(event):
    selected_language = detected_lang_var.get()
    print(f"Detected language selected: {selected_language}")

def select_desired_language(event):
    selected_language = desired_lang_var.get()
    print(f"Desired language selected: {selected_language}")

# Create the main window
root = tk.Tk()
root.title("2NB Translate")
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
root.state('zoomed')  # Maximize window

# Create a frame for content alignment
content_frame = tk.Frame(root, bg="white")
content_frame.pack(expand=True, fill='both')

# Title Frame with background color
title_frame = tk.Frame(content_frame, bg="#f1efe7")
title_frame.grid(row=0, column=0, columnspan=2, sticky='nsew')

# Title Label
title_label1 = tk.Label(title_frame, text="2NB", font=("Arial", 30, "bold"), bg="#f1efe7")
title_label1.pack(pady=(20, 0))  # Giảm khoảng cách trên và loại bỏ khoảng cách dưới
title_label2 = tk.Label(title_frame, text="Translate", font=("Arial", 15), bg="#f1efe7")
title_label2.pack(pady=(0, 20))  # Loại bỏ khoảng cách trên và chỉ để khoảng cách dưới

# Row 1 Frame
row1_frame = tk.Frame(content_frame,bg="white")
row1_frame.grid(row=1, column=0, columnspan=2, pady=20, padx=20)

# Language detection dropdown menu
detected_lang_var = tk.StringVar()
detected_lang_var.set("Select Language")
detected_lang_menu = ttk.Combobox(row1_frame, textvariable=detected_lang_var, state="readonly", width=40, font=("Arial", 16))
detected_lang_menu["values"] = ["English", "French", "Spanish", "German", "Vietnamese"]
detected_lang_menu.grid(row=1, column=0, padx=(40, 200),pady=(40, 10)) 
detected_lang_menu.bind("<<ComboboxSelected>>", select_detected_language)

desired_lang_var = tk.StringVar()
desired_lang_var.set("Select Language")
desired_lang_menu = ttk.Combobox(row1_frame, textvariable=desired_lang_var, state="readonly", width=40, font=("Arial", 16))
desired_lang_menu["values"] = ["English", "French", "Spanish", "German", "Vietnamese"]
desired_lang_menu.grid(row=1, column=1,pady=(40, 10)) 
desired_lang_menu.bind("<<ComboboxSelected>>", select_desired_language)

# Input text frame
input_text = tk.Text(content_frame, height=15, width=60, borderwidth=2, relief="solid", font=("Arial", 14), bg="#f1efe7")
input_text.grid(row=2, column=0, padx=40, pady=20)

# Output text frame
output_text = tk.Text(content_frame, height=15, width=60, borderwidth=2, relief="solid", font=("Arial", 14), bg="#f1efe7")
output_text.grid(row=2, column=1, padx=40, pady=20)

# Translate button
translate_button = tk.Button(content_frame, text="Translate", command=translate_text, width=20, height=2, font=("Arial", 16), bg="#f1efe7")
translate_button.grid(row=3, column=0, columnspan=2, pady=20)

# Align columns evenly
content_frame.grid_columnconfigure(0, weight=1)
content_frame.grid_columnconfigure(1, weight=1)

# Run the application
root.mainloop()
