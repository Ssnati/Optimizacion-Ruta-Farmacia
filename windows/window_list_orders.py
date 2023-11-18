import tkinter as tk
from tkinter import ttk
import config
from util import util_images


class ListaPedidosFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg="white")
        self.crear_interfaz()

    def crear_interfaz(self):
        # Titulo
        titulo_label = tk.Label(self, text="Lista de Pedidos", font=("Arial", 16), bg="white", fg="black",
                                anchor=tk.CENTER)
        titulo_label.grid(row=0, column=0, columnspan=4, pady=(10, 0), sticky="n")

        # Lista desplegable para elegir una farmacia
        farmacia_label = tk.Label(self, text="Elegir Farmacia:", bg="white")
        farmacia_label.grid(row=1, column=1, sticky="e", pady=(10, 5))
        farmacia_dropdown = ttk.Combobox(self, values=["Farmacia 1", "Farmacia 2", "Farmacia 3"])
        farmacia_dropdown.grid(row=1, column=2, pady=(10, 5), sticky="w")

        # Lista desplegable para elegir un producto
        producto_label = tk.Label(self, text="Elegir Producto:", bg="white")
        producto_label.grid(row=2, column=1, sticky="e", pady=5)
        producto_dropdown = ttk.Combobox(self, values=["Producto 1", "Producto 2", "Producto 3"])
        producto_dropdown.grid(row=2, column=2, pady=5, sticky="w")

        # Boton para agregar el pedido
        agregar_button = tk.Button(self, text="Agregar Pedido", command=self.agregar_pedido, bg=config.COLOR_SECUNDARIO)
        agregar_button.grid(row=3, column=1, columnspan=2, pady=(5, 10))

        # Panel con la lista de entregas
        self.tv_frame = tk.Frame(self, bg="red")
        self.tv_frame.grid(row=1, column=3, rowspan=3, pady=(10, 0), sticky="w")

        self.create_order_panel()

    def agregar_pedido(self):
        # Lógica para agregar el pedido
        print("Pedido agregado")

    def create_order_panel(self):
        # Crear una lista de pedidos
        pedidos = [
            {"farmacia": "Farmacia 1", "producto": "Producto A"},
            {"farmacia": "Farmacia 2", "producto": "Producto B"},
            {"farmacia": "Farmacia 2", "producto": "Producto B"},
            {"farmacia": "Farmacia 2", "producto": "Producto B"},
            {"farmacia": "Farmacia 2", "producto": "Producto B"},
            {"farmacia": "Farmacia 2", "producto": "Producto B"},
            {"farmacia": "Farmacia 2", "producto": "Producto B"},
            {"farmacia": "Farmacia 2", "producto": "Producto B"},
            {"farmacia": "Farmacia 2", "producto": "Producto B"},
            {"farmacia": "Farmacia 2", "producto": "Producto B"},
            {"farmacia": "Farmacia 2", "producto": "Producto B"},
            {"farmacia": "Farmacia 2", "producto": "Producto B"},
            {"farmacia": "Farmacia 2", "producto": "Producto B"},
            {"farmacia": "Farmacia 2", "producto": "Producto B"},
            {"farmacia": "Farmacia 2", "producto": "Producto B"},
            {"farmacia": "Farmacia 2", "producto": "Producto B"},
            {"farmacia": "Farmacia 2", "producto": "Producto B"},
            {"farmacia": "Farmacia 2", "producto": "Producto B"},
            {"farmacia": "Farmacia 2", "producto": "Producto B"},
            {"farmacia": "Farmacia 3", "producto": "Producto C"},
        ]

        self.tv = ttk.Treeview(self.tv_frame, columns=("Farmacia"), show="headings", height=10)
        self.tv.column("Farmacia", minwidth=0, width=100, stretch=tk.NO)
        self.tv.heading("Farmacia", text="Farmacia")
        self.tv.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Agregar un evento al hacer clic en una fila
        for pedido in pedidos:
            self.tv.insert("", tk.END, values=[pedido["farmacia"]])
        self.tv.bind("<ButtonRelease-1>", self.on_tree_click)

        scroll = tk.Scrollbar(self.tv_frame, orient=tk.VERTICAL, command=self.tv.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tv.configure(yscrollcommand=scroll.set)

    def on_tree_click(self):
        # Obtener la fila seleccionada
        selected_item = self.tv.selection()
        if selected_item:
            # Obtener los valores de la fila seleccionada
            values = self.tv.item(selected_item)['values']
            if values:
                print("Farmacia seleccionada:", values[0], "Indice:", selected_item)
            else:
                print("No hay valores seleccionados en la fila.")