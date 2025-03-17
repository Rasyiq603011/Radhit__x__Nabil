import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont

class LibraryManagementSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Konfigurasi window
        self.title("📚 Library Management System")
        self.geometry("800x600")
        self.minsize(800, 600)
        
        # Mengatur font
        default_font = tkfont.nametofont("TkDefaultFont")
        default_font.configure(size=10)
        self.option_add("*Font", default_font)
        
        # Frame utama
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Tampilkan halaman koleksi buku
        self.show_book_collection()
        
    def show_book_collection(self):
        # Hapus widget yang ada di main_frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
        # Header
        header_frame = ttk.Frame(self.main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Tombol Back
        back_button = ttk.Button(header_frame, text="← Back", width=10)
        back_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # Judul halaman
        title_font = tkfont.Font(family="Arial", size=16, weight="bold")
        title_label = ttk.Label(header_frame, text="Book Collection", font=title_font)
        title_label.pack(side=tk.LEFT, padx=5)
        
        # Frame Search
        search_frame = ttk.Frame(self.main_frame)
        search_frame.pack(fill=tk.X, pady=5)
        
        # Label Search
        search_label = ttk.Label(search_frame, text="Search:")
        search_label.pack(side=tk.LEFT, padx=(0, 5))
        
        # Entry Search
        search_entry = ttk.Entry(search_frame, width=30)
        search_entry.pack(side=tk.LEFT, padx=5)
        
        # Dropdown Search Type
        search_type = ttk.Combobox(search_frame, values=["title", "author", "isbn"], width=15, state="readonly")
        search_type.current(0)
        search_type.pack(side=tk.LEFT, padx=5)
        
        # Tombol Search
        search_button = ttk.Button(search_frame, text="Search")
        search_button.pack(side=tk.LEFT, padx=5)
        
        # Tombol Reset
        reset_button = ttk.Button(search_frame, text="Reset")
        reset_button.pack(side=tk.LEFT, padx=5)
        
        # Frame Filter
        filter_frame = ttk.LabelFrame(self.main_frame, text="Filters")
        filter_frame.pack(fill=tk.X, pady=10)
        
        # Filter baris 1
        filter_row1 = ttk.Frame(filter_frame)
        filter_row1.pack(fill=tk.X, padx=10, pady=5)
        
        # Author filter
        ttk.Label(filter_row1, text="Author:").pack(side=tk.LEFT, padx=(0, 5))
        author_combo = ttk.Combobox(filter_row1, values=["All", "Author 1", "Author 2"], width=20, state="readonly")
        author_combo.current(0)
        author_combo.pack(side=tk.LEFT, padx=(0, 20))
        
        # Genre filter
        ttk.Label(filter_row1, text="Genre:").pack(side=tk.LEFT, padx=(0, 5))
        genre_combo = ttk.Combobox(filter_row1, values=["All", "Fiction", "Non-Fiction", "Science"], width=20, state="readonly")
        genre_combo.current(0)
        genre_combo.pack(side=tk.LEFT)
        
        # Filter baris 2
        filter_row2 = ttk.Frame(filter_frame)
        filter_row2.pack(fill=tk.X, padx=10, pady=5)
        
        # Publisher filter
        ttk.Label(filter_row2, text="Publisher:").pack(side=tk.LEFT, padx=(0, 5))
        publisher_combo = ttk.Combobox(filter_row2, values=["All", "Publisher 1", "Publisher 2"], width=20, state="readonly")
        publisher_combo.current(0)
        publisher_combo.pack(side=tk.LEFT, padx=(0, 10))
        
        # Status filter
        ttk.Label(filter_row2, text="Status:").pack(side=tk.LEFT, padx=(0, 5))
        status_combo = ttk.Combobox(filter_row2, values=["All", "Available", "Borrowed"], width=20, state="readonly")
        status_combo.current(0)
        status_combo.pack(side=tk.LEFT, padx=(0, 10))
        
        # Apply filter button
        apply_filter_button = ttk.Button(filter_row2, text="Apply Filters")
        apply_filter_button.pack(side=tk.RIGHT, padx=5)
        
        # Frame untuk daftar buku
        book_list_frame = ttk.Frame(self.main_frame)
        book_list_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Menampilkan pesan "No books found"
        no_books_label = ttk.Label(
            book_list_frame, 
            text="No books found matching your criteria",
            font=("Arial", 12),
            foreground="#555555"
        )
        no_books_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Frame untuk pagination
        pagination_frame = ttk.Frame(self.main_frame)
        pagination_frame.pack(fill=tk.X, pady=10)
        
        # Previous button
        prev_button = ttk.Button(pagination_frame, text="< Previous", state=tk.DISABLED)
        prev_button.pack(side=tk.LEFT)
        
        # Page info
        page_label = ttk.Label(pagination_frame, text="Page 1 of 1")
        page_label.pack(side=tk.LEFT, padx=20)
        
        # Next button
        next_button = ttk.Button(pagination_frame, text="Next >", state=tk.DISABLED)
        next_button.pack(side=tk.LEFT)
        
        # Status bar
        status_bar = ttk.Label(self.main_frame, text="Displaying 0 books", relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(fill=tk.X, side=tk.BOTTOM, pady=(5, 0))

if __name__ == "__main__":
    app = LibraryManagementSystem()
    
    # Style settings untuk tampilan modern
    style = ttk.Style()
    style.theme_use('clam')  # Gunakan 'vista' atau 'winnative' di Windows untuk tampilan native
    
    # Mengatur style untuk beberapa widget
    style.configure("TLabelframe", borderwidth=1, relief="solid")
    style.configure("TButton", padding=5)
    
    app.mainloop()