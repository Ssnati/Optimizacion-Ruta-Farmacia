import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class RouteFrame(tk.Frame):
    def __init__(self, parent, pharmacies, archs, shortest_path):
        super().__init__(parent)
        self.config(bg="white")
        self.graph = nx.DiGraph()  # Grafo Dirijido
        self.rutas_list = []  # Lista de rutas
        for i in range(5):
            self.rutas_list.append(f"Ruta {i}")

        self.crear_interfaz()
        self.crear_grafo_visual(pharmacies,archs,shortest_path)

    def crear_interfaz(self):
        # Subframe izquierdo para el grafo
        self.panel_izquierdo = tk.Frame(self, bg="white")
        self.panel_izquierdo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Subframe derecho para la lista
        self.panel_derecho = tk.Frame(self, bg="white")
        self.panel_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Crear grafo visual
        #self.crear_grafo_visual()

        # Crear lista de rutas
        #self.ver_rutas()

    def crear_grafo_visual(self,pharmacies,archs,shortest_path):
        positions = dict()
        # Crear un grafo simple para el ejemplo
        for ph in pharmacies:
            positions[ph.get_pharmacy_name()] = (ph.get_latitud(), ph.get_longitud())
            self.graph.add_node(ph.get_pharmacy_name())
        
        for a in archs:
            self.graph.add_edge(a.get_pharmacy_1().get_pharmacy_name(), a.get_pharmacy_2().get_pharmacy_name(), weight=a.get_distance())

        # Asignar colores a los nodos y bordes del camino
        node_colors = ['red' if node in shortest_path else 'blue' for node in self.graph.nodes()]
        edge_colors = ['red' if (u, v) in zip(shortest_path, shortest_path[1:]) else 'blue' for u, v in self.graph.edges()]

        # Dibujar el grafo con colores asignados
        fig, ax = plt.subplots(figsize=(1, 1))
        nx.draw(self.graph, positions, with_labels=True, node_color=node_colors, edge_color=edge_colors, font_weight='bold',ax=ax)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, positions, edge_labels=labels)

        # Visualizar el grafo utilizando Matplotlib y Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.panel_izquierdo)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def ver_rutas(self):
        # Limpiar la lista
        for child in self.panel_derecho.winfo_children():
            child.destroy()

        # Crear un label por cada ruta
        for ruta in self.rutas_list:
            label = tk.Label(self.panel_derecho, text=ruta)
            label.pack(side=tk.TOP, pady=5, padx=5)