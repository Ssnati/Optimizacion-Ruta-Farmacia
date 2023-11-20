from model import *
from conection import *
from windows.window_main import *

con = conection()
app = MainWindow()
app.load_pharmacies(con.getMatrixPharmacy)
app.mainloop()
