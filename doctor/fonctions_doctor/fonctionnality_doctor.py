import os
from patient.fonctions.data import get_data, recording_data

folder_current = os.getcwd().replace("/doctor", "")
folder_data = os.path.join(folder_current, "data_programme")

list_patient = get_data(folder_data, "list_patients")


def fill_canet():
    id_patient = input("Veuillez entrer l'identifiant du patient: ")
    reason = input("Veuillez remplir le canet: ")  
    
    list_canet = get_data(folder_data, "list_canet")  
    canet = {"id": id_patient, "reason": reason}
    list_canet.append(canet)
    
    for item in list_patient:
        if item["id"] == id_patient:
            recording_data(list_canet, folder_current, "data_programme", "list_canet")
            break
    else:
        print("L'identifiant du partient est incorrecte")
            

    
    
    