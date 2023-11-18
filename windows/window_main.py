import tkinter as tk

import config
import util.util_images as utils_images
import util.util_window as utils_window
from windows.window_pharmacies import Tabla


class MainWindow(tk.Tk):
    # attributo Logo

    def __init__(self):
        super().__init__()
        self.logo = utils_images.read_image("image/logo.png", (100, 100))
        self.home = utils_images.read_image("image/home.png", (50, 50))
        self.config_window()
        self.paneles()
        self.lateral_panel_control()
        self.main_panel_control()

    def config_window(self):
        self.title("Farmasec")
        self.iconbitmap("image/logo.ico")
        w, h = config.WIDTH, config.HEIGHT
        utils_window.center_frame(self, w, h)
        self.resizable(False, False)
        self.config(bg=config.COLOR_PRINCIPAL)

    def show_panel(self, panel):
        self.main_panel.pack_forget()  # Oculta el panel actual
        self.pharmacies_panel.pack_forget()  # Oculta el panel actual
        self.list_panel.pack_forget()  # Oculta el panel actual
        panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)  # Muestra el nuevo panel

    def paneles(self):
        self.lateral_panel = tk.Frame(self, bg=config.COLOR_PRINCIPAL, width=150)
        self.lateral_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

        self.main_panel = tk.Frame(self, bg=config.COLOR_SECUNDARIO, width=800)
        self.main_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.pharmacies_panel = tk.Frame(self, bg=config.COLOR_TERCERO, width=800)
        self.pharmacies_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.pharmacies_panel_control()
        self.pharmacies_panel.pack_forget()

        self.list_panel = tk.Frame(self, bg=config.COLOR_TERCERO, width=800)
        self.list_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.list_panel.pack_forget()

    def go_to_pharmacies(self):
        self.main_panel.pack_forget()  # Oculta el panel actual
        self.list_panel.pack_forget()  # Oculta el panel actual
        self.pharmacies_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)  # Muestra el nuevo panel
        print("Farmacias")
        pass

    def go_to_product_list(self):
        self.show_panel(self.list_panel)
        print("Lista de Pedidos")
        pass

    def go_to_home(self):
        self.show_panel(self.main_panel)
        print("Home")
        pass

    def lateral_panel_control(self):
        # Boton de inicio
        # image_home = utils_images.read_image("image/home.png", (50, 50))
        self.main_button = tk.Button(self.lateral_panel, image=self.home, command=self.go_to_home)
        self.main_button.pack(side=tk.TOP, pady=50, padx=55)
        # self.main_button.pack(side=tk.TOP)

        # Boton de Relleno
        self.fill_button1 = tk.Button(self.lateral_panel, bg=self.lateral_panel.cget("bg"), border=0)
        self.fill_button1.pack(side=tk.TOP, pady=20, expand=False)

        # Boton de Farmacias
        self.farmacy_button = tk.Button(self.lateral_panel, text="Farmacias", bg=config.COLOR_BOTONES)
        self.farmacy_button.config(anchor=tk.W, command=self.go_to_pharmacies)
        self.farmacy_button.pack(side=tk.TOP, padx=25, fill=tk.X, expand=True)

        # Boton de Lista de Pedidos
        self.list_button = tk.Button(self.lateral_panel, text="Lista de Pedidos", bg=config.COLOR_BOTONES)
        self.list_button.config(anchor=tk.W, command=self.go_to_product_list)
        self.list_button.pack(side=tk.TOP, padx=25, fill=tk.X, expand=True)

        # Boton de Relleno
        self.fill_button2 = tk.Button(self.lateral_panel, bg=self.lateral_panel.cget("bg"), border=0)
        self.fill_button2.pack(side=tk.TOP, pady=80, expand=False)

    def main_panel_control(self):
        self.main_title = tk.Label(self.main_panel, text="Farmasec", font=("Arial", 30), bg=self.main_panel.cget("bg"))
        self.main_title.pack(side=tk.TOP, pady=50, padx=55)

        self.main_logo = tk.Label(self.main_panel, image=self.logo, bg=self.main_panel.cget("bg"))
        self.main_logo.pack(side=tk.TOP, pady=50, padx=55)

    def pharmacies_panel_control(self):
        self.pharmacies_main = tk.Label(self.pharmacies_panel, text="Farmacias", font=("Arial", 30), bg=self.pharmacies_panel.cget("bg"))
        self.pharmacies_main.config()
        self.pharmacies_main.pack(fill=tk.X)

        self.pharmacies_table = Tabla(self.pharmacies_main, ("Nombre", "Dirección", "Teléfono", "Horario"))
        self.pharmacies_table.pack(side=tk.BOTTOM, pady=50)

        filas = [["FarmaciaFarmacia 1", "DirecciónDirección 1", "Teléfono 1", "Horario 1"],
                 ["Farmacia 2", "Dirección 2", "Teléfono 2", "Horario 2"],
                 ["Farmacia 2", "Dirección 2", "Teléfono 2", "Horario 2"],
                 ["Farmacia 2", "Dirección 2", "Teléfono 2", "Horario 2"],
                 ["Farmacia 2", "Dirección 2", "Teléfono 2", "Horario 2"],
                 ["Farmacia 2", "Dirección 2", "Teléfono 2", "Horario 2"],
                 ["Farmacia 2", "Dirección 2", "Teléfono 2", "Horario 2"],
                 ["Farmacia 2", "Dirección 2", "Teléfono 2", "Horario 2"]]
        for fila in filas:
            self.pharmacies_table.agregar_fila(fila)

        #create a vertical scrollbar to the right of the table in the main panel
        # self.pharmacies_vsb = tk.Scrollbar(self.pharmacies_main, orient="vertical", command=self.pharmacies_table.yview)
        # self.pharmacies_table.configure(yscrollcommand=self.pharmacies_vsb.set)
        # self.pharmacies_vsb.pack(side="right", fill="y")