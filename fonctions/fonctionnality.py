import os
from fonctions.data import get_data, recording_data

folder_current = os.getcwd().replace("/fonctions", "")
folder_data = os.path.join(folder_current, "data_programme")


def recording_clients():
    list_patients = get_data(folder_data, "list_patients")
    last_name = input("Veuillez entrer votre nom: ").lower()
    firs_name = input("Veuillez entrer votre prénom: ").lower()
    telephone = input("Veuillez entrer votre numéro de téléphone: ")
    password = input("Veuillez entrer votre mot de passe: ").lower()
    
    if last_name and firs_name and telephone.isdigit() and password:
        data_patient = {
            "last_name": last_name,
            "firs_name": firs_name,
            "telephone": telephone,
            "password": password
        }

        list_patients.append(data_patient)
        recording_data(list_patients, folder_current, "data_programme", "list_patients")
    else:
        print("Erreur")

def connection():
    pass