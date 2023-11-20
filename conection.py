from model import *
import sqlite3 as sq
import networkx as nx
import matplotlib.pyplot as plt

class conection:
    conection = sq.connect("BD/distribuidora.db")
    orders_list = [
    Order("Farmacia A", "Medicamento X", 10, 4.5, 2.3),
    Order("Farmacia B", "Medicamento Y", 5, 3.8, 1.5),
    Order("Farmacia C", "Medicamento Z", 8, 4.0, 3.0)]
    order_imanager = ""
    products = []
    pharmacies = []
    archs = []
    graph = nx.DiGraph()

    def __init__(self):
        self.order_manager = OrderManager(self.orders_list)
        self.consult_products()
        self.consult_pharmacies()
        self.consult_archs()
        self.add_nodes_graph()
    
    # Ya
    def add_nodes_graph(self):
        # positions = dict()
        # for ph in self.pharmacies:
        #     positions[ph.get_pharmacy_name()] = (ph.get_latitud(), ph.get_longitud())
        #     self.graph.add_node(ph.get_pharmacy_name())
        
        positions = dict()
        # Crear un grafo simple para el ejemplo
        for ph in self.pharmacies:
            positions[ph.get_pharmacy_name()] = (ph.get_latitud(), ph.get_longitud())
            self.graph.add_node(ph.get_pharmacy_name())
        
        for a in self.archs:
            self.graph.add_edge(a.get_pharmacy_1().get_pharmacy_name(), a.get_pharmacy_2().get_pharmacy_name(), weight=a.get_distance())
        
        # nx.draw(self.graph, pos=positions, node_color='blue',edge_color='red',with_labels=True)
        # labels = nx.get_edge_attributes(self.graph, 'weight')
        # nx.draw_networkx_edge_labels(self.graph, positions, edge_labels=labels)
        # plt.title("Grafo Ponderado Dirigido")
        
        # Calcular el camino más corto desde 'A' a 'E'
        shortest_path = nx.shortest_path(self.graph, source='SALUDEXPRESS', target='ECOFARMA')

        # Asignar colores a los nodos y bordes del camino
        node_colors = ['red' if node in shortest_path else 'blue' for node in self.graph.nodes()]
        edge_colors = ['red' if (u, v) in zip(shortest_path, shortest_path[1:]) else 'blue' for u, v in self.graph.edges()]

        # Dibujar el grafo con colores asignados
        nx.draw(self.graph, positions, with_labels=True, node_color=node_colors, edge_color=edge_colors, font_weight='bold')
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, positions, edge_labels=labels)
        plt.show()


    def delete_nodes_graph(self, pharmacy_name):
        for ph in self.pharmacies:
            if ph.get_pharmacy_name() == pharmacy_name:
                self.graph.remove_node(ph.get_pharmacy_name())
    
    def add_archs_graph(self):
        for a in self.archs:
            self.graph.add_edge(a.get_pharmacy_1().get_pharmacy_name(), a.get_pharmacy_2().get_pharmacy_name(), weight=a.get_distance())
    
    def obtain_dijkstra_source_to_target(self, source, target):
        shortest_paths = nx.single_source_dijkstra(self.graph, source=source)
        # print(f"Todos caminos: {shortest_paths[0]}")
        path = shortest_paths[1][target]
        distance= shortest_paths[0][target]
        return path, distance
    
    def obtain_path_dijkstra_source_to_target(self, source, target):
        path, _ = self.obtain_dijkstra_source_to_target(source, target)
        path_string = ', '.join(path)
        return path_string

    def ordered_list_update(self, source, target):
        list = self.obtain_path_dijkstra_source_to_target(source, target)
        arr = list.split(',')
        for i in range(len(arr)):
            self.order_manager.remove_organized_orders(arr[i])

    def search_pharmacy(self, id_pharmacy):
        for ph in self.pharmacies:
            if ph.get_id_pharmacy() == id_pharmacy:
                return ph
        return pharmacy() 
    
    def consult_products(self):
        cursor = self.conection.cursor()
        cursor.execute("SELECT P.id_product, P.product_name, P.product_description, PT.id_product_type, PT.type FROM PRODUCTS P INNER JOIN PRODUCT_TYPES PT ON P.id_product_type = PT.id_product_type")
        for i in cursor.fetchall():
            self.products.append(product(i[0],i[1],i[2], product_type(i[3],i[4])))

        
    def consult_pharmacies(self):
        cursor = self.conection.cursor()
        cursor.execute("SELECT * FROM PHARMACIES")
        for i in cursor.fetchall():
            self.pharmacies.append(pharmacy(i[0],i[1],i[2],i[3],i[4]))
    
    def consult_archs(self):
        cursor = self.conection.cursor()
        cursor.execute("SELECT * FROM PHARMACY_CONECTIONS")
        for i in cursor.fetchall():
            self.archs.append(arch(self.search_pharmacy(i[0]), self.search_pharmacy(i[1])))
                    
    def get_products(self):
        return self.products
    
    def get_pharmacies(self):
        return self.pharmacies
    
    def get_archs(self):
        return self.archs
    
    def obtain_archs_data(self):
        return nx.get_edge_attributes(self.graph,'weight').items()


conection()

# path, distance = conection().obtain_dijkstra_source_to_target("DISTRIBUIDORA FARMASEC", "VIDAFARMACIAS")

# print(f"\nCamino más corto desde DISTRIBUIDORA FARMASEC a VIDAFARMACIAS: {path} con una distancia de {distance}")
# archs_data = conection().obtain_archs_data()
# for i in archs_data:
#     pharmacies = i[0]
#     print(f"{pharmacies[0]} - {pharmacies[1]} - {i[1]}")
    
# conection.commit()
# products = conection().get_products()
# for i in products:
#     print(f"{i.get_id_product()} - {i.get_product_name()} - {i.get_product_description()} - {i.get_product_type().get_id_product_type()} - {i.get_product_type().get_type()}")

# pharmacies = conection().get_pharmacies()
# for i in pharmacies:
#     print(f"{i.get_id_pharmacy()} - {i.get_pharmacy_name()} - {i.get_pharmacy_NIT()} - {i.get_latitud()} - {i.get_longitud()}")

# archs = conection().get_archs()
# for i in archs:
#     print(f"Origen: {i.get_pharmacy_1().get_id_pharmacy()} - {i.get_pharmacy_1().get_pharmacy_name()} | Destino: {i.get_pharmacy_2().get_id_pharmacy()} - {i.get_pharmacy_2().get_pharmacy_name()} | Distancia: {i.get_distance()}")
