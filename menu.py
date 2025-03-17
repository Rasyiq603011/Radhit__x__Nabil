import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Menu Utama")

# Ukuran Window
winwidth = 1000
winheight = 800

# Posisi Window di Tengah Layar
scr_width = window.winfo_screenwidth()
scr_height = window.winfo_screenheight()

x_pos = (scr_width // 2) - (winwidth // 2)
y_pos = (scr_height // 2) - (winheight // 2)

window.geometry(f"{winwidth}x{winheight}+{x_pos}+{y_pos}")

# Grid Konfigurasi Utama
window.rowconfigure(0, weight=2)  # Header
window.rowconfigure(1, weight=7)  # Content
window.rowconfigure(2, weight=1)  # Footer
window.columnconfigure(0, weight=1)

# ===================== FRAME HEADER =====================
frame_head = tk.Frame(window, bg="#4C0086")
frame_head.grid(row=0, column=0, sticky="nsew")

frame_head.rowconfigure([0, 1, 2], weight=1)
frame_head.columnconfigure(0, weight=1)

# Judul
judul = tk.Label(frame_head, text="📖 Book-Ku!", font=("Comic Sans MS", 40, "bold"), fg="black", bg="#4C0086")
judul.grid(row=0, column=0, sticky="nsew")

# Welcome Text
welcome = tk.Label(
    frame_head, text="Selamat Datang User! Mau Mencari Buku Apa Hari Ini?",
    font=("Arial", 14), fg="black", bg="#4C0086"
)
welcome.grid(row=1, column=0, sticky="nsew")

# Search Bar dengan Placeholder
SearchBar = tk.Entry(frame_head, fg="black", bg="#00FF11", font=("Arial", 12), justify="center")
SearchBar.grid(row=2, column=0, sticky="nsew", padx=200, pady=5)

def placeholder(entry, text):
    entry.insert(0, text)
    entry.config(fg="grey")

    def on_focus_in(event):
        if entry.get() == text:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, text)
            entry.config(fg="grey")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

placeholder(SearchBar, "Search Your Book Here")

# ===================== FRAME CONTENT (SCROLLABLE) =====================
# Ubah warna latar dari green ke black untuk konsistensi
frame_content = tk.Frame(window, bg="black")
frame_content.grid(row=1, column=0, sticky="nsew")

# Wrap canvas in a container to make it center-aligned - ubah warna juga ke black
canvas_container = tk.Frame(frame_content, bg="black")
canvas_container.pack(expand=True, fill="both", anchor="center")

# Canvas untuk Scrollable Frame
canvas = tk.Canvas(canvas_container, bg="black")  # Ubah warna canvas ke black untuk konsistensi
scrollbar = tk.Scrollbar(frame_content, orient="vertical", command=canvas.yview)

canvas.configure(yscrollcommand=scrollbar.set)
canvas_container.pack(fill="both", expand=True)
canvas.pack(side="left", anchor="center", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Buat frame yang akan discroll
scrollable_frame = tk.Frame(canvas, bg="black")

# Jumlah total buku
total_books = 50
cols = 5

# Baris dan kolom
rows = (total_books + cols - 1) // cols

# Hitung ukuran button container
button_width = 120  # Perkiraan lebar tombol (dengan padding)
total_width = button_width * cols

# Pastikan canvas window tetap di tengah
def center_scrollable_frame(event=None):
    canvas.update_idletasks()
    canvas_width = canvas.winfo_width()
    frame_width = total_width
    
    # Hitung posisi x untuk menempatkan frame di tengah
    x_position = max(0, (canvas_width - frame_width) // 2)
    
    # Update posisi canvas window
    canvas.create_window((x_position, 0), window=scrollable_frame, anchor="nw")
    
    # Update scroll region
    canvas.configure(scrollregion=canvas.bbox("all"))

# Load Gambar
size = (100, 150)
book_img = Image.open("image.jpeg")
book_img = book_img.resize(size, Image.LANCZOS)
book_img = ImageTk.PhotoImage(book_img)

# Menampilkan Buku dalam Bentuk Tombol
def buku_dipilih(nomor):
    print(f"Buku {nomor} dipilih!")

# Hitung lebar button container
button_container = tk.Frame(scrollable_frame, bg="black")
button_container.pack(pady=20)

# Tempatkan tombol dalam grid
for index in range(total_books):
    row = index // cols
    col = index % cols

    btn = tk.Button(
        button_container, image=book_img, bg="white", borderwidth=2, 
        text=f"Buku {index}", compound="top",
        command=lambda i=index: buku_dipilih(i)
    )
    btn.image = book_img  # Agar tidak terhapus oleh garbage collector
    btn.grid(row=row, column=col, padx=10, pady=10)

# Tambahkan frame kosong di bawah button_container untuk memberi ruang tambahan
# dan mencegah terlihatnya latar belakang yang berbeda warna
bottom_padding = tk.Frame(scrollable_frame, bg="black", height=50)
bottom_padding.pack(fill="x", expand=True)

# Bind events
canvas.bind("<Configure>", center_scrollable_frame)
scrollable_frame.bind("<Configure>", lambda e: center_scrollable_frame())

def on_mouse_wheel(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

canvas.bind_all("<MouseWheel>", on_mouse_wheel)

# Initial center after all components are added
window.update_idletasks()
center_scrollable_frame()

# ===================== FRAME FOOTER =====================
frame_foot = tk.Frame(window, bg="#4C0086")
frame_foot.grid(row=2, column=0, sticky="nsew")

window.mainloop()