import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from datetime import datetime, timedelta


class BookDetailFrame(ttk.Frame):
    """
    Book details display
    """
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.book_id = None
        self.book = None
        self.cover_image = None
        self.setup_ui()

    def setup_ui(self):
        """Setup book detail UI"""
        # Create main container
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create header frame
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Back button
        back_button = ttk.Button(header_frame, text="← Back", command=self.go_back)
        back_button.pack(side=tk.LEFT)
        
        # Page title
        self.title_label = ttk.Label(header_frame, text="Book Details", font=("Helvetica", 16, "bold"))
        self.title_label.pack(side=tk.LEFT, padx=20)
        
        # Content frame
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Book cover and details layout
        self.left_frame = ttk.Frame(content_frame, width=300)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 20))
        self.left_frame.pack_propagate(False)  # Keep width
        
        self.right_frame = ttk.Frame(content_frame)
        self.right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Cover image placeholder
        self.cover_frame = ttk.Frame(self.left_frame, width=250, height=350)
        self.cover_frame.pack(pady=(0, 20))
        self.cover_frame.pack_propagate(False)  # Keep size
        
        self.cover_label = ttk.Label(self.cover_frame)
        self.cover_label.pack(expand=True, fill=tk.BOTH)
        
        # Borrow button
        self.borrow_button = ttk.Button(self.left_frame, text="Borrow", command=self.borrow_book)
        self.borrow_button.pack(fill=tk.X, pady=5)
        
        # Status frame
        status_frame = ttk.Frame(self.left_frame)
        status_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(status_frame, text="Status:", font=("Helvetica", 11, "bold")).pack(side=tk.LEFT)
        self.status_label = ttk.Label(status_frame, text="", font=("Helvetica", 11))
        self.status_label.pack(side=tk.LEFT, padx=(5, 0))
        
        # Book details in right frame
        # Title
        title_frame = ttk.Frame(self.right_frame)
        title_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.book_title_label = ttk.Label(title_frame, text="", font=("Helvetica", 18, "bold"), wraplength=500)
        self.book_title_label.pack(anchor=tk.W)
        
        # Author
        author_frame = ttk.Frame(self.right_frame)
        author_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(author_frame, text="Author:", width=10, anchor=tk.W).pack(side=tk.LEFT)
        self.author_label = ttk.Label(author_frame, text="")
        self.author_label.pack(side=tk.LEFT, fill=tk.X)
        
        # Publisher
        publisher_frame = ttk.Frame(self.right_frame)
        publisher_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(publisher_frame, text="Publisher:", width=10, anchor=tk.W).pack(side=tk.LEFT)
        self.publisher_label = ttk.Label(publisher_frame, text="")
        self.publisher_label.pack(side=tk.LEFT, fill=tk.X)
        
        # Genre
        genre_frame = ttk.Frame(self.right_frame)
        genre_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(genre_frame, text="Genre:", width=10, anchor=tk.W).pack(side=tk.LEFT)
        self.genre_label = ttk.Label(genre_frame, text="")
        self.genre_label.pack(side=tk.LEFT, fill=tk.X)
        
        # Year
        year_frame = ttk.Frame(self.right_frame)
        year_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(year_frame, text="Year:", width=10, anchor=tk.W).pack(side=tk.LEFT)
        self.year_label = ttk.Label(year_frame, text="")
        self.year_label.pack(side=tk.LEFT, fill=tk.X)
        
        # Pages
        pages_frame = ttk.Frame(self.right_frame)
        pages_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(pages_frame, text="Pages:", width=10, anchor=tk.W).pack(side=tk.LEFT)
        self.pages_label = ttk.Label(pages_frame, text="")
        self.pages_label.pack(side=tk.LEFT, fill=tk.X)
        
        # Description
        description_frame = ttk.LabelFrame(self.right_frame, text="Description")
        description_frame.pack(fill=tk.BOTH, expand=True, pady=(20, 0))
        
        # Add scrolling for description
        desc_scroll = ttk.Scrollbar(description_frame)
        desc_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.description_text = tk.Text(description_frame, wrap=tk.WORD, height=10, 
                                       font=("Helvetica", 10), padx=5, pady=5)
        self.description_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Connect scrollbar
        desc_scroll.config(command=self.description_text.yview)
        self.description_text.config(yscrollcommand=desc_scroll.set)
        
        # Make description read-only
        self.description_text.config(state=tk.DISABLED)

    def initialize(self, book_id=None):
        """Initialize with book details"""
        if book_id:
            self.book_id = book_id
            self.load_book()

    def load_book(self):
        """Load book details"""
        if not self.book_id:
            return
            
        # Get book from controller
        self.book = self.controller.get_book(self.book_id)
        
        if not self.book:
            messagebox.showerror("Error", "Book not found")
            self.go_back()
            return
            
        # Update UI with book details
        self.title_label.config(text="Book Details")
        self.book_title_label.config(text=self.book.title)
        self.author_label.config(text=self.book.author)
        self.publisher_label.config(text=self.book.publisher)
        self.genre_label.config(text=self.book.genre)
        self.year_label.config(text=str(self.book.publication_year))
        self.pages_label.config(text=f"{self.book.pages} pages" if self.book.pages else "N/A")
        
        # Update description text
        self.description_text.config(state=tk.NORMAL)
        self.description_text.delete(1.0, tk.END)
        self.description_text.insert(tk.END, self.book.description or "No description available.")
        self.description_text.config(state=tk.DISABLED)
        
        # Load cover image
        self.load_cover_image()
        
        # Update status and button
        self.update_status_and_button()

    def load_cover_image(self):
        """Load book cover image"""
        try:
            # Default placeholder
            placeholder_path = "assets/images/book_placeholder.png"
            
            # Create placeholder if it doesn't exist
            if not os.path.exists(placeholder_path):
                os.makedirs(os.path.dirname(placeholder_path), exist_ok=True)
                img = Image.new('RGB', (200, 300), color=(200, 200, 200))
                img.save(placeholder_path)
            
            # Try to load book cover if exists
            if self.book.cover_image and os.path.exists(self.book.cover_image):
                img = Image.open(self.book.cover_image)
            else:
                img = Image.open(placeholder_path)
                
            # Resize image to fit frame
            img = img.resize((200, 300), Image.LANCZOS)
            self.cover_image = ImageTk.PhotoImage(img)
            self.cover_label.config(image=self.cover_image)
            
        except Exception as e:
            print(f"Error loading cover image: {str(e)}")
            self.cover_label.config(text="No Cover\nAvailable", font=("Helvetica", 12))

    def update_status_and_button(self):
        """Update status label and borrow button based on book status"""
        if not self.book:
            return
            
        # Update status label
        status_color = "green"
        if self.book.status == "Available":
            status_text = "Available"
        elif self.book.status == "Borrowed":
            status_text = "Borrowed"
            status_color = "red"
        elif self.book.status == "Booked":
            status_text = "Booked"
            status_color = "orange"
        else:
            status_text = self.book.status
            
        self.status_label.config(text=status_text, foreground=status_color)
        
        # Update borrow button
        if self.book.status == "Available":
            self.borrow_button.config(text="Borrow", state=tk.NORMAL)
        elif self.book.status == "Booked":
            self.borrow_button.config(text="Book", state=tk.NORMAL)
        else:
            self.borrow_button.config(text="Unavailable", state=tk.DISABLED)

    def borrow_book(self):
        """Initiate book borrowing"""
        if not self.book:
            return
            
        if not self.controller.current_user:
            messagebox.showerror("Error", "You must be logged in to borrow books")
            return
            
        if self.book.status == "Available":
            # Direct borrow
            if messagebox.askyesno("Borrow Book", f"Do you want to borrow '{self.book.title}'?"):
                user_id = self.controller.current_user.user_id
                today = datetime.now()
                days = int(self.controller.config.get("borrow_days", 7))
                due_date = today + timedelta(days=days)
                
                result = self.controller.borrow_book(user_id, self.book.id, today, due_date)
                
                if result:
                    messagebox.showinfo("Success", f"Book borrowed successfully. Due date: {due_date.strftime('%Y-%m-%d')}")
                    self.load_book()  # Refresh to show updated status
                else:
                    messagebox.showerror("Error", "Failed to borrow book")
                    
        elif self.book.status == "Booked":
            # Book for future date
            self.controller.show_frame("BorrowFrame", book_id=self.book.book_id, mode="booking")
            
        else:
            messagebox.showinfo("Unavailable", "This book is currently unavailable for borrowing")

    def go_back(self):
        """Go back to previous screen"""
        self.controller.show_frame("BookListFrame")

if __name__ == "__main__":
    class MockController:
        def __init__(self):
            self.current_user = None
            self.config = {"borrow_days": 7}
        def get_book(self, book_id):
            return None
        def show_frame(self, frame_name):
            pass
            
    root = tk.Tk()
    app = BookDetailFrame(root, MockController())
    root.mainloop()