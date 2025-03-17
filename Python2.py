import tkinter as tk
from tkinter import ttk, StringVar, Entry, Button, Frame, Label
import os
from PIL import Image, ImageTk
import math
import random

class BookLibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Perpustakaan Buku")
        self.root.geometry("1000x700")
        
        # Data buku (simulasi database)
        self.total_books = 100000
        self.books_per_page = 100
        self.current_page = 1
        self.total_pages = math.ceil(self.total_books / self.books_per_page)
        
        # Kategori untuk data dummy
        self.categories = ["Fiksi", "Psikologi", "Sejarah", "Penunjang Pendidikan", 
                          "Ekonomi", "Teknologi", "Sastra", "Filosofi", "Sains", "Biografi"]
        self.publishers = ["Indoliterasi", "Bumi Literasi", "Gramedia", "Penerbit Erlangga", 
                          "Mizan", "Pustaka Utama", "Grasindo", "Kompas", "Balai Pustaka"]
        
        # Folder untuk gambar cover
        self.cover_folder = "D:\\Project 1\\coba\\python\\Cover"
        
        # Pastikan folder Cover ada
        if not os.path.exists(self.cover_folder):
            os.makedirs(self.cover_folder)
            print(f"Folder {self.cover_folder} dibuat karena tidak ditemukan")
        
        # Main frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Search frame
        self.create_search_frame()
        
        # Books display frame with scrollbars
        self.create_books_display_frame()
        
        # Pagination frame
        self.create_pagination_frame()
        
        # Inisialisasi dictionary untuk menyimpan referensi gambar
        self.photo_references = {}
        
        # Tampilkan buku halaman pertama
        self.display_current_page()
    
    def create_search_frame(self):
        """Membuat frame untuk pencarian buku"""
        search_frame = tk.Frame(self.main_frame, pady=10)
        search_frame.pack(fill=tk.X)
        
        # Label
        tk.Label(search_frame, text="Cari Buku:").pack(side=tk.LEFT, padx=(0, 10))
        
        # Search entry
        self.search_var = StringVar()
        search_entry = Entry(search_frame, textvariable=self.search_var, width=40)
        search_entry.pack(side=tk.LEFT, padx=(0, 10))
        
        # Search button
        Button(search_frame, text="Cari", command=self.search_books).pack(side=tk.LEFT)
        
        # Reset button
        Button(search_frame, text="Reset", command=self.reset_search).pack(side=tk.LEFT, padx=(10, 0))
    
    def create_books_display_frame(self):
        """Membuat frame untuk menampilkan buku dengan scrollbar"""
        # Container frame
        display_container = tk.Frame(self.main_frame)
        display_container.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Canvas dan Scrollbar
        self.canvas = tk.Canvas(display_container)
        scrollbar_y = ttk.Scrollbar(display_container, orient=tk.VERTICAL, command=self.canvas.yview)
        scrollbar_x = ttk.Scrollbar(display_container, orient=tk.HORIZONTAL, command=self.canvas.xview)
        
        # Konfigurasi scrollbar
        self.canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        
        # Penempatan elemen
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Frame untuk grid buku
        self.book_frame = tk.Frame(self.canvas)
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.book_frame, anchor="nw")
        
        # Event binding untuk scrolling
        self.book_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        
        # Tambahkan header tabel
        self.create_table_header()
    
    def create_table_header(self):
        """Membuat header tabel"""
        # Definisi header
        headers = ["Judul Buku", "Penulis", "Penerbit", "Kategori", "ISBN", "Tahun"]
        widths = [300, 150, 120, 100, 120, 60]
        
        # Buat frame header
        header_frame = tk.Frame(self.book_frame, bg="#f0f0f0")
        header_frame.grid(row=0, column=0, sticky="ew", columnspan=4)
        
        # Tempatkan header
        for i, (header, width) in enumerate(zip(headers, widths)):
            lbl = tk.Label(header_frame, text=header, font=("Arial", 10, "bold"), 
                          width=width//10, bg="#f0f0f0", anchor="w", padx=5)
            lbl.grid(row=0, column=i, sticky="ew", padx=2, pady=5)
        
        # Garis pemisah
        sep = ttk.Separator(self.book_frame, orient="horizontal")
        sep.grid(row=1, column=0, sticky="ew", columnspan=4, pady=2)
    
    def create_pagination_frame(self):
        """Membuat frame untuk navigasi halaman"""
        pagination_frame = tk.Frame(self.main_frame)
        pagination_frame.pack(fill=tk.X, pady=10)
        
        # Frame info halaman
        info_frame = tk.Frame(pagination_frame)
        info_frame.pack(side=tk.LEFT)
        
        self.page_info_label = tk.Label(info_frame, 
                                       text=f"Menampilkan 1 sampai {self.books_per_page} dari {self.total_books} entri")
        self.page_info_label.pack(side=tk.LEFT)
        
        # Frame tombol navigasi
        nav_frame = tk.Frame(pagination_frame)
        nav_frame.pack(side=tk.RIGHT)
        
        Button(nav_frame, text="Previous", command=self.prev_page).pack(side=tk.LEFT, padx=2)
        
        # Jumlah tombol halaman yang ditampilkan
        max_page_buttons = 5
        
        # Tambahkan tombol halaman
        self.page_buttons = []
        for i in range(1, min(max_page_buttons + 1, self.total_pages + 1)):
            btn = Button(nav_frame, text=str(i), width=3,
                        command=lambda p=i: self.go_to_page(p))
            btn.pack(side=tk.LEFT, padx=2)
            self.page_buttons.append(btn)
        
        # Jika halaman banyak, tambahkan elipsis dan tombol halaman terakhir
        if self.total_pages > max_page_buttons:
            tk.Label(nav_frame, text="...").pack(side=tk.LEFT, padx=2)
            Button(nav_frame, text=str(self.total_pages), width=3,
                  command=lambda: self.go_to_page(self.total_pages)).pack(side=tk.LEFT, padx=2)
        
        Button(nav_frame, text="Next", command=self.next_page).pack(side=tk.LEFT, padx=2)
        
        # Label dan input untuk langsung ke halaman tertentu
        tk.Label(nav_frame, text="Halaman:").pack(side=tk.LEFT, padx=(10, 2))
        self.page_entry = tk.Entry(nav_frame, width=5)
        self.page_entry.pack(side=tk.LEFT, padx=2)
        Button(nav_frame, text="Go", command=self.jump_to_page).pack(side=tk.LEFT, padx=2)
    
    def update_page_info(self):
        """Memperbarui informasi halaman"""
        start = (self.current_page - 1) * self.books_per_page + 1
        end = min(start + self.books_per_page - 1, self.total_books)
        self.page_info_label.config(text=f"Menampilkan {start} sampai {end} dari {self.total_books} entri")
    
    def update_pagination_buttons(self):
        """Memperbarui tampilan tombol paginasi"""
        # Tentukan range tombol halaman yang ditampilkan
        max_page_buttons = len(self.page_buttons)
        half = max_page_buttons // 2
        
        # Hitung range halaman
        start_page = max(1, self.current_page - half)
        end_page = min(start_page + max_page_buttons - 1, self.total_pages)
        
        # Sesuaikan start_page jika end_page mencapai batas
        if end_page - start_page < max_page_buttons - 1:
            start_page = max(1, end_page - max_page_buttons + 1)
        
        # Update text tombol
        for i, btn in enumerate(self.page_buttons):
            page_num = start_page + i
            if page_num <= self.total_pages:
                btn.config(text=str(page_num), 
                          bg="#007bff" if page_num == self.current_page else "#f0f0f0",
                          fg="white" if page_num == self.current_page else "black")
                btn.config(command=lambda p=page_num: self.go_to_page(p))
                btn.pack_forget()
                btn.pack(side=tk.LEFT, padx=2)
            else:
                btn.pack_forget()
    
    def on_frame_configure(self, event):
        """Menyesuaikan area scrollable berdasarkan ukuran frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def on_canvas_configure(self, event):
        """Menyesuaikan lebar frame saat canvas diubah ukurannya"""
        self.canvas.itemconfig(self.canvas_frame, width=event.width)
    
    def load_image(self, book_id, size=(50, 70)):
        """Memuat gambar cover buku dari folder Cover dengan nama file image_X"""
        try:
            # Path file gambar dengan format image_X
            image_path = os.path.join(self.cover_folder, f"image_{book_id}")
            
            # Coba mencari file dengan ekstensi umum
            for ext in ['.jpg', '.jpeg', '.png', '.gif']:
                full_path = image_path + ext
                if os.path.exists(full_path):
                    img = Image.open(full_path)
                    img = img.resize(size, Image.LANCZOS)
                    return ImageTk.PhotoImage(img)
            
            # Jika tidak ditemukan file dengan nama yang sesuai, gunakan placeholder
            return self.create_placeholder(size)
        except Exception as e:
            print(f"Error memuat gambar untuk buku ID {book_id}: {e}")
            return self.create_placeholder(size)
    
    def create_placeholder(self, size=(50, 70)):
        """Membuat placeholder untuk gambar yang tidak ditemukan"""
        img = Image.new('RGB', size, color=(200, 200, 200))
        return ImageTk.PhotoImage(img)
    
    def generate_dummy_book(self, book_id):
        """Menghasilkan data buku dummy berdasarkan ID"""
        # Gunakan ID sebagai seed untuk memastikan data yang sama untuk ID yang sama
        random.seed(book_id)
        
        # Judul berdasarkan ID
        titles = [
            f"A HISTORY OF {random.choice(['CHINA', 'EUROPE', 'ASIA', 'AFRICA', 'AMERICA'])}",
            f"Introduction to {random.choice(['Psychology', 'Philosophy', 'Mathematics', 'Physics', 'Chemistry'])}",
            f"Bank Soal Super Lengkap {random.choice(['SD', 'SMP', 'SMA', 'IPA', 'IPS', 'Matematika'])}",
            f"The Art of {random.choice(['Programming', 'Design', 'Writing', 'Communication', 'Leadership'])}",
            f"Modern {random.choice(['Science', 'Technology', 'Medicine', 'Economics', 'Politics'])}"
        ]
        
        # Penulis
        authors = [
            f"{random.choice(['Mark', 'John', 'Linda', 'Sarah', 'David', 'Michael', 'Sigmund', 'Frederick'])} "
            f"{random.choice(['Twain', 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Freud', 'Wells'])}"
        ]
        
        # Data buku
        return {
            "id": book_id,
            "title": random.choice(titles) + f" {book_id//1000}",
            "author": random.choice(authors),
            "publisher": random.choice(self.publishers),
            "category": random.choice(self.categories),
            "isbn": f"978-602-{random.randint(1000, 9999)}-{random.randint(10, 99)}-{random.randint(1, 9)}",
            "year": str(random.randint(2010, 2023))
        }
    
    def get_books_for_page(self, page_num):
        """Mendapatkan data buku untuk halaman tertentu"""
        start_idx = (page_num - 1) * self.books_per_page
        books = []
        
        for i in range(start_idx, min(start_idx + self.books_per_page, self.total_books)):
            book_id = i + 1
            books.append(self.generate_dummy_book(book_id))
            
        return books
    
    def display_current_page(self):
        """Menampilkan buku untuk halaman saat ini"""
        # Hapus semua widget dari frame buku kecuali header
        for widget in self.book_frame.winfo_children():
            if widget.grid_info().get('row', 0) > 1:  # Pertahankan header
                widget.destroy()
        
        books = self.get_books_for_page(self.current_page)
        self.display_books(books)
        
        # Update info paginasi
        self.update_page_info()
        self.update_pagination_buttons()
        
        # Reset scroll ke atas
        self.canvas.yview_moveto(0)
    
    def display_books(self, books):
        """Menampilkan daftar buku dalam tabel"""
        # Mulai dari row 2 (setelah header dan separator)
        start_row = 2
        
        for i, book in enumerate(books):
            row = start_row + i
            
            # Frame untuk satu baris buku
            book_row = tk.Frame(self.book_frame)
            book_row.grid(row=row, column=0, sticky="ew", columnspan=4, pady=1)
            
            # Load gambar dengan ID buku
            photo = self.load_image(book["id"])
            photo_button = tk.Button(book_row, image=photo, relief="flat", cursor="hand2",
                                   command=lambda b=book: print(f"Selected book: {b['title']}"))
            photo_button.grid(row=0, column=0, padx=5, pady=2)
            self.photo_references[book["id"]] = photo
            
            # Informasi buku
            title_label = tk.Label(book_row, text=book["title"], anchor="w", width=30, 
                                  wraplength=280, justify=tk.LEFT)
            title_label.grid(row=0, column=1, sticky="w", padx=5)
            
            author_label = tk.Label(book_row, text=book["author"], anchor="w", width=15)
            author_label.grid(row=0, column=2, sticky="w", padx=5)
            
            publisher_label = tk.Label(book_row, text=book["publisher"], anchor="w", width=12)
            publisher_label.grid(row=0, column=3, sticky="w", padx=5)
            
            category_label = tk.Label(book_row, text=book["category"], anchor="w", width=10)
            category_label.grid(row=0, column=4, sticky="w", padx=5)
            
            isbn_label = tk.Label(book_row, text=book["isbn"], anchor="w", width=12)
            isbn_label.grid(row=0, column=5, sticky="w", padx=5)
            
            year_label = tk.Label(book_row, text=book["year"], anchor="w", width=6)
            year_label.grid(row=0, column=6, sticky="w", padx=5)
            
            # Garis pemisah
            if i < len(books) - 1:
                sep = ttk.Separator(self.book_frame, orient="horizontal")
                sep.grid(row=row+1, column=0, sticky="ew", columnspan=4, pady=2)
    
    def prev_page(self):
        """Pindah ke halaman sebelumnya"""
        if self.current_page > 1:
            self.current_page -= 1
            self.display_current_page()
    
    def next_page(self):
        """Pindah ke halaman berikutnya"""
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.display_current_page()
    
    def go_to_page(self, page):
        """Pindah ke halaman tertentu"""
        if 1 <= page <= self.total_pages:
            self.current_page = page
            self.display_current_page()
    
    def jump_to_page(self):
        """Pindah ke halaman yang diinput"""
        try:
            page = int(self.page_entry.get())
            if 1 <= page <= self.total_pages:
                self.go_to_page(page)
            else:
                print(f"Halaman harus antara 1 dan {self.total_pages}")
        except ValueError:
            print("Masukkan nomor halaman yang valid")
    
    def search_books(self):
        """Mencari buku berdasarkan input pengguna"""
        search_term = self.search_var.get().lower()
        if not search_term:
            return
            
        print(f"Mencari buku dengan kata kunci: {search_term}")
        # Implementasi pencarian sebenarnya
        # Di sini hanya simulasi, dalam aplikasi nyata lakukan query ke database
        
        # Reset halaman ke 1 setelah pencarian
        self.current_page = 1
        self.display_current_page()
    
    def reset_search(self):
        """Reset pencarian"""
        self.search_var.set("")
        self.current_page = 1
        self.display_current_page()

# Jalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = BookLibraryApp(root)
    root.mainloop()