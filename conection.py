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
    order_manager = ""
    products = []
    pharmacies = []
    archs = []
    graph = nx.DiGraph()

    def __init__(self):
        self.order_manager = OrderManager(self.orders_list)
        self.consult_products()
        self.consult_pharmacies()
        self.consult_archs()
        self.add_archs_graph()
        self.add_archs_graph()
        
        position = nx.layout.circular_layout(self.graph)
        nx.draw_networkx(self.graph,position)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, position, edge_labels=labels)
        plt.title("Grafo Ponderado Dirigido")
        plt.show()
        # --- 
        
    def add_nodes_graph(self):
        for ph in self.pharmacies:
            self.graph.add_node(ph.get_pharmacy_name())

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

path, distance = conection().obtain_dijkstra_source_to_target("DISTRIBUIDORA FARMASEC", "VIDAFARMACIAS")

print(f"\nCamino más corto desde DISTRIBUIDORA FARMASEC a VIDAFARMACIAS: {path} con una distancia de {distance}")
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
