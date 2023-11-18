import tkinter as tk
from functools import partial
from tkinter import simpledialog

from util import util_window, util_images


class Tabla(tk.Frame):
    def __init__(self, parent, columnas):
        super().__init__(parent)
        self.edit_logo = util_images.read_image("image/create-sharp.png", (20, 20))
        self.delete_logo = util_images.read_image("image/trash-sharp.png", (20, 20))
        self.columnas = columnas
        self.config(bg="white")

        for col in columnas:
            header = tk.Button(self, text=col, padx=10, pady=5, borderwidth=1, relief="solid", anchor=tk.CENTER,
                               command=lambda: print("Hola"))
            header.grid(row=0, column=columnas.index(col), sticky=tk.W)
        edit_column = tk.Label(self, text="      ", padx=10, pady=5, borderwidth=1, anchor=tk.CENTER, bg="white")
        edit_column.grid(row=0, column=len(columnas), sticky=tk.W)

        delete_column = tk.Label(self, text="        ", padx=10, pady=5, borderwidth=1, anchor=tk.CENTER, bg="white")
        delete_column.grid(row=0, column=len(columnas) + 1, sticky=tk.W)

        # Lista para almacenar las filas
        self.lista_filas = []

    def edit_popup(self, row):
        # Crear un popup para editar la fila
        popup = tk.Toplevel(self)
        popup.title("Editar")
        popup.geometry("300x100")
        popup.resizable(False, False)
        util_window.center_frame(popup, 300, 100)

        # Crear un entry para ingresar el nuevo valor

        value = simpledialog.askstring("Editar", f"Editar fila {row}", parent=self)
        if value is not None:
            # Actualizar la fila con el nuevo valor
            self.lista_filas[row - 1] = value
            # Actualizar la interfaz gráfica
            self.actualizar_tabla()

    def delete_row(self, row):
        # Crear un popup de confirmación para la eliminación
        result = tk.messagebox.askquestion("Eliminar", f"¿Está seguro de eliminar la fila {row}?", parent=self)
        if result:
            # Eliminar la fila de la lista
            del self.lista_filas[row - 1]
            # Actualizar la interfaz gráfica
            self.actualizar_tabla()

    def agregar_fila(self, valores):
        # Agregar la fila a la lista
        self.lista_filas.append(valores)

        # Actualizar la interfaz gráfica
        for col, valor in enumerate(valores):
            label = tk.Label(self, text=str(valor), padx=10, pady=5)
            label.grid(row=len(self.lista_filas), column=col, sticky=tk.W)

        edit_button = tk.Button(self, image=self.edit_logo, padx=10, pady=5, borderwidth=1, relief="solid",
                                anchor=tk.CENTER, command=partial(self.edit_popup, len(self.lista_filas)))
        edit_button.grid(row=len(self.lista_filas), column=len(self.columnas), sticky=tk.W)

        delete_button = tk.Button(self, image=self.delete_logo, padx=10, pady=5, borderwidth=1, relief="solid",
                                  anchor=tk.CENTER, command=partial(self.delete_row, len(self.lista_filas)))
        delete_button.grid(row=len(self.lista_filas), column=len(self.columnas) + 1, sticky=tk.W)

    def actualizar_tabla(self):
        # Eliminar todos los widgets de la tabla
        for widget in self.winfo_children():
            widget.destroy()

        # Crear los encabezados
        for col in self.columnas:
            header = tk.Label(self, text=col, padx=10, pady=5, borderwidth=1, relief="solid", anchor=tk.CENTER)
            header.grid(row=0, column=self.columnas.index(col), sticky=tk.W)

        edit_column = tk.Label(self, text="      ", padx=10, pady=5, borderwidth=1, anchor=tk.CENTER, bg="white")
        edit_column.grid(row=0, column=len(self.columnas), sticky=tk.W)

        delete_column = tk.Label(self, text="        ", padx=10, pady=5, borderwidth=1, anchor=tk.CENTER, bg="white")
        delete_column.grid(row=0, column=len(self.columnas) + 1, sticky=tk.W)

        # Crear las filas
        for row, fila in enumerate(self.lista_filas):
            for col, valor in enumerate(fila):
                label = tk.Label(self, text=str(valor), padx=10, pady=5)
                label.grid(row=row + 1, column=col, sticky=tk.W)

            edit_button = tk.Button(self, image=self.edit_logo, padx=10, pady=5, borderwidth=1, relief="solid",
                                    anchor=tk.CENTER, command=partial(self.edit_popup, row + 1))
            edit_button.grid(row=row + 1, column=len(self.columnas), sticky=tk.W)

            delete_button = tk.Button(self, image=self.delete_logo, padx=10, pady=5, borderwidth=1, relief="solid",
                                      anchor=tk.CENTER, command=partial(self.delete_row, row + 1))
            delete_button.grid(row=row + 1, column=len(self.columnas) + 1, sticky=tk.W)
