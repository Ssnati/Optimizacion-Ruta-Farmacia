import random
import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class RouteFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg="white")
        self.graph = nx.Graph()  # Grafo
        self.rutas_list = []  # Lista de rutas

        self.crear_interfaz()

    def crear_interfaz(self):
        # Subframe izquierdo para el grafo
        self.panel_izquierdo = tk.Frame(self, bg="white")
        self.panel_izquierdo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Subframe derecho para la lista
        self.panel_derecho = tk.Frame(self, bg="white")
        self.panel_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Crear grafo visual
        self.crear_grafo_visual()

        # Crear lista de rutas
        self.ver_rutas()

    def crear_grafo_visual(self):
        # Crear un grafo simple para el ejemplo
        self.graph.add_nodes_from(range(1, 20))
        for i in range(1, 20):
            self.graph.add_edge(random.randint(1, 20), random.randint(1, 20))

        # Tamaño personalizado de la figura
        fig, ax = plt.subplots(figsize=(1, 1))
        nx.draw(self.graph, with_labels=True, font_weight='bold', ax=ax)

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
