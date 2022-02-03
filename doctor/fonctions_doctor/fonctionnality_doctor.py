import os
from patient.fonctions.data import get_data, recording_data

folder_current = os.getcwd().replace("/doctor", "")
folder_data = os.path.join(folder_current, "data_programme")

list_patient = get_data(folder_data, "list_patients")
list_notebook = get_data(folder_data, "list_notebook")  


def fill_notebook():
    id_patient = input("Veuillez entrer l'identifiant du patient: ")
    reason = input("Veuillez remplir le canet: ")  
    
    canet = {"id": id_patient, "reason": reason}
    list_notebook.append(canet)
    
    for item in list_patient:
        if item["id"] == id_patient:
            recording_data(list_notebook, folder_current, "data_programme", "list_notebook")
            break
    else:
        print("L'identifiant n'es pas attribué a un patient")
            

def modify_notebook():
    id_patient = input("Veuillez entrer l'identifiant du patient: ")
    new_reason = input("Veuillez remplir le canet: ")  
    
    for item in list_notebook:
        if item["id"] == id_patient:
            item["reason"] = new_reason
            recording_data(list_notebook, folder_current, "data_programme", "list_notebook")
            break
    else:
        print("L'identifiant n'es pas attribué a un patient")
    