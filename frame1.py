import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry("800x600")

frame = tk.Frame(root)
frame.pack(fill="both", expand = True)

frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=6) 
frame.grid_rowconfigure(2, weight=1)
frame.grid_columnconfigure(0, weight=1)

frame_header = tk.Frame(frame,bg="#4C0086")
frame_header.grid(row=0, column= 0, sticky="nsew")

frame_content = tk.Frame(frame,bg="#FF0000")
frame_content.grid(row=1, column=0, sticky="nsew")

frame_footer = tk.Frame(frame,bg="#4C0086")
frame_footer.grid(row=2, column=0, sticky="nsew")

frame_login = tk.Frame(frame_content, bg="#4C0086", height= 300, width= 400)
frame_login.pack(anchor="center", expand=True, fill=None)

label = tk.Label(frame_login, text= "Username")
label.grid(row= 0, column= 0)

Entry = tk.Entry(frame_login)
Entry.grid(row= 0, column= 1)

label2 = tk.Label(frame_login, text= "password")
label2.grid(row=1, column=0)

Entry2 = tk.Entry(frame_login)
Entry2.grid(row= 1, column= 1)

button = tk.Button(frame_login, text="Login")
button.grid(row=2, columnspan=2 )



root.mainloop()