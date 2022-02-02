import os
from functions import fonctionnlity

folder_current = os.getcwd()
folder_data = os.path.join(folder_current, "data")

fonctionnlity.recording_clients()