import tkinter as tk
import tkinter.ttk as ttk

import util.util_images
from util import util_images


def center_frame(window, width, height):
    window_width = window.winfo_screenwidth()
    window_height = window.winfo_screenheight()
    x = (window_width - width) // 2
    y = (window_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


def crear_barra_busqueda(parent):
    # Crear el frame
    frame = tk.Frame(parent, bg="white")
    frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

    # Crear el entry
    entry = tk.Entry(frame, bg="white", fg="black", font=("Arial", 12))
    entry.place(x=10, y=10, width=400, height=30)

    # Crear el botón de búsqueda
    search_logo = util_images.read_image("image/search.png", (20, 20))
    search_button = tk.Button(frame, image=search_logo, bg="white", bd=0, command=lambda: print("Buscar"))
    search_button.place(x=420, y=10, width=30, height=30)

    return entry
