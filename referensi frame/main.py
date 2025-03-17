import tkinter as tk
from tkinter import ttk, messagebox, Menu
from tkinter import filedialog

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Cobaaa")
        self.geometry("800x600")
        
        # Variabel untuk menyimpan data
        self.nama_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.gender_var = tk.StringVar(value="Laki-laki")
        
        # Membuat menu dan widgets
        self.create_menu()
        self.create_widgets()
        
    def create_menu(self):
        # Membuat menu bar
        self.menubar = Menu(self)
        
        # Menu File
        file_menu = Menu(self.menubar, tearoff=0)
        file_menu.add_command(label="Baru", command=self.file_baru)
        file_menu.add_command(label="Buka", command=self.file_buka)
        file_menu.add_command(label="Simpan", command=self.file_simpan)
        file_menu.add_separator()
        file_menu.add_command(label="Keluar", command=self.keluar)
        self.menubar.add_cascade(label="File", menu=file_menu)
        
        # Menu Bantuan
        help_menu = Menu(self.menubar, tearoff=0)
        help_menu.add_command(label="Tentang", command=self.tentang)
        self.menubar.add_cascade(label="Bantuan", menu=help_menu)
        
        # Pasang menu ke window
        self.config(menu=self.menubar)
    
    def create_widgets(self):
        # Frame Utama
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Frame Kiri - Form Input
        left_frame = ttk.LabelFrame(main_frame, text="Input Data", padding="10")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Nama
        ttk.Label(left_frame, text="Nama:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(left_frame, textvariable=self.nama_var, width=30).grid(row=0, column=1, sticky=tk.W, pady=5)
        
        # Email
        ttk.Label(left_frame, text="Email:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Entry(left_frame, textvariable=self.email_var, width=30).grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # Gender
        ttk.Label(left_frame, text="Gender:").grid(row=2, column=0, sticky=tk.W, pady=5)
        gender_frame = ttk.Frame(left_frame)
        gender_frame.grid(row=2, column=1, sticky=tk.W, pady=5)
        
        ttk.Radiobutton(gender_frame, text="Laki-laki", variable=self.gender_var, value="Laki-laki").pack(side=tk.LEFT)
        ttk.Radiobutton(gender_frame, text="Perempuan", variable=self.gender_var, value="Perempuan").pack(side=tk.LEFT)
        
        # Hobi
        ttk.Label(left_frame, text="Hobi:").grid(row=3, column=0, sticky=tk.W, pady=5)
        hobi_frame = ttk.Frame(left_frame)
        hobi_frame.grid(row=3, column=1, sticky=tk.W, pady=5)
        
        self.hobi_baca = tk.BooleanVar()
        self.hobi_musik = tk.BooleanVar()
        self.hobi_olahraga = tk.BooleanVar()
        
        ttk.Checkbutton(hobi_frame, text="Membaca", variable=self.hobi_baca).pack(anchor=tk.W)
        ttk.Checkbutton(hobi_frame, text="Musik", variable=self.hobi_musik).pack(anchor=tk.W)
        ttk.Checkbutton(hobi_frame, text="Olahraga", variable=self.hobi_olahraga).pack(anchor=tk.W)
        
        # Deskripsi
        ttk.Label(left_frame, text="Deskripsi:").grid(row=4, column=0, sticky=tk.NW, pady=5)
        self.deskripsi_text = tk.Text(left_frame, width=30, height=5)
        self.deskripsi_text.grid(row=4, column=1, sticky=tk.W, pady=5)
        
        # Tombol
        button_frame = ttk.Frame(left_frame)
        button_frame.grid(row=5, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Simpan", command=self.simpan_data).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Reset", command=self.reset_form).pack(side=tk.LEFT, padx=5)
        
        # Frame Kanan - Daftar dan Hasil
        right_frame = ttk.LabelFrame(main_frame, text="Daftar & Hasil", padding="10")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Treeview untuk menampilkan data
        self.tree = ttk.Treeview(right_frame, columns=("nama", "email", "gender"), show="headings")
        self.tree.heading("nama", text="Nama")
        self.tree.heading("email", text="Email")
        self.tree.heading("gender", text="Gender")
        self.tree.column("nama", width=100)
        self.tree.column("email", width=150)
        self.tree.column("gender", width=80)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Status bar
        self.statusbar = ttk.Label(self, text="Siap", relief=tk.SUNKEN, anchor=tk.W)
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)
    
    # Fungsi-fungsi menu File
    def file_baru(self):
        self.reset_form()
        messagebox.showinfo("Informasi", "Dokumen baru telah dibuat")
        
    def file_buka(self):
        filename = filedialog.askopenfilename(
            title="Buka File",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filename:
            self.statusbar.config(text=f"File dibuka: {filename}")
            
    def file_simpan(self):
        filename = filedialog.asksaveasfilename(
            title="Simpan File",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filename:
            self.statusbar.config(text=f"File disimpan: {filename}")
    
    def keluar(self):
        if messagebox.askokcancel("Keluar", "Yakin ingin keluar?"):
            self.destroy()
    
    def tentang(self):
        messagebox.showinfo("Tentang", "Aplikasi Demo Tkinter\nVersi 1.0\n© 2025")
    
    # Fungsi-fungsi untuk form
    def simpan_data(self):
        nama = self.nama_var.get()
        email = self.email_var.get()
        gender = self.gender_var.get()
        
        if not nama or not email:
            messagebox.showerror("Error", "Nama dan email harus diisi!")
            return
        
        # Tambahkan data ke treeview
        self.tree.insert("", tk.END, values=(nama, email, gender))
        
        # Update status
        self.statusbar.config(text=f"Data untuk {nama} telah disimpan")
        
        # Opsional: Reset form setelah simpan
        self.reset_form()
        
    def reset_form(self):
        self.nama_var.set("")
        self.email_var.set("")
        self.gender_var.set("Laki-laki")
        self.hobi_baca.set(False)
        self.hobi_musik.set(False)
        self.hobi_olahraga.set(False)
        self.deskripsi_text.delete("1.0", tk.END)
        self.statusbar.config(text="Form direset")

# Menjalankan aplikasi
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()