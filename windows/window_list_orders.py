import tkinter as tk
from tkinter import ttk
from windows.add_order_popup import AddPopup
from windows.edit_order_popup import EditPopup


class ListaPedidosFrame(tk.Frame):
    def __init__(self, parent, window_main):
        super().__init__(parent)
        self.config(bg="white")
        self.parent = parent
        self.window_main = window_main
        self.crear_interfaz()

    def crear_interfaz(self):
        # Panel superior con tabla de pedidos y botones
        panel_superior = tk.Frame(self, bg="white")
        panel_superior.grid(row=0, column=0, sticky="nsew", pady=(10, 0), padx=5)

        # - Tabla de pedidos
        self.tabla_pedidos = ttk.Treeview(panel_superior, columns=("Farmacia", "Producto"), show="headings", height=10)
        self.tabla_pedidos.heading("Farmacia", text="Farmacia")
        self.tabla_pedidos.heading("Producto", text="Producto")
        self.tabla_pedidos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        for i in range(20):
            self.tabla_pedidos.insert("", tk.END, values=[f"Farmacia {i}", f"Pedido {i}"])
        self.tabla_pedidos.bind("<Double-1>", self.editar_pedido)

        # - Panel para botones
        panel_botones_superior = tk.Frame(panel_superior, bg="white")
        panel_botones_superior.pack(side=tk.LEFT, padx=10)

        #   - Boton para agregar pedido
        boton_agregar_pedido = tk.Button(panel_botones_superior, text="Agregar Pedido", command=self.agregar_pedido)
        boton_agregar_pedido.pack(side=tk.TOP, pady=5)

        #   - Boton para hacer ruta
        boton_hacer_ruta = tk.Button(panel_botones_superior, text="Hacer Ruta", command=self.hacer_ruta)
        boton_hacer_ruta.pack(side=tk.TOP, pady=5)

        # Panel inferior con botones para editar y eliminar pedidos y tabla de productos de pedidos
        panel_inferior = tk.Frame(self, bg="white")
        panel_inferior.grid(row=1, column=0, sticky="nsew", pady=(10, 0), padx=5)

        # - Panel para botones
        panel_botones_inferior = tk.Frame(panel_inferior, bg="white")
        panel_botones_inferior.pack(side=tk.TOP, padx=10)

        #   - Boton para editar pedido
        boton_editar_pedido = tk.Button(panel_botones_inferior, text="Editar Pedido", command=self.editar_pedido)
        boton_editar_pedido.pack(side=tk.LEFT, pady=5, padx=5)

        #   - Boton para eliminar pedido
        boton_eliminar_pedido = tk.Button(panel_botones_inferior, text="Eliminar Pedido", command=self.eliminar_pedido)
        boton_eliminar_pedido.pack(side=tk.RIGHT, pady=5, padx=5)

        # - Tabla de productos de pedidos
        self.tabla_productos_pedidos = ttk.Treeview(panel_inferior, columns=("Producto", "Cantidad"), show="headings",
                                                    height=10)
        self.tabla_productos_pedidos.heading("Producto", text="Producto")
        self.tabla_productos_pedidos.heading("Cantidad", text="Cantidad")
        for i in range(20):
            self.tabla_productos_pedidos.insert("", tk.END, values=[f"Producto {i}", i])

        self.tabla_productos_pedidos.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def agregar_pedido(self):
        pedido_popup = AddPopup(self, "Agregar Pedido", 400, 400)
        pedido_popup.title("Agregar Pedido")
        pedido_popup.grab_set()
        pedido_popup.focus_set()
        pedido_popup.wait_window()
        print("Agregar Pedido")

    def hacer_ruta(self):
        self.window_main.go_to_route()
        print("Hacer Ruta")

    def editar_pedido(self, event=None):
        selected_item = self.tabla_pedidos.selection()
        if selected_item:
            # Obtener los valores de la fila seleccionada
            values = self.tabla_pedidos.item(selected_item)['values']
            if values:
                print("Farmacia seleccionada:", values, "Indice:", selected_item)
                pedido_popup = EditPopup(self, "Editar Pedido", 400, 400)
                pedido_popup.title("Editar Pedido")
                pedido_popup.grab_set()
                pedido_popup.focus_set()
                pedido_popup.wait_window()
            else:
                print("No hay valores seleccionados en la fila.")
        print("Editar Pedido")

    def eliminar_pedido(self):
        # Pedir confirmacion para eliminar el pedido

        print("Eliminar Pedido")
