import os
import string
import tkinter
import random
from fonctions.data import get_data, recording_data

folder_current = os.getcwd().replace("/patient", "")
folder_data = os.path.join(folder_current, "data_programme")

list_patients = get_data(folder_data, "list_patients")
list_appointment = get_data(folder_data, "list_appoitment")

def recording_clients():
    last_name = input("Veuillez entrer votre nom: ").lower()
    firs_name = input("Veuillez entrer votre prénom: ").lower()
    telephone = input("Veuillez entrer votre numéro de téléphone: ")
    password = input("Veuillez entrer votre mot de passe: ").lower()
    
    if last_name and firs_name and telephone.isdigit() and password:
        _id = creation_id(list_patients, "id")
        
        data_patient = {
            "id": _id,
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
        

def appoitment():
    last_name = input("Veuillez entrer votre nom: ")
    firs_name = input("Veuillez entrer votre prénom: ")
    telephone = input("Veuillez entrer votre numéro de télephone: ")
    choose_specialist = input("Veuillez choisir votre spéialiste: ")
    
    if firs_name and last_name and telephone.isdigit() and choose_specialist:
        _id = creation_id(list_appointment, "id")
        data_appointment = {
            "id": _id,
            "last_name": last_name,
            "firs_name": firs_name,
            "telephone": telephone,
            "choose_specialist": choose_specialist
        }
        
        list_appointment.append(data_appointment)
        recording_data(list_appointment, folder_current, "data_programme", "list_appoitment")
    else:
        print("Erreur")
        

def creation_id(list_check: list, cle_search: str) -> str: 
    """
    Cette foonction nous permet de génerer un id unique

    Args:
        list_check (list): Ce paremetre represente la liste a parcourir 
        key_search (str): Ce paremetre represente la clé de notre dictionnaire

    Returns:
        [str]: La fonctionne nous retourne l'id 
    """
    
    list_alphabet = list(string.ascii_letters)
    id_unique = []
    id_existe = False
    
    for i in range(8):
        n = random.choice(list_alphabet)
        id_unique.append(n)
    
    id_unique = "".join(id_unique)
    
    for item in list_check:
        if item[cle_search] == id_unique:
            id_existe = True
            break
        
    if id_existe:
        creation_id()
    return id_unique

    
def cancel_appointment():
    id_appointment = input("Veuillez entrer l'identifiant du rendez vous: ")
    
    if id_appointment:
        for item in list_appointment:
            if item["id"] == id_appointment:
                list_appointment.remove(item)
                recording_data(list_appointment, folder_current, "data_programme", "list_appoitment")
                break
    else:
        print("Veuillez entrer un identifiant correcte")
        
   