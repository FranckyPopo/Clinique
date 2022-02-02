import os
from fonctions import fonctionnality

folder_current = os.getcwd()
folder_data = os.path.join(folder_current, "data")

fonctionnality.connection()