import tkinter as tk
from tkinter import messagebox
import platform

class CustomMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi dengan Menubar Cantik")
        self.root.geometry("800x600")
        
        # Warna tema (pink)
        self.bg_color = "#FFB6C1"       # Light pink
        self.menu_bg = "#FF69B4"        # Hot pink
        self.menu_fg = "#FFFFFF"        # White text
        self.hover_bg = "#FF1493"       # Deep pink
        
        # Set warna latar belakang aplikasi
        self.root.configure(bg=self.bg_color)
        
        # TEKNIK KHUSUS: Buat frame sebagai menubar custom
        # Ini adalah cara yang lebih radikal untuk mengganti menubar default
        self.custom_menubar = tk.Frame(root, bg=self.menu_bg, height=30)
        self.custom_menubar.pack(side=tk.TOP, fill=tk.X)
        
        # Membuat tombol-tombol menu
        self.create_menu_buttons()
        
        # Menambahkan content frame
        self.content_frame = tk.Frame(self.root, bg=self.bg_color)
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Label contoh
        main_label = tk.Label(
            self.content_frame, 
            text="Aplikasi dengan Menubar Berwarna Pink", 
            font=("Arial", 18, "bold"),
            bg=self.bg_color,
            fg="#8B008B"  # Dark magenta text
        )
        main_label.pack(pady=50)
        
        # Tombol contoh
        sample_button = tk.Button(
            self.content_frame,
            text="Tombol Contoh",
            bg=self.menu_bg,
            fg=self.menu_fg,
            activebackground=self.hover_bg,
            activeforeground=self.menu_fg,
            relief=tk.RAISED,
            padx=20,
            pady=10,
            font=("Arial", 12)
        )
        sample_button.pack(pady=20)
        
    def create_menu_buttons(self):
        """
        Membuat tombol-tombol menu sebagai pengganti menubar standar
        """
        # Membuat tombol File menu
        self.file_btn = tk.Menubutton(
            self.custom_menubar, 
            text="File", 
            bg=self.menu_bg, 
            fg=self.menu_fg,
            activebackground=self.hover_bg,
            activeforeground=self.menu_fg,
            relief=tk.FLAT,
            padx=10,
            pady=5
        )
        self.file_btn.pack(side=tk.LEFT)
        
        # Membuat menu dropdown untuk File
        self.file_menu = tk.Menu(
            self.file_btn, 
            tearoff=0, 
            bg=self.menu_bg, 
            fg=self.menu_fg,
            activebackground=self.hover_bg, 
            activeforeground=self.menu_fg
        )
        self.file_menu.add_command(label="Baru", command=self.dummy_command)
        self.file_menu.add_command(label="Buka", command=self.dummy_command)
        self.file_menu.add_command(label="Simpan", command=self.dummy_command)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Keluar", command=self.root.quit)
        
        # Menghubungkan dropdown ke tombol
        self.file_btn["menu"] = self.file_menu
        
        # Membuat tombol Edit menu
        self.edit_btn = tk.Menubutton(
            self.custom_menubar, 
            text="Edit", 
            bg=self.menu_bg, 
            fg=self.menu_fg,
            activebackground=self.hover_bg,
            activeforeground=self.menu_fg,
            relief=tk.FLAT,
            padx=10,
            pady=5
        )
        self.edit_btn.pack(side=tk.LEFT)
        
        # Membuat menu dropdown untuk Edit
        self.edit_menu = tk.Menu(
            self.edit_btn, 
            tearoff=0, 
            bg=self.menu_bg, 
            fg=self.menu_fg,
            activebackground=self.hover_bg, 
            activeforeground=self.menu_fg
        )
        self.edit_menu.add_command(label="Potong", command=self.dummy_command)
        self.edit_menu.add_command(label="Salin", command=self.dummy_command)
        self.edit_menu.add_command(label="Tempel", command=self.dummy_command)
        
        # Menghubungkan dropdown ke tombol
        self.edit_btn["menu"] = self.edit_menu
        
        # Membuat tombol Tampilan menu
        self.view_btn = tk.Menubutton(
            self.custom_menubar, 
            text="Tampilan", 
            bg=self.menu_bg, 
            fg=self.menu_fg,
            activebackground=self.hover_bg,
            activeforeground=self.menu_fg,
            relief=tk.FLAT,
            padx=10,
            pady=5
        )
        self.view_btn.pack(side=tk.LEFT)
        
        # Membuat menu dropdown untuk Tampilan
        self.view_menu = tk.Menu(
            self.view_btn, 
            tearoff=0, 
            bg=self.menu_bg, 
            fg=self.menu_fg,
            activebackground=self.hover_bg, 
            activeforeground=self.menu_fg
        )
        self.view_menu.add_command(label="Zoom In", command=self.dummy_command)
        self.view_menu.add_command(label="Zoom Out", command=self.dummy_command)
        self.view_menu.add_command(label="Tampilan Normal", command=self.dummy_command)
        
        # Menghubungkan dropdown ke tombol
        self.view_btn["menu"] = self.view_menu
        
        # Membuat tombol Bantuan menu
        self.help_btn = tk.Menubutton(
            self.custom_menubar, 
            text="Bantuan", 
            bg=self.menu_bg, 
            fg=self.menu_fg,
            activebackground=self.hover_bg,
            activeforeground=self.menu_fg,
            relief=tk.FLAT,
            padx=10,
            pady=5
        )
        self.help_btn.pack(side=tk.LEFT)
        
        # Membuat menu dropdown untuk Bantuan
        self.help_menu = tk.Menu(
            self.help_btn, 
            tearoff=0, 
            bg=self.menu_bg, 
            fg=self.menu_fg,
            activebackground=self.hover_bg, 
            activeforeground=self.menu_fg
        )
        self.help_menu.add_command(label="Bantuan", command=self.show_help)
        self.help_menu.add_command(label="Tentang", command=self.show_about)
        
        # Menghubungkan dropdown ke tombol
        self.help_btn["menu"] = self.help_menu
        
    def dummy_command(self):
        # Fungsi dummy untuk menu yang belum diimplementasikan
        messagebox.showinfo("Info", "Fitur ini belum diimplementasikan")
        
    def show_help(self):
        messagebox.showinfo("Bantuan", "Ini adalah contoh aplikasi dengan menubar berwarna pink menggunakan Tkinter.")
        
    def show_about(self):
        messagebox.showinfo("Tentang", "Aplikasi Menubar Cantik\nVersi 1.0\n© 2025")


if __name__ == "__main__":
    root = tk.Tk()
    
    # Sembunyikan menubar asli
    # Menggunakan pendekatan yang lebih kompatibel dengan Windows
    # Tidak menggunakan menubar standar Tkinter sama sekali
        
    app = CustomMenuApp(root)
    root.mainloop()