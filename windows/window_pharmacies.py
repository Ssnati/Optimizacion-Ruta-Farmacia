import tkinter as tk
import util.util_images as util_images
import util.util_window as util_window


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

    def agregar_fila(self, valores):
        # Agregar la fila a la lista
        self.lista_filas.append(valores)

        # Actualizar la interfaz gráfica
        for col, valor in enumerate(valores):
            label = tk.Label(self, text=str(valor), padx=10, pady=5)
            label.grid(row=len(self.lista_filas), column=col, sticky=tk.W)

        edit_button = tk.Button(self, image=self.edit_logo, padx=10, pady=5, borderwidth=1, relief="solid",
                                anchor=tk.CENTER,
                                command=lambda: print("Editar"))
        edit_button.grid(row=len(self.lista_filas), column=len(self.columnas), sticky=tk.W)

        delete_button = tk.Button(self, image=self.delete_logo, padx=10, pady=5, borderwidth=1, relief="solid",
                                  anchor=tk.CENTER, command=lambda: print("Eliminar"))
        delete_button.grid(row=len(self.lista_filas), column=len(self.columnas) + 1, sticky=tk.W)
