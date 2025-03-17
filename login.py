import tkinter as tk
from tkinter import ttk

def on_hover(event):
    event.widget.config(
        bg="#FF6666",
        fg="white"
    )  # Warna merah saat hover

def on_leave(event):
    event.widget.config(
        bg="#FF9999",
        fg="black"
    )  # Warna normal

def on_click(event):
    event.widget.config(
        bg="#CC3333",
        fg="white"
    )  # Warna lebih gelap saat ditekan


main = tk.Tk()
main.title("Login")

main.rowconfigure(0, weight=2)
main.rowconfigure(1, weight=8)
main.rowconfigure(2, weight=1)
main.columnconfigure(0, weight=1)

winwidth = 1000
winheight = 800

screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

x_pos = (screen_width // 2) - (winwidth // 2)
y_pos = (screen_height // 2) - (winheight // 2)

main.geometry(f"{winwidth}x{winheight}+{x_pos}+{y_pos}")


frame_header = tk.Frame(
    main,
    bg="#C599B6"
)

frame_header.grid(
    row=0,
    column=0,
    sticky="nsew"
)

titleHead = tk.Label(
    frame_header,
    text="Book-Ku!",
    font=(
        "Comic Sans MS",
        40,
        "bold"
    ),
    fg="#FFF7F3",
    bg="#C599B6"
)

titleHead.pack(
    anchor="center",
    expand=True
)

frame_contents = tk.Frame(
    main,
    bg="#E6B2BA"
)

frame_contents.grid(
    row=1,
    column=0,
    sticky="nsew"
)

frame_login = tk.Frame(
    frame_contents,
    bg="#FAD0C4",
    padx=20,
    pady=20
)

frame_login.pack(
    anchor="center",
    expand=True
)

username = tk.Label(
    frame_login,
    text="Username"
)

username.grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)

inputName = tk.Entry(
    frame_login
)

inputName.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)

password = tk.Label(
    frame_login,
    text="Passoword"
)

password.grid(
    row=1,
    column=0,
    padx=5,
    pady=5
)

inputPass = tk.Entry(
    frame_login,
    show="*"
)

inputPass.grid(
    row=1,
    column=1,
    padx=5,
    pady=5
)


submit = tk.Button(
    frame_login,
    text="Submit"
)

submit.grid(
    row=2,
    columnspan=2
)

submit.bind("<Enter>", on_hover)
submit.bind("<Leave>", on_leave)
submit.bind("<ButtonPress-1>", on_click)
submit.bind("<ButtonRelease-1>", on_hover)


frame_footer = tk.Frame(
    main,
    bg="#C599B6"
)
frame_footer.grid(
    row=2,
    column=0,
    sticky="nsew"
)


main.mainloop()

