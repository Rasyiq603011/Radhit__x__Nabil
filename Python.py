import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk

class BookLibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Perpustakaan Buku")
        self.root.geometry("800x600")
        
        # Main frame
        main_frame = tk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Canvas dan Scrollbar
        self.canvas = tk.Canvas(main_frame)
        scrollbar_y = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        scrollbar_x = ttk.Scrollbar(main_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        
        # Konfigurasi scrollbar
        self.canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        
        # Penempatan elemen
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Frame untuk grid buku
        self.book_frame = tk.Frame(self.canvas, bg="#fff")
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.book_frame, anchor="nw")
        
        # Event binding untuk scrolling
        self.book_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        
        # Binding mouse wheel untuk scrolling di semua platform
        # Linux (Button-4/Button-5)
        self.canvas.bind("<Button-4>", self.on_mousewheel)
        self.canvas.bind("<Button-5>", self.on_mousewheel)
        # Windows/macOS (MouseWheel)
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)
        
        # Binding tambahan untuk memastikan scrolling bekerja saat kursor di atas item dalam canvas
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        self.canvas.bind_all("<Button-4>", self.on_mousewheel)
        self.canvas.bind_all("<Button-5>", self.on_mousewheel)
        
        # Inisialisasi dictionary untuk menyimpan referensi gambar
        self.photo_references = {}
        
        # Jumlah buku untuk pengujian
        self.total_books = 200
        
        # Tampilkan grid buku
        self.display_books()
    
    def on_mousewheel(self, event):
        """Handler untuk scrolling dengan mouse wheel yang kompatibel dengan semua platform"""
        # Menentukan arah dan jumlah scroll
        if event.num == 4 or event.delta > 0:
            # Scroll ke atas (Linux: Button-4, Windows/macOS: positive delta)
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            # Scroll ke bawah (Linux: Button-5, Windows/macOS: negative delta)
            self.canvas.yview_scroll(1, "units")
    
    def on_frame_configure(self, _event):
        """Menyesuaikan area scrollable berdasarkan ukuran frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def on_canvas_configure(self, event):
        """Menyesuaikan lebar frame saat canvas diubah ukurannya"""
        self.canvas.itemconfig(self.canvas_frame, width=event.width)
    
    def load_image(self, size=(100, 150)):
        image_path = "1.jpeg"
        
        if os.path.exists(image_path):
            try:
                img = Image.open(image_path)
                img = img.resize(size, Image.LANCZOS)
                return ImageTk.PhotoImage(img)
            except Exception as e:
                print(f"Error memuat gambar {image_path}: {e}")
                return self.create_placeholder(size)
        else:
            print(f"File gambar {image_path} tidak ditemukan.")
            return self.create_placeholder(size)
    
    def create_placeholder(self, size=(100, 150)):
        """Membuat placeholder untuk gambar yang tidak ditemukan"""
        img = Image.new('RGB', size, color=(200, 200, 200))
        return ImageTk.PhotoImage(img)
    
    def display_books(self):
        cek = True
        i = 0
        count = 0
        # Implementasi algoritma sesuai permintaan
        while cek:
            for j in range(4):  # 4 kolom
                if count < self.total_books:
                    book_id = count + 1
                    self.create_book_button({
                        "id": book_id,
                        "title": f"Buku #{book_id}"
                    }, i, j)
                    count += 1
                else:
                    cek = False
                    break
            i += 1
    
    def create_book_button(self, book, row, col):
        """Membuat button untuk setiap buku"""
        # Frame untuk setiap buku
        book_frame = tk.Frame(self.book_frame, padx=5, pady=5, bg="#42f5bf")
        book_frame.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)
        
        # Memuat gambar cover (gunakan gambar yang sama untuk semua buku)
        photo = self.load_image()
        self.photo_references[book["id"]] = photo
        
        # Button dengan gambar cover
        btn = tk.Button(
            book_frame, 
            image=photo, 
            text=book["title"],
            compound=tk.TOP,
            width=110,
            height=180,
            wraplength=100
        )
        btn.pack(fill=tk.BOTH, expand=True)
        
        # Menambahkan handler
        btn.configure(command=lambda b=book: self.on_book_click(b))
        
        # Binding scroll pada button juga
        btn.bind("<MouseWheel>", self.on_mousewheel)
        btn.bind("<Button-4>", self.on_mousewheel)
        btn.bind("<Button-5>", self.on_mousewheel)
    
    def on_book_click(self, book):
        """Handler untuk event klik pada buku"""
        print(f"Buku diklik: {book['title']}")
        # Implementasi untuk menampilkan detail buku

# Jalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = BookLibraryApp(root)
    root.mainloop()