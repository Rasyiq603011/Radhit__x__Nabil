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
frame_head = tk.Frame(window, bg="#4C0086", pady=20)
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
# Bagian ini dioptimalkan untuk menghilangkan ruang kosong
content_bg = "black"  # Warna konsisten untuk latar belakang

# Frame utama konten
frame_content = tk.Frame(window, bg=content_bg)
frame_content.grid(row=1, column=0, sticky="nsew")
frame_content.rowconfigure(0, weight=1)
frame_content.columnconfigure(0, weight=1)

# Canvas untuk scrolling
canvas = tk.Canvas(frame_content, bg=content_bg, highlightthickness=0)
scrollbar = tk.Scrollbar(frame_content, orient="vertical", command=canvas.yview)

# Konfigurasi canvas dan scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

# Frame untuk konten yang dapat di-scroll
scrollable_frame = tk.Frame(canvas, bg=content_bg)
scrollable_frame_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", tags="scrollable_frame")

# Jumlah total buku dan layout
total_books = 50
cols = 5
rows = (total_books + cols - 1) // cols

# Update fungsi agar canvas selalu mengikuti ukuran frame konten
def configure_scroll_region(event):
    # Update scrollregion berdasarkan ukuran konten
    canvas.configure(scrollregion=canvas.bbox("all"))
    
    # Pastikan frame konten mengisi lebar canvas
    canvas_width = canvas.winfo_width()
    if canvas_width > 1:  # Hanya update jika canvas sudah memiliki lebar
        canvas.itemconfig(scrollable_frame_id, width=canvas_width)

scrollable_frame.bind("<Configure>", configure_scroll_region)

# Fungsi untuk menyesuaikan lebar frame scrollable dengan canvas
def adjust_frame_width(event):
    canvas_width = event.width
    canvas.itemconfig(scrollable_frame_id, width=canvas_width)

canvas.bind("<Configure>", adjust_frame_width)

# Load Gambar
size = (100, 150)
book_img = Image.open("image.jpeg")
book_img = book_img.resize(size, Image.LANCZOS)
book_img = ImageTk.PhotoImage(book_img)

# Menampilkan Buku dalam Bentuk Tombol
def buku_dipilih(nomor):
    print(f"Buku {nomor} dipilih!")

# Container untuk grid buku
book_grid = tk.Frame(scrollable_frame, bg="green", padx=100, pady=20)
book_grid.pack(fill="both", expand=True)

# book_grid.columnconfigure()

# Grid untuk buku-buku
for index in range(total_books):
    row = index // cols
    col = index % cols
    
    # Frame untuk setiap buku (container putih)
    book_frame = tk.Frame(book_grid, bg="white", bd=2, relief="solid")
    book_frame.grid(row=row, column=col, padx=10, pady=10)
    
    # Tombol gambar buku
    btn = tk.Button(
        book_frame, 
        image=book_img, 
        bg="white", 
        borderwidth=0,
        command=lambda i=index: buku_dipilih(i)
    )
    btn.image = book_img  # Agar tidak terhapus oleh garbage collector
    btn.pack(padx=15, pady=5)
    
    # Label teks buku
    book_label = tk.Label(book_frame, text=f"Buku {index}", bg="white")
    book_label.pack(padx=5, pady=5)

# Pastikan grid kolom seimbang
for i in range(cols):
    book_grid.columnconfigure(i, weight=1)

# Tambahkan padding frame untuk mengisi space kosong di bawah grid buku
# Ini akan menyesuaikan dengan sisa ruang di frame konten
bottom_spacer = tk.Frame(scrollable_frame, bg=content_bg, height=10)
bottom_spacer.pack(fill="both", expand=True)

def on_mouse_wheel(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

canvas.bind_all("<MouseWheel>", on_mouse_wheel)

# ===================== FRAME FOOTER =====================
frame_foot = tk.Frame(window, bg="#4C0086")
frame_foot.grid(row=2, column=0, sticky="nsew")

# Pastikan semua konten di-render sebelum mengkonfigurasi scrolling
window.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))

window.mainloop()