import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

class HomeFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.mainFrame = tk.Frame(self.master, bg="white")
        self.mainFrame.pack(fill=tk.BOTH, expand=True)


    def create_widgets(self):
        # Header frame
        self.header_frame = tk.Frame(self.mainFrame, bg=self.light_blue, height=120)
        self.header_frame.pack(fill=tk.X)
        
        # Content frame
        self.content_frame = tk.Frame(self.mainFrame, bg=self.cream)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

    def displayBook(self):
        cek = True
        i = 0
        count = 0

        while cek:
            for j in range(4):  # 4 columns
                if count < self.total_books:
                    book_id = count + 1
                    book = Book(book_id, f"Buku #{book_id}")
                    self.createBookButton(book, i, j)
                    count += 1
                else:
                    cek = False
                    break
            i += 1

    def createBookButton(self, book, row, col):
        bookFrame = tk.Frame(self.book_frame, padx=5, pady=5, bg=self.cream)
        bookFrame.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)
        

        photo = self.load_image()
        self.photo_references[book.get_id()] = photo
        
        # Button with cover image
        btn = tk.Button(
            book_frame, 
            image=photo, 
            text=book.get_title(),
            compound=tk.BOTTOM,
            width=110,
            height=180,
            wraplength=100,
            bg=self.cream,
            relief=tk.FLAT,
            borderwidth=0,
            highlightthickness=0
        )
        btn.pack(fill=tk.BOTH, expand=True)
        
        # Add handler
        btn.configure(command=lambda b=book: self.on_book_click(b))
        
        # Binding scroll on button too
        btn.bind("<MouseWheel>", self.on_mousewheel)
        btn.bind("<Button-4>", self.on_mousewheel)
        btn.bind("<Button-5>", self.on_mousewheel)

if __name__ == "__main__":
    root = tk.Tk()
    app = HomeFrame(root)
    
    # Add escape key binding to exit fullscreen mode
    root.bind("<Escape>", lambda event: root.destroy())
    
    root.mainloop()