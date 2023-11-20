import math

#Clase Administrador de pedidos. Se supone que se le pasa la lista completa de pedidos (order_list) y la orgniza (organized_orders)
# Clase Pedido
class Order:
    def __init__(self, pharmacy_name, product_type, quantity, pharmacy_reputation, distance):
        self.pharmacy_name = pharmacy_name
        self.product_type = product_type
        self.quantity = quantity
        self.pharmacy_reputation = pharmacy_reputation
        self.distance = distance

    def get_pharmacy_name(self):
        return self.pharmacy_name
    
    def get_product_type(self):
        return self.product_type

    def get_quantity(self):
        return self.quantity

    def get_pharmacy_reputation(self):
        return self.pharmacy_reputation

    def get_distance(self):
        return self.distance

# Clase Administrador de pedidos
class OrderManager:
    def __init__(self, order_list):
        self.order_list = order_list
        self.organized_orders = []

    def organize_orders(self):
        self.organized_orders = sorted(self.order_list, key=lambda x: (
            {'emergencia': 3, 'refrigerados': 2, 'cronicos': 1, 'comunes': 0}[x.get_product_type()],
            x.get_quantity(), x.get_pharmacy_reputation(), x.get_distance()
        ), reverse=True)

    def add_order_list(self, order):
        self.order_list.append(order)

    def add_organized_orders(self, order):
        self.organized_orders.append(order)

    def remove_order_list(self, order):
        self.order_list.remove(order)

    def remove_organized_orders(self, pharmacy_name):
        for orders in self.organized_orders:
            if orders.get_pharmacy_name() == pharmacy_name:
                self.organized_orders.remove(orders)

    def get_all_order(self):
        return self.order_list

    def get_organized_orders(self):
        return self.organized_orders
  
# Clase farmacia
class pharmacy:
    id_pharmacy = 0
    pharmacy_name = ""
    pharmacy_NIT = ""
    latitud = 0.0
    longitud = 0.0

    def __init__(self, id_pharmacy, pharmacy_name, pharmacy_NIT, latitud, longitud):
        self.id_pharmacy = id_pharmacy
        self.pharmacy_name = pharmacy_name
        self.pharmacy_NIT = pharmacy_NIT
        self.convert_coordinates(latitud, longitud)
    
    def convert_coordinates(self, latitud, longitud):
        lat_rad = math.radians(latitud)
        lon_rad = math.radians(longitud)

        self.longitud = (6371 * lon_rad) * 10
        self.latitud = (6371 * math.log(math.tan(math.pi / 4 + lat_rad / 2))) * 10

    def get_id_pharmacy(self):
        return self.id_pharmacy
    
    def get_pharmacy_name(self):
        return self.pharmacy_name
    
    def get_pharmacy_NIT(self):
        return self.pharmacy_NIT
    
    def get_latitud(self):
        return self.latitud
    
    def get_longitud(self):
        return self.longitud

# Clase Arcos
class arch:
    pharmacy_1 = ""
    pharmacy_2 = ""
    distance = ""

    def __init__(self, pharmacy_1, pharmacy_2):
        self.pharmacy_1 = pharmacy_1
        self.pharmacy_2 = pharmacy_2
        self.calculate_distance()

    def calculate_distance(self):
        self.distance = round(math.sqrt((self.pharmacy_2.get_latitud() - self.pharmacy_1.get_latitud())**2 + (self.pharmacy_2.get_longitud() - self.pharmacy_1.get_longitud())**2))

    def get_pharmacy_1(self):
        return self.pharmacy_1
    
    def get_pharmacy_2(self):
        return self.pharmacy_2
    
    def get_distance(self):
        return self.distance

# Clase tipo de producto
class product_type:
    id_product_type = 0
    type = ""
    
    def __init__(self, id_product_type, type):
        self.id_product_type = id_product_type
        self.type = type
    
    def get_id_product_type(self):
        return self.id_product_type    
    
    def get_type(self):
        return self.type
    
# Clase producto
class product:
    id_product = 0
    product_name = ""
    product_description = ""
    product_type = ""

    def __init__(self, id_product, product_name, product_description, product_type):
        self.id_product = id_product
        self.product_name = product_name
        self.product_description = product_description
        self.product_type = product_type

    def get_id_product(self):
        return self.id_product
    
    def get_product_name(self):
        return self.product_name
    
    def get_product_description(self):
        return self.product_description
    
    def get_product_type(self):
        return self.product_type  