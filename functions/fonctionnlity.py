from functions import data
from main import folder_data, folder_current


def recording_clients():
    list_patients = data.get_data(folder_data, "list_patients")
    last_name = input("Veuillez entrer votre nom: ").lower()
    firs_name = input("Veuillez entrer votre prénom: ").lower()
    telephone = int(input("Veuillez entrer votre numéro de téléphone: "))
    password = input("Veuillez entrer votre mot de passe: ").lower()
    
    if last_name and firs_name and is_numeric(telephone) and password:
        data_patient = {
            "last_name": last_name,
            "firs_name": firs_name,
            "telephone": telephone,
            "password": password
        }

        list_patients.append(data_patient)
        data.recording_data(list_patients, folder_current, "data", "list_patients")
    else:
        print("Erreur")

