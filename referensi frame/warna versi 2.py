import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw  # Perlu menginstal pillow: pip install pillow

class MenuWithImagesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi dengan Menubar dan Gambar")
        self.root.geometry("800x600")
        
        # Warna tema (pink)
        self.bg_color = "#FFB6C1"       # Light pink
        self.menu_bg = "#FF69B4"        # Hot pink
        self.menu_fg = "#FFFFFF"        # White text
        self.hover_bg = "#FF1493"       # Deep pink
        
        # Set warna latar belakang aplikasi
        self.root.configure(bg=self.bg_color)
        
        # Membuat frame sebagai menubar custom
        self.custom_menubar = tk.Frame(root, bg=self.menu_bg, height=30)
        self.custom_menubar.pack(side=tk.TOP, fill=tk.X)
        
        # Menyiapkan ikon sederhana menggunakan PIL
        self.create_simple_icons()
        
        # Membuat tombol-tombol menu dengan ikon
        self.create_menu_buttons_with_icons()
        
        # Menambahkan logo di menubar (di sebelah kanan)
        self.add_logo_to_menubar()
        
        # Menambahkan content frame
        self.content_frame = tk.Frame(self.root, bg=self.bg_color)
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Label contoh
        main_label = tk.Label(
            self.content_frame, 
            text="Aplikasi dengan Menubar dan Ikon", 
            font=("Arial", 18, "bold"),
            bg=self.bg_color,
            fg="#8B008B"  # Dark magenta text
        )
        main_label.pack(pady=50)
    
    def create_simple_icons(self):
        """Membuat ikon sederhana menggunakan PIL"""
        # Ukuran ikon
        icon_size = (16, 16)
        logo_size = (24, 24)
        
        # File icon (square)
        file_img = Image.new('RGBA', icon_size, color=(0,0,0,0))
        draw = ImageDraw.Draw(file_img)
        draw.rectangle([2, 2, 14, 14], fill="#FFFFFF")
        self.file_icon = ImageTk.PhotoImage(file_img)
        
        # Edit icon (lines)
        edit_img = Image.new('RGBA', icon_size, color=(0,0,0,0))
        draw = ImageDraw.Draw(edit_img)
        draw.line([4, 12, 12, 4], fill="#FFFFFF", width=2)
        self.edit_icon = ImageTk.PhotoImage(edit_img)
        
        # View icon (circle)
        view_img = Image.new('RGBA', icon_size, color=(0,0,0,0))
        draw = ImageDraw.Draw(view_img)
        draw.ellipse([2, 4, 14, 12], outline="#FFFFFF", width=2)
        self.view_icon = ImageTk.PhotoImage(view_img)
        
        # Help icon (rectangle)
        help_img = Image.new('RGBA', icon_size, color=(0,0,0,0))
        draw = ImageDraw.Draw(help_img)
        draw.rectangle([4, 4, 12, 12], outline="#FFFFFF", width=2)
        self.help_icon = ImageTk.PhotoImage(help_img)
        
        # Logo icon (circle)
        logo_img = Image.new('RGBA', logo_size, color=(0,0,0,0))
        draw = ImageDraw.Draw(logo_img)
        draw.ellipse([2, 2, 22, 22], fill="#FFFFFF")
        self.logo_icon = ImageTk.PhotoImage(logo_img)
        
    def create_menu_buttons_with_icons(self):
        # File menu dengan ikon
        self.file_btn = tk.Menubutton(
            self.custom_menubar, 
            text=" File", 
            image=self.file_icon,
            compound=tk.LEFT,  # Posisi ikon di sebelah kiri teks
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
        
        # Edit menu dengan ikon
        self.edit_btn = tk.Menubutton(
            self.custom_menubar, 
            text=" Edit", 
            image=self.edit_icon,
            compound=tk.LEFT,
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
        
        # View menu dengan ikon
        self.view_btn = tk.Menubutton(
            self.custom_menubar, 
            text=" Tampilan", 
            image=self.view_icon,
            compound=tk.LEFT,
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
        
        # Help menu dengan ikon
        self.help_btn = tk.Menubutton(
            self.custom_menubar, 
            text=" Bantuan", 
            image=self.help_icon,
            compound=tk.LEFT,
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
    
    def add_logo_to_menubar(self):
        """Menambahkan logo di sebelah kanan menubar"""
        # Spacer untuk mendorong logo ke kanan
        spacer = tk.Frame(self.custom_menubar, bg=self.menu_bg)
        spacer.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Logo button di sebelah kanan
        self.logo_btn = tk.Button(
            self.custom_menubar,
            image=self.logo_icon,
            bg=self.menu_bg,
            activebackground=self.hover_bg,
            relief=tk.FLAT,
            padx=5,
            pady=2,
            command=self.show_about
        )
        self.logo_btn.pack(side=tk.RIGHT, padx=10)
        
    def dummy_command(self):
        # Fungsi dummy untuk menu yang belum diimplementasikan
        messagebox.showinfo("Info", "Fitur ini belum diimplementasikan")
        
    def show_help(self):
        messagebox.showinfo("Bantuan", "Ini adalah contoh aplikasi dengan menubar dan ikon menggunakan Tkinter.")
        
    def show_about(self):
        messagebox.showinfo("Tentang", "Aplikasi Menubar dengan Ikon\nVersi 1.0\n© 2025")


if __name__ == "__main__":
    root = tk.Tk()
    app = MenuWithImagesApp(root)
    root.mainloop()