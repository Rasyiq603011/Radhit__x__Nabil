import tkinter as tk
from tkinter import ttk

class RoundedFrame(tk.Canvas):
    def __init__(self, parent, width=300, height=200, corner_radius=20, bg_color="#ffffff", **kwargs):
        super().__init__(parent, width=width, height=height, bg=parent["bg"], 
                         highlightthickness=0, **kwargs)
        self.corner_radius = corner_radius
        self.bg_color = bg_color
        
        # Buat frame dengan sudut tumpul
        self.round_rectangle(0, 0, width, height, self.corner_radius, fill=bg_color, outline="")
        
        # Buat frame untuk konten
        self.content_frame = tk.Frame(self, bg=bg_color)
        self.create_window(width/2, height/2, window=self.content_frame, width=width-corner_radius, 
                           height=height-corner_radius)
    
    def round_rectangle(self, x1, y1, x2, y2, radius, **kwargs):
        """Buat persegi panjang dengan sudut tumpul"""
        points = [
            x1 + radius, y1,          # Top left
            x2 - radius, y1,          # Top right
            x2, y1,
            x2, y1 + radius,
            x2, y2 - radius,          # Bottom right
            x2, y2,
            x2 - radius, y2,
            x1 + radius, y2,          # Bottom left
            x1, y2,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1
        ]
        
        return self.create_polygon(points, smooth=True, **kwargs)

# Contoh penggunaan
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Frame dengan Sudut Tumpul")
    root.geometry("400x300")
    root.configure(bg="#f0f0f0")
    
    # Buat frame dengan sudut tumpul
    rounded_frame = RoundedFrame(root, width=300, height=200, corner_radius=30, bg_color="#e1e1ff")
    rounded_frame.pack(padx=20, pady=20)
    
    # Tambahkan konten ke dalam frame
    label = tk.Label(rounded_frame.content_frame, text="Frame dengan Sudut Tumpul", bg="#e1e1ff")
    label.pack(pady=20)
    
    button = ttk.Button(rounded_frame.content_frame, text="Tombol")
    button.pack(pady=10)
    
    # Contoh lain dengan warna berbeda
    rounded_frame2 = RoundedFrame(root, width=300, height=80, corner_radius=15, bg_color="#ffe1e1")
    rounded_frame2.pack(padx=20, pady=20)
    
    label2 = tk.Label(rounded_frame2.content_frame, text="Frame dengan radius sudut lebih kecil", bg="#ffe1e1")
    label2.pack(pady=20)
    
    root.mainloop()