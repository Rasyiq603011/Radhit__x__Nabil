import tkinter as tk    
from tkinter import ttk


root = tk.Tk()

# Konfigurasi langsung pada widget
button = tk.Button(root, text="Tombol", 
                  bg="lightblue",    # Warna latar belakang
                  fg="navy",         # Warna teks
                  font=("Arial", 12),# Font
                  relief="raised",   # Jenis border
                  bd=3)              # Ketebalan border

button.pack(pady=10)
# Menggunakan sistem style
style = ttk.Style()
style.configure("Custom.TButton", 
                background="lightblue", 
                foreground="navy",
                font=("Arial", 12))

button2 = ttk.Button(root, text="Tombol", style="Custom.TButton")
button2.pack(pady=10)

root.mainloop()