import tkinter as tk
from tkinter import ttk, Menu  # Menu dari tk

root = tk.Tk()
root.title("Demo Tkinter")
root.geometry("400x400")

# Menggunakan ttk untuk sebagian besar widget UI
frame = ttk.Frame(root, padding="10", relief="raised")
frame.pack(fill=tk.BOTH, expand=True)  # Penting: Frame harus di-pack!

label = ttk.Label(frame, text="Nama:")
label.pack(anchor=tk.W, pady=5)  # Widget harus di-pack!

entry = ttk.Entry(frame)
entry.pack(fill=tk.X, pady=5)  # Widget harus di-pack!

button = ttk.Button(frame, text="Simpan")
button.pack(pady=5)  # Widget harus di-pack!

# Menggunakan tk untuk widget khusus
canvas = tk.Canvas(root, width=300, height=200, bg="lightgray")
canvas.create_line(0, 0, 300, 200, fill="red", width=2)
canvas.create_rectangle(50, 50, 250, 150, fill="blue", outline="white")
canvas.pack(pady=10)  # Canvas harus di-pack!

# Cara yang benar untuk membuat menu
menubar = Menu(root)

# Membuat menu dropdown File
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Baru")
file_menu.add_command(label="Buka")
file_menu.add_command(label="Simpan")
file_menu.add_separator()
file_menu.add_command(label="Keluar", command=root.destroy)
file_menu.config(bg="lightgray", fg="black")
menubar.add_cascade(label="File", menu=file_menu)  # Menu utama dengan submenu

# Membuat menu dropdown Edit
edit_menu = Menu(menubar, tearoff=0)
edit_menu.add_command(label="Potong")
edit_menu.add_command(label="Salin")
edit_menu.add_command(label="Tempel")
menubar.add_cascade(label="Edit", menu=edit_menu)  # Menu utama dengan submenu

# Membuat menu dropdown Help
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="Tentang", command=lambda: tk.messagebox.showinfo("Tentang", "Demo Aplikasi Tkinter\nVersi 1.0"))
menubar.add_cascade(label="Help", menu=help_menu)  # Menu utama dengan submenu

# Memasang menu ke window (cara yang benar)
root.config(menu=menubar)

root.mainloop()