import os
from fonctions.data import get_data, recording_data

folder_current = os.getcwd().replace("/fonctions", "")
folder_data = os.path.join(folder_current, "data_programme")

list_patients = get_data(folder_data, "list_patients")

def recording_clients():
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
    telephone = input("Veuillez entrez votre numero de telephone: ")
    password = input("Veuillez entrez votre mot de passe: ")
    account_exists = False
    
    if password and telephone.isdigit():
        for item in list_patients:
            if item["telephone"] and item["password"]:
                account_exists = True
                break
        
        if account_exists:
            print("Le compte existe")
        else:
            print("Le compte n'existe pas")
    else:
        print("Erreur")