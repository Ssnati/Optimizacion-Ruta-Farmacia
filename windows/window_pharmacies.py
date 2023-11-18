import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Asegúrate de tener Pillow instalado (pip install Pillow)

from util import util_images


class Tabla(tk.Frame):
    def __init__(self, parent, columnas):
        super().__init__(parent)
        self.edit_logo = util_images.read_image("image/create-sharp.png", (20, 20))
        self.delete_logo = util_images.read_image("image/trash-sharp.png", (20, 20))

        self.columnas = columnas
        self.config(bg="white")

        # Contenedor para los botones
        self.botones_frame = tk.Frame(self, bg="white", padx=25, pady=10)
        self.botones_frame.pack(side=tk.TOP, fill=tk.X)

        # Botones de editar y eliminar
        editar_button = tk.Button(self.botones_frame, image=self.edit_logo, command=self.editar_seleccion)
        editar_button.pack(side=tk.RIGHT, padx=50)
        eliminar_button = tk.Button(self.botones_frame, image=self.delete_logo, command=self.eliminar_seleccion)
        eliminar_button.pack(side=tk.LEFT, padx=50)

        # Contenedor para la tabla
        self.tv_frame = tk.Frame(self, bg="white")
        self.tv_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Tabla
        self.tv = ttk.Treeview(self.tv_frame, columns=columnas, show="headings", height=10)

        for col in columnas:
            self.tv.column(col, minwidth=0, width=100, stretch=tk.NO)
            self.tv.heading(col, text=col.title())

        self.tv.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scroll = tk.Scrollbar(self.tv_frame, orient=tk.VERTICAL, command=self.tv.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tv.configure(yscrollcommand=scroll.set)

    def agregar_fila(self, fila):
        self.tv.insert("", tk.END, values=fila)
        self.actualizar_columnas()

    def editar_seleccion(self):
        seleccion = self.tv.selection()
        if seleccion:
            # Obtener la fila seleccionada
            fila_seleccionada = self.tv.item(seleccion)['values']
            print(f"Editar fila: {fila_seleccionada}")

    def eliminar_seleccion(self):
        seleccion = self.tv.selection()
        if seleccion:
            # Obtener la fila seleccionada
            fila_seleccionada = self.tv.item(seleccion)['values']
            print(f"Eliminar fila: {fila_seleccionada}")

    def actualizar_columnas(self):
        for col in self.columnas:
            self.tv.column(col, minwidth=10, width=100, stretch=tk.NO)
            self.tv.heading(col, text=col.title())
