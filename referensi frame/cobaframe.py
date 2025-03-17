import pandas as pd
import os
import tkinter as tk
from tkinter import ttk, messagebox

FILE_NAME = "data_buku.xlsx"

class BookManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Aplikasi Manajemen Buku")
        self.geometry("800x600")
        self.resizable(True, True)
        
        # Ensure the file exists
        self.buat_file()
        
        # Container untuk semua frame
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        # Dictionary untuk menyimpan semua frame
        self.frames = {}
        
        # Buat dan inisialisasi frame-frame
        self.create_frames()
        
        # Tampilkan frame utama (HomeFrame) pertama kali
        self.show_frame("HomeFrame")
    
    def create_frames(self):
        """Buat semua frame yang dibutuhkan aplikasi"""
        # Daftar semua kelas frame yang akan digunakan
        frame_classes = (HomeFrame, ViewBooksFrame, AddBookFrame, UpdateBookFrame)
        
        # Inisialisasi setiap frame
        for F in frame_classes:
            frame_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[frame_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
    
    def show_frame(self, frame_name):
        """Menampilkan frame tertentu ke depan"""
        frame = self.frames[frame_name]
        frame.tkraise()
        
        # Perbarui data jika perlu
        if hasattr(frame, "on_show_frame"):
            frame.on_show_frame()
    
    def refresh_all_frames(self):
        """Memperbarui data di semua frame"""
        for frame_name, frame in self.frames.items():
            if hasattr(frame, "refresh_data"):
                frame.refresh_data()
    
    def buat_file(self):
        """Fungsi untuk membuat file XLSX jika belum ada"""
        if not os.path.exists(FILE_NAME):
            df = pd.DataFrame(columns=["ID", "Judul", "Penulis", "Tahun"])
            df.to_excel(FILE_NAME, index=False)


class HomeFrame(tk.Frame):
    """Frame utama dengan menu navigasi"""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Header
        header_frame = tk.Frame(self, bg="#3498db", height=100)
        header_frame.pack(fill="x", pady=10)
        
        tk.Label(
            header_frame, 
            text="SISTEM MANAJEMEN BUKU", 
            font=("Arial", 24, "bold"),
            bg="#3498db",
            fg="white"
        ).pack(pady=25)
        
        # Main content
        main_frame = tk.Frame(self)
        main_frame.pack(fill="both", expand=True, padx=50, pady=30)
        
        # Menu buttons with icons (using text as placeholders for icons)
        button_width = 25
        button_height = 3
        button_font = ("Arial", 12)
        
        # Lihat Buku Button
        view_button = tk.Button(
            main_frame,
            text="📚 Lihat Data Buku",
            font=button_font,
            width=button_width,
            height=button_height,
            bg="#2ecc71",
            fg="white",
            command=lambda: controller.show_frame("ViewBooksFrame")
        )
        view_button.pack(pady=10)
        
        # Tambah Buku Button
        add_button = tk.Button(
            main_frame,
            text="➕ Tambah Buku Baru",
            font=button_font,
            width=button_width,
            height=button_height,
            bg="#3498db",
            fg="white",
            command=lambda: controller.show_frame("AddBookFrame")
        )
        add_button.pack(pady=10)
        
        # Update Buku Button
        update_button = tk.Button(
            main_frame,
            text="🔄 Update Data Buku",
            font=button_font,
            width=button_width,
            height=button_height,
            bg="#f39c12",
            fg="white",
            command=lambda: controller.show_frame("UpdateBookFrame")
        )
        update_button.pack(pady=10)
        
        # Footer
        footer_frame = tk.Frame(self, bg="#34495e", height=50)
        footer_frame.pack(fill="x", side="bottom")
        
        tk.Label(
            footer_frame,
            text="© 2025 Sistem Manajemen Perpustakaan",
            font=("Arial", 10),
            bg="#34495e",
            fg="white"
        ).pack(pady=15)


class ViewBooksFrame(tk.Frame):
    """Frame untuk melihat dan menghapus data buku"""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Header
        tk.Label(
            self, 
            text="Daftar Buku", 
            font=("Arial", 16, "bold")
        ).pack(pady=10)
        
        # Back button (top left)
        back_button = tk.Button(
            self,
            text="← Kembali",
            command=lambda: controller.show_frame("HomeFrame")
        )
        back_button.place(x=10, y=10)
        
        # Frame for book data display
        self.data_frame = ttk.LabelFrame(self, text="Data Buku")
        self.data_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Treeview to display book data
        self.tree = ttk.Treeview(self.data_frame, columns=("ID", "Judul", "Penulis", "Tahun"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Judul", text="Judul")
        self.tree.heading("Penulis", text="Penulis")
        self.tree.heading("Tahun", text="Tahun")
        
        # Column widths
        self.tree.column("ID", width=50)
        self.tree.column("Judul", width=200)
        self.tree.column("Penulis", width=150)
        self.tree.column("Tahun", width=100)
        
        # Scrollbar for the treeview
        scrollbar = ttk.Scrollbar(self.data_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Place the treeview and scrollbar
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Action buttons
        action_frame = ttk.Frame(self)
        action_frame.pack(fill="x", padx=10, pady=10)
        
        ttk.Button(
            action_frame, 
            text="Refresh Data", 
            command=self.refresh_data
        ).pack(side="left", padx=5)
        
        ttk.Button(
            action_frame, 
            text="Edit Buku", 
            command=self.edit_selected_book
        ).pack(side="left", padx=5)
        
        ttk.Button(
            action_frame, 
            text="Hapus Buku", 
            command=self.hapus_buku
        ).pack(side="left", padx=5)
    
    def on_show_frame(self):
        """Dipanggil saat frame ini ditampilkan"""
        self.refresh_data()
    
    def refresh_data(self):
        """Fungsi untuk membaca data dan menampilkan di treeview"""
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Read data from file
        try:
            df = pd.read_excel(FILE_NAME)
            
            # Insert data to treeview
            for _, row in df.iterrows():
                self.tree.insert("", "end", values=(row["ID"], row["Judul"], row["Penulis"], row["Tahun"]))
        except Exception as e:
            messagebox.showerror("Error", f"Gagal membaca data: {str(e)}")
    
    def edit_selected_book(self):
        """Pergi ke frame update dengan buku yang dipilih"""
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showwarning("Peringatan", "Pilih buku yang ingin diedit!")
            return
        
        # Get data from selected item
        item = selected_items[0]
        values = self.tree.item(item, "values")
        
        # Pass the data to the update frame
        update_frame = self.controller.frames["UpdateBookFrame"]
        update_frame.populate_fields(values)
        
        # Show the update frame
        self.controller.show_frame("UpdateBookFrame")
    
    def hapus_buku(self):
        """Fungsi untuk menghapus buku"""
        # Check if an item is selected
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showwarning("Peringatan", "Pilih buku yang ingin dihapus!")
            return
        
        # Get ID from the selected item
        item = selected_items[0]
        values = self.tree.item(item, "values")
        id_buku = int(values[0])
        
        # Confirm deletion
        confirm = messagebox.askyesno("Konfirmasi", f"Yakin ingin menghapus buku dengan ID {id_buku}?")
        if not confirm:
            return
        
        try:
            # Read current data
            df = pd.read_excel(FILE_NAME)
            
            # Remove the book
            if id_buku in df["ID"].values:
                df = df[df["ID"] != id_buku]
                df.to_excel(FILE_NAME, index=False)
                
                # Refresh all frames
                self.controller.refresh_all_frames()
                
                messagebox.showinfo("Sukses", "Buku berhasil dihapus!")
            else:
                messagebox.showwarning("Peringatan", "ID buku tidak ditemukan.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menghapus data: {str(e)}")


class AddBookFrame(tk.Frame):
    """Frame untuk menambah buku baru"""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Header
        tk.Label(
            self, 
            text="Tambah Buku Baru", 
            font=("Arial", 16, "bold")
        ).pack(pady=10)
        
        # Back button (top left)
        back_button = tk.Button(
            self,
            text="← Kembali",
            command=lambda: controller.show_frame("HomeFrame")
        )
        back_button.place(x=10, y=10)
        
        # Main form
        form_frame = ttk.LabelFrame(self, text="Data Buku Baru")
        form_frame.pack(fill="both", expand=True, padx=50, pady=30)
        
        # Form fields
        # Using grid for better alignment
        padx = 10
        pady = 10
        
        # Judul
        ttk.Label(form_frame, text="Judul Buku:").grid(row=0, column=0, sticky="w", padx=padx, pady=pady)
        self.judul_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.judul_var, width=50).grid(row=0, column=1, padx=padx, pady=pady)
        
        # Penulis
        ttk.Label(form_frame, text="Penulis:").grid(row=1, column=0, sticky="w", padx=padx, pady=pady)
        self.penulis_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.penulis_var, width=50).grid(row=1, column=1, padx=padx, pady=pady)
        
        # Tahun
        ttk.Label(form_frame, text="Tahun Terbit:").grid(row=2, column=0, sticky="w", padx=padx, pady=pady)
        self.tahun_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.tahun_var, width=50).grid(row=2, column=1, padx=padx, pady=pady)
        
        # Button frame
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Save button
        save_button = ttk.Button(
            button_frame,
            text="Simpan Data",
            command=self.tambah_buku
        )
        save_button.pack(side="left", padx=5)
        
        # Clear button
        clear_button = ttk.Button(
            button_frame,
            text="Bersihkan Form",
            command=self.clear_form
        )
        clear_button.pack(side="left", padx=5)
    
    def on_show_frame(self):
        """Dipanggil saat frame ini ditampilkan"""
        # Bersihkan form saat frame ditampilkan
        self.clear_form()
    
    def clear_form(self):
        """Bersihkan semua field"""
        self.judul_var.set("")
        self.penulis_var.set("")
        self.tahun_var.set("")
    
    def tambah_buku(self):
        """Fungsi untuk menambah buku baru"""
        judul = self.judul_var.get().strip()
        penulis = self.penulis_var.get().strip()
        tahun = self.tahun_var.get().strip()
        
        # Validation
        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return
        
        try:
            # Read current data
            df = pd.read_excel(FILE_NAME)
            
            # Create new ID
            id_baru = 1 if df.empty else int(df["ID"].max()) + 1
            
            # Add new book
            df = pd.concat([df, pd.DataFrame({"ID": [id_baru], "Judul": [judul], "Penulis": [penulis], "Tahun": [tahun]})], ignore_index=True)
            df.to_excel(FILE_NAME, index=False)
            
            # Clear form
            self.clear_form()
            
            # Refresh all frames
            self.controller.refresh_all_frames()
            
            messagebox.showinfo("Sukses", "Buku berhasil ditambahkan!")
            
            # Option to add another or go back to home
            if messagebox.askyesno("Tambah Lagi?", "Ingin menambahkan buku lain?"):
                # Stay on this form
                pass
            else:
                # Go back to home
                self.controller.show_frame("HomeFrame")
                
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menambah data: {str(e)}")


class UpdateBookFrame(tk.Frame):
    """Frame untuk mengupdate buku"""
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Header
        tk.Label(
            self, 
            text="Update Data Buku", 
            font=("Arial", 16, "bold")
        ).pack(pady=10)
        
        # Back button (top left)
        back_button = tk.Button(
            self,
            text="← Kembali",
            command=lambda: controller.show_frame("ViewBooksFrame")
        )
        back_button.place(x=10, y=10)
        
        # Main form
        form_frame = ttk.LabelFrame(self, text="Edit Data Buku")
        form_frame.pack(fill="both", expand=True, padx=50, pady=30)
        
        # Form fields
        # Using grid for better alignment
        padx = 10
        pady = 10
        
        # ID (hidden/readonly)
        ttk.Label(form_frame, text="ID Buku:").grid(row=0, column=0, sticky="w", padx=padx, pady=pady)
        self.id_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.id_var, width=50, state="readonly").grid(row=0, column=1, padx=padx, pady=pady)
        
        # Judul
        ttk.Label(form_frame, text="Judul Buku:").grid(row=1, column=0, sticky="w", padx=padx, pady=pady)
        self.judul_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.judul_var, width=50).grid(row=1, column=1, padx=padx, pady=pady)
        
        # Penulis
        ttk.Label(form_frame, text="Penulis:").grid(row=2, column=0, sticky="w", padx=padx, pady=pady)
        self.penulis_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.penulis_var, width=50).grid(row=2, column=1, padx=padx, pady=pady)
        
        # Tahun
        ttk.Label(form_frame, text="Tahun Terbit:").grid(row=3, column=0, sticky="w", padx=padx, pady=pady)
        self.tahun_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.tahun_var, width=50).grid(row=3, column=1, padx=padx, pady=pady)
        
        # Button frame
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=20)
        
        # Update button
        update_button = ttk.Button(
            button_frame,
            text="Update Data",
            command=self.update_buku
        )
        update_button.pack(side="left", padx=5)
        
        # View All button
        view_button = ttk.Button(
            button_frame,
            text="Lihat Semua Buku",
            command=lambda: controller.show_frame("ViewBooksFrame")
        )
        view_button.pack(side="left", padx=5)
    
    def populate_fields(self, values):
        """Isi form dengan data buku yang dipilih"""
        self.id_var.set(values[0])
        self.judul_var.set(values[1])
        self.penulis_var.set(values[2])
        self.tahun_var.set(values[3])
    
    def on_show_frame(self):
        """Dipanggil saat frame ditampilkan"""
        # Jika tidak ada data yang diisi (misal dari home langsung ke update)
        # Maka tampilkan dialog untuk memilih buku dari daftar
        if not self.id_var.get():
            messagebox.showinfo("Pilih Buku", "Silakan pilih buku dari daftar untuk diupdate.")
            self.controller.show_frame("ViewBooksFrame")
    
    def update_buku(self):
        """Fungsi untuk mengupdate data buku"""
        id_buku = self.id_var.get()
        judul = self.judul_var.get().strip()
        penulis = self.penulis_var.get().strip()
        tahun = self.tahun_var.get().strip()
        
        # Validation
        if not id_buku or not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return
        
        try:
            # Read current data
            df = pd.read_excel(FILE_NAME)
            
            # Find and update the book
            id_buku = int(id_buku)
            if id_buku in df["ID"].values:
                df.loc[df["ID"] == id_buku, ["Judul", "Penulis", "Tahun"]] = [judul, penulis, tahun]
                df.to_excel(FILE_NAME, index=False)
                
                # Refresh all frames
                self.controller.refresh_all_frames()
                
                messagebox.showinfo("Sukses", "Buku berhasil diupdate!")
                
                # Go back to view books
                self.controller.show_frame("ViewBooksFrame")
            else:
                messagebox.showwarning("Peringatan", "ID buku tidak ditemukan.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mengupdate data: {str(e)}")


# Main function to run the app
def main():
    app = BookManagerApp()
    app.mainloop()

if __name__ == "__main__":
    main()