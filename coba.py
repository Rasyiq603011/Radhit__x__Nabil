import tkinter as tk

class HomeFrame(tk.Frame):
    def __init__(self, master, switch_frame):
        super().__init__(master)
        self.switch_frame = switch_frame
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Ini adalah HomeFrame")
        self.label.pack()

        # Tombol untuk berpindah ke frame lain
        self.switch_button = tk.Button(self, text="Ke Frame Kedua",
                                       command=self.switch_frame)
        self.switch_button.pack()

class SecondFrame(tk.Frame):
    def __init__(self, master, switch_back):
        super().__init__(master)
        self.switch_back = switch_back
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Ini adalah Frame Kedua")
        self.label.pack()

        # Tombol untuk kembali ke HomeFrame
        self.back_button = tk.Button(self, text="Kembali ke HomeFrame",
                                     command=self.switch_back)
        self.back_button.pack()

# Fungsi untuk berpindah antar frame
def show_home():
    global current_frame
    current_frame.pack_forget()
    current_frame = HomeFrame(root, show_second)
    current_frame.pack()

def show_second():
    global current_frame
    current_frame.pack_forget()
    current_frame = SecondFrame(root, show_home)
    current_frame.pack()

# Jendela utama
root = tk.Tk()
root.title("Pergantian Frame")

# Frame pertama yang ditampilkan
current_frame = HomeFrame(root, show_second)
current_frame.pack()

root.mainloop()
