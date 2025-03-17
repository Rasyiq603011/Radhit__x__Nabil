import pandas as pd
import os
import tkinter as tk
from tkinter import ttk, messagebox

FILE_NAME = "data_buku.xlsx"

class BookManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Manajemen Buku")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Ensure the file exists
        self.buat_file()
        
        # Create UI elements
        self.create_widgets()
        
        # Load initial data
        self.refresh_data()
    
    def create_widgets(self):
        # Frame for book data display
        self.data_frame = ttk.LabelFrame(self.root, text="Data Buku")
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
        
        # Frame for input fields
        self.input_frame = ttk.LabelFrame(self.root, text="Informasi Buku")
        self.input_frame.pack(fill="both", padx=10, pady=10)
        
        # Input fields
        ttk.Label(self.input_frame, text="Judul:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.judul_var = tk.StringVar()
        ttk.Entry(self.input_frame, textvariable=self.judul_var, width=40).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.input_frame, text="Penulis:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.penulis_var = tk.StringVar()
        ttk.Entry(self.input_frame, textvariable=self.penulis_var, width=40).grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self.input_frame, text="Tahun:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.tahun_var = tk.StringVar()
        ttk.Entry(self.input_frame, textvariable=self.tahun_var, width=40).grid(row=2, column=1, padx=5, pady=5)
        
        # ID field (hidden/disabled, only for updates)
        ttk.Label(self.input_frame, text="ID:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.id_var = tk.StringVar()
        self.id_entry = ttk.Entry(self.input_frame, textvariable=self.id_var, width=40, state="disabled")
        self.id_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Buttons frame
        self.buttons_frame = ttk.Frame(self.root)
        self.buttons_frame.pack(fill="both", padx=10, pady=10)
        
        # Buttons
        ttk.Button(self.buttons_frame, text="Tambah Buku", command=self.tambah_buku).pack(side="left", padx=5)
        ttk.Button(self.buttons_frame, text="Update Buku", command=self.prepare_update).pack(side="left", padx=5)
        ttk.Button(self.buttons_frame, text="Hapus Buku", command=self.hapus_buku).pack(side="left", padx=5)
        ttk.Button(self.buttons_frame, text="Refresh Data", command=self.refresh_data).pack(side="left", padx=5)
        ttk.Button(self.buttons_frame, text="Bersihkan Form", command=self.clear_form).pack(side="left", padx=5)
        ttk.Button(self.buttons_frame, text="Keluar", command=self.root.destroy).pack(side="right", padx=5)
        
        # Tree selection event
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
    
    def buat_file(self):
        """Fungsi untuk membuat file XLSX jika belum ada"""
        if not os.path.exists(FILE_NAME):
            df = pd.DataFrame(columns=["ID", "Judul", "Penulis", "Tahun"])
            df.to_excel(FILE_NAME, index=False)
    
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
    
    def clear_form(self):
        """Bersihkan form input"""
        self.judul_var.set("")
        self.penulis_var.set("")
        self.tahun_var.set("")
        self.id_var.set("")
        
        # Deselect any selected item
        for selected_item in self.tree.selection():
            self.tree.selection_remove(selected_item)
    
    def on_tree_select(self, event):
        """Fungsi untuk menangani pemilihan data di treeview"""
        selected_items = self.tree.selection()
        if selected_items:  # If something is selected
            item = selected_items[0]
            values = self.tree.item(item, "values")
            
            # Fill the form with selected data
            self.id_var.set(values[0])
            self.judul_var.set(values[1])
            self.penulis_var.set(values[2])
            self.tahun_var.set(values[3])
    
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
            
            # Update display
            self.refresh_data()
            self.clear_form()
            
            messagebox.showinfo("Sukses", "Buku berhasil ditambahkan!")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menambah data: {str(e)}")
    
    def prepare_update(self):
        """Fungsi untuk mempersiapkan update buku"""
        # Check if an item is selected
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showwarning("Peringatan", "Pilih buku yang ingin diupdate!")
            return
        
        # Item is already selected and form is filled via on_tree_select
        self.update_buku()
    
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
                
                # Update display
                self.refresh_data()
                self.clear_form()
                
                messagebox.showinfo("Sukses", "Buku berhasil diupdate!")
            else:
                messagebox.showwarning("Peringatan", "ID buku tidak ditemukan.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mengupdate data: {str(e)}")
    
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
                
                # Update display
                self.refresh_data()
                self.clear_form()
                
                messagebox.showinfo("Sukses", "Buku berhasil dihapus!")
            else:
                messagebox.showwarning("Peringatan", "ID buku tidak ditemukan.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menghapus data: {str(e)}")

# Main function to run the app
def main():
    root = tk.Tk()
    app = BookManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()