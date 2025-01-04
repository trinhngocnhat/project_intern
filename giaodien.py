import tkinter as tk
from tkinter import ttk

def translate_text():
    # Logic for translation will go here (placeholder for now)
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
root.title("Translator")
root.geometry("800x500")

# Center the window
root.update_idletasks()
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"800x500+{x}+{y}")

# Create a frame for content alignment
content_frame = tk.Frame(root)
content_frame.pack(expand=True)

# Language detection dropdown menu
detected_lang_var = tk.StringVar()
detected_lang_var.set("Select Language")
detected_lang_menu = ttk.Combobox(content_frame, textvariable=detected_lang_var, state="readonly", width=40)
detected_lang_menu["values"] = ["English", "French", "Spanish", "German", "Vietnamese"]
detected_lang_menu.grid(row=0, column=0, padx=20, pady=20)
detected_lang_menu.bind("<<ComboboxSelected>>", select_detected_language)

# Desired language dropdown menu
desired_lang_var = tk.StringVar()
desired_lang_var.set("Select Language")
desired_lang_menu = ttk.Combobox(content_frame, textvariable=desired_lang_var, state="readonly", width=40)
desired_lang_menu["values"] = ["English", "French", "Spanish", "German", "Vietnamese"]
desired_lang_menu.grid(row=0, column=1, padx=20, pady=20)
desired_lang_menu.bind("<<ComboboxSelected>>", select_desired_language)

# Input text frame
input_text = tk.Text(content_frame, height=20, width=75, borderwidth=2, relief="solid")
input_text.grid(row=1, column=0, padx=20, pady=20)

# Output text frame
output_text = tk.Text(content_frame, height=20, width=75, borderwidth=2, relief="solid")
output_text.grid(row=1, column=1, padx=20, pady=20)

# Translate button
translate_button = tk.Button(content_frame, text="Translate", command=translate_text, width=20, height=2)
translate_button.grid(row=2, column=0, columnspan=2, pady=20)

# Align columns evenly
content_frame.grid_columnconfigure(0, weight=1)
content_frame.grid_columnconfigure(1, weight=1)

# Run the application
root.mainloop()
