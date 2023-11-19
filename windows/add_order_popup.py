import tkinter as tk
import tkinter.ttk as ttk


class Popup(tk.Toplevel):
    def __init__(self, parent, title, width, height):
        super().__init__(parent)
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.resizable(False, False)
        self.config(bg="white")

        self.parent = parent

        self.crear_interfaz()

    def crear_interfaz(self):
        # Lista desplegable para elegir una farmacia
        farmacia_label = tk.Label(self, text="Elegir Farmacia:")
        farmacia_label.grid(row=0, column=0, pady=(10, 5), padx=10, sticky="e")
        farmacia_dropdown = ttk.Combobox(self, values=["Farmacia 1", "Farmacia 2", "Farmacia 3"])
        farmacia_dropdown.grid(row=0, column=1, pady=(10, 5), padx=10, sticky="w")

        # Lista desplegable para elegir un producto
        producto_label = tk.Label(self, text="Elegir Producto:")
        producto_label.grid(row=1, column=0, pady=5, padx=10, sticky="e")
        producto_dropdown = ttk.Combobox(self, values=["Producto 1", "Producto 2", "Producto 3"])
        producto_dropdown.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        # Panel para aumentar los pedidos
        cantidad_label = tk.Label(self, text="Cantidad:")
        cantidad_label.grid(row=2, column=0, pady=5, padx=10, sticky="e")

        cantidad_var = tk.StringVar(value="1")
        cantidad_entry = tk.Entry(self, textvariable=cantidad_var)
        cantidad_entry.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        disminuir_button = tk.Button(self, text="-", command=lambda: self.actualizar_cantidad(cantidad_var, -1))
        disminuir_button.grid(row=2, column=2, pady=5, padx=5, sticky="w")

        aumentar_button = tk.Button(self, text="+", command=lambda: self.actualizar_cantidad(cantidad_var, 1))
        aumentar_button.grid(row=2, column=3, pady=5, padx=5, sticky="w")

        # Boton para agregar el producto al pedido
        agregar_producto_button = tk.Button(self, text="Agregar Producto",
                                            command=lambda: self.guardar_producto(farmacia_dropdown.get(),
                                                                                  producto_dropdown.get(),
                                                                                  cantidad_var.get(), productos_table))
        agregar_producto_button.grid(row=3, column=0, columnspan=4, pady=(10, 0))

        # Tabla para mostrar los productos del pedido
        productos_table = ttk.Treeview(self, columns=("Producto", "Cantidad"), show="headings", height=5)
        productos_table.column("Producto", width=150)
        productos_table.heading("Producto", text="Producto")
        productos_table.column("Cantidad", width=80)
        productos_table.heading("Cantidad", text="Cantidad")
        productos_table.grid(row=4, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")

        # Boton para agregar el pedido
        agregar_pedido_button = tk.Button(self, text="Agregar Pedido",
                                          command=lambda: self.guardar_pedido())
        agregar_pedido_button.grid(row=5, column=0, columnspan=4, pady=(10, 0))

        # Configuraciones del layout
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(3, weight=1)

    def actualizar_cantidad(self, cantidad_var, cambio):
        nueva_cantidad = int(cantidad_var.get()) + cambio
        if nueva_cantidad >= 1:
            cantidad_var.set(str(nueva_cantidad))

    def guardar_pedido(self):
        # Lógica para guardar el pedido en la tabla

        self.destroy()

    def guardar_producto(self, farmacia, producto, cantidad, productos_table):
        # Lógica para guardar el pedido en la tabla
        productos_table.insert("", tk.END, values=(producto, cantidad))
        self.refresh_table(productos_table)


    def refresh_table(self, productos_table):
        print("Refresh table")

