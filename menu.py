import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

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
frame_content = tk.Frame(window, bg="white")
frame_content.grid(row=1, column=0, sticky="nsew")

# Canvas untuk Scrollable Frame
canvas = tk.Canvas(frame_content, bg="white")
scrollbar = tk.Scrollbar(frame_content, orient="vertical", command=canvas.yview)

scrollable_frame = tk.Frame(canvas, bg="white")
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Grid Konfigurasi untuk 5 Kolom
cols = 5
for i in range(cols):
    scrollable_frame.columnconfigure(i, weight=1)

# Load Gambar
book_img = PhotoImage(file="image.png")  # Pastikan file ada
book_img = book_img.subsample(2, 2)  # Resize agar pas

# Jumlah total buku
total_books = 50

# Menampilkan Buku dalam Bentuk Tombol
def buku_dipilih(nomor):
    print(f"Buku {nomor} dipilih!")

for index in range(total_books):
    row = index // cols
    col = index % cols

    btn = tk.Button(
        scrollable_frame, image=book_img, bg="white", borderwidth=2,
        command=lambda i=index: buku_dipilih(i)
    )
    btn.image = book_img  # Agar tidak terhapus oleh garbage collector
    btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")


def on_mouse_wheel(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

canvas.bind_all("<MouseWheel>", on_mouse_wheel)


frame_foot = tk.Frame(window, bg="#4C0086")
frame_foot.grid(row=2, column=0, sticky="nsew")

window.mainloop()
