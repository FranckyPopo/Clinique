import os
from functools import partial
from time import sleep
import tkinter
from tkcalendar import DateEntry
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from fonctions.data import get_data, recording_data
from fonctions import fonctionnality

# Chemin pour les images
folder_clinique = os.getcwd().replace("patient", "")
folder_img = os.path.join(folder_clinique, "img")
path_img = folder_img + "/" + "—Pngtree—healthcare medical logo vector icon_5059582.png"

# Chemin pour les fichiers json 
folder_data = os.path.join(folder_clinique, "data_programme")
list_patients = get_data(folder_data, "list_patients")
list_appointment = get_data(folder_data, "list_appoitment")
list_reason = get_data(folder_data, "list_notebook")

# ID patient
_ID = {}

def recording_clients():
    def check_registration():
        last_name = enter_last_name.get().lower()
        firs_name = enter_firs_name.get().lower()
        phone = enter_phone.get()
        password = enter_password.get()
        
        if last_name and firs_name and phone.isdigit() and password:
            _id = fonctionnality.creation_id(list_patients, "id")
            data_patient = {
                "id": _id,
                "last_name": last_name,
                "firs_name": firs_name,
                "phone": phone,
                "password": password
            }
            
            for key, value in data_patient.items(): _ID[key] = value
             
            list_patients.append(data_patient)
            recording_data(list_patients, folder_clinique, "data_programme", "list_patients")
            
            enter_last_name.delete(0, "end")
            enter_firs_name.delete(0, "end")
            enter_phone.delete(0, "end")
            enter_password.delete(0, "end")
            
            label_error["fg"] = "#15AED6"
            window_user()
        else:
            label_error["fg"] = "#FA0000"
    
    frame_main.place_forget()    
    frame_container_registration.place(x=150, y=140) 
    
    label_title = tkinter.Label(frame_container_registration, text="Crée votre compte", bg="#15AED6", font=("Arial", 24, "bold"))
    label_title.grid(row=0, column=0, pady=20, sticky="w")
    
    label_last_name = tkinter.Label(frame_container_registration, text="Nom:", bg="#15AED6", font=("Rubik", 16), fg="#1C1C1C")
    label_last_name.grid(row=1, column=0, sticky="w")
    
    enter_last_name = tkinter.Entry(frame_container_registration, width=30)
    enter_last_name.grid(row=2, column=0, sticky="w", pady=5)
    
    label_firs_name = tkinter.Label(frame_container_registration, text="Prénom:", bg="#15AED6", font=("Rubik", 16), fg="#1C1C1C")
    label_firs_name.grid(row=3, column=0, sticky="w")
    
    enter_firs_name = tkinter.Entry(frame_container_registration, width=30)
    enter_firs_name.grid(row=4, column=0, sticky="w", pady=5)
    
    label_phone = tkinter.Label(frame_container_registration, text="Téléphone:", bg="#15AED6", font=("Rubik", 16), fg="#1C1C1C")
    label_phone.grid(row=5, column=0, sticky="w")
    
    enter_phone = tkinter.Entry(frame_container_registration, width=30)
    enter_phone.grid(row=6, column=0, sticky="w", pady=5)
    
    label_password = tkinter.Label(frame_container_registration, text="Mot de passe:", bg="#15AED6", font=("Rubik", 16), fg="#1C1C1C")
    label_password.grid(row=7, column=0, sticky="w")
    
    enter_password = tkinter.Entry(frame_container_registration, width=30)
    enter_password.grid(row=8, column=0, sticky="w", pady=5)

    label_error = tkinter.Label(frame_container_registration, text="Veuillez remplir tout les champs", fg="#15AED6", bg="#15AED6", font=("Arial", 12, "bold"))
    label_error.grid(row=9, column=0, sticky="w", pady=5)
    
    bnt_registration = tkinter.Button(frame_container_registration, text="S'inscrir", bg="#0e7993", width=8, height=2, font=("Rubik", 13), command=check_registration)
    bnt_registration.grid(row=10, column=0, sticky="w", pady=5) 
    
    bnt_back = tkinter.Button(frame_container_registration, text="Retour", bg="#FA0000", width=8, height=2, font=("Rubik", 13), command=back)
    bnt_back.grid(row=11, column=0, sticky="w", pady=5)


def connection():
    def check_connection():
        password = enter_password.get()
        phone = enter_phone.get()        

        if password and phone.isdigit():
            for items in list_patients:
                if items["phone"] == phone and items["password"] == password:
                    label_error["fg"] = "#15AED6"
                    enter_password.delete(0, "end")
                    enter_phone.delete(0, "end")
                    
                    for key, value in items.items():
                        _ID[key] = value
                    window_user()
                    break
            else:
                label_error["fg"] = "#FA0000"    
        else:
            label_error["fg"] = "#FA0000"
    
    frame_main.place_forget()
    
    frame_container_connection.place(x=150, y=140)  
        
    label_title = tkinter.Label(frame_container_connection, text="Connectez-vous", bg="#15AED6", font=("Arial", 24, "bold"))
    label_title.grid(row=0, column=0, pady=15)
    
    label_phone = tkinter.Label(frame_container_connection, text="Téléphone", bg="#15AED6", font=("Rubik", 16), fg="#1C1C1C")
    label_phone.grid(row=1, column=0, sticky="w")
    
    enter_phone = tkinter.Entry(frame_container_connection)
    enter_phone.grid(row=2, column=0, sticky="w", pady=5)
    
    label_password = tkinter.Label(frame_container_connection, text="Mot de passe:", bg="#15AED6", font=("Rubik", 16), fg="#1C1C1C")
    label_password.grid(row=3, column=0, sticky="w")
    
    enter_password = tkinter.Entry(frame_container_connection)
    enter_password.grid(row=4, column=0, sticky="w", pady=5)
    
    label_error = tkinter.Label(frame_container_connection, text="Impossible de vous connecter", fg="#15AED6", bg="#15AED6", font=("Arial", 12, "bold"))
    label_error.grid(row=5, column=0, sticky="w", pady=7)
    
    bnt_connect = tkinter.Button(frame_container_connection, text="Se connecter", width=10, height=2, bg="#0e7993", command=check_connection, font=("Rubik", 13))
    bnt_connect.grid(row=6, column=0, pady=5, sticky="w")
    
    bnt_back = tkinter.Button(frame_container_connection, text="Retour", bg="#FA0000", width=8, height=2, font=("Rubik", 13), command=back)
    bnt_back.grid(row=7, column=0, sticky="w", pady=5)
    
    
def back():
    frame_container_connection.place_forget()        
    frame_container_registration.place_forget()
    frame_main.place(x=80, y=200)
    
    
def window_user():
    frame_container_connection.place_forget()
    frame_container_registration.place_forget()
    frame_container_see_notebook.place_forget()
    frame_container_img.pack_forget()
    
    frame_menu = tkinter.Frame(frame_1, bg="white")
    frame_menu.place(x=0, y=110)
    
    bnt_appointment = tkinter.Button(frame_menu, text="Prendre rendez-vous", bg="#eaeaea", width=76, height=3, command=appoitment, relief="raised")
    bnt_appointment.grid(row=0, column=0, pady=50)
    
    bnt_notebook = tkinter.Button(frame_menu, text="Voir canet de santé", bg="#eaeaea", width=76, height=3, command=see_notebook, relief="raised")
    bnt_notebook.grid(row=1, column=0, pady=50)
    
    bnt_cancel = tkinter.Button(frame_menu, text="Anuler un rendez-vous", bg="#eaeaea", width=76, height=3, command=cancel_appointment, relief="raised")
    bnt_cancel.grid(row=2, column=0, pady=50)


def appoitment():
    def check_appoitment ():
        choose_specialist = enter_specialist.get()
        date_appoitment = enter_date.get()
        
        if date_appoitment and choose_specialist:
            _id = fonctionnality.creation_id(list_appointment, "id")
            data_appointment = {
                "id": _id,
                "last_name": _ID.get("last_name", "la clé last_name n'existe pas"),
                "firs_name": _ID.get("firs_name", "la clé firs_name n'existe pas"),
                "phone": _ID.get("phone", "la clé phone n'existe pas"),
                "choice_specialist": choose_specialist,
                "data_appointment": date_appoitment
            }
            
            list_appointment.append(data_appointment)
            recording_data(list_appointment, folder_clinique, "data_programme", "list_appoitment")
            
            messagebox.showinfo("Rendez-vous", "Votre rendez-vous a été pris avec succès")
            label_error["fg"] = "#15AED6"
            cancel_appointment()
        else:
           label_error["fg"] = "#FA0000"
    
    frame_container_cancel_appointment.place_forget()
    frame_container_see_notebook.place_forget()
    frame_container_appointment.place(x=180, y=220)
    
    label_specialist = tkinter.Label(frame_container_appointment, text="Spécialiste:", bg="#15AED6", font=("Rubik", 16), fg="#1C1C1C")
    label_specialist.grid(row=0, column=0, sticky="w", pady=5)
    
    choice_specialist = ["Genéraliste", "Dermatologue", "Dentiste", "Neurologue", "Génécolgue"]
    enter_specialist = ttk.Combobox(frame_container_appointment, values=choice_specialist)
    enter_specialist.current(0)
    enter_specialist.grid(row=1, column=0, sticky="w", pady=5)
    
    label_specialist = tkinter.Label(frame_container_appointment, text="Date du rendez-vous:", bg="#15AED6", font=("Rubik", 16), fg="#1C1C1C")
    label_specialist.grid(row=2, column=0, sticky="w", pady=5)
    
    enter_date = DateEntry(frame_container_appointment, width=20)
    enter_date.grid(row=3, column=0, sticky="w", pady=5)
    
    label_error = tkinter.Label(frame_container_appointment, text="Veuillez remplir tout les champs", bg="#15AED6", fg="#15AED6", font=("Arial", 12, "bold"))
    label_error.grid(row=4, column=0, pady=5, sticky="w")
    
    bnt_validate_appoitment = tkinter.Button(frame_container_appointment, text="Prendre le rendez-vous", width=20, font=("Rubik", 14), bg="#0e7993", command=check_appoitment, relief="flat")
    bnt_validate_appoitment.grid(row=5, column=0, pady=5, sticky="w", ipadx=3, ipady=2)
    

def cancel_appointment():
    def delete_appointment(id_delete: str, *label_delete):
        for widget in label_delete:
            widget.grid_forget()
        
        for item in list_appointment:
            if item["id"] == id_delete:
                list_appointment.remove(item)
                recording_data(list_appointment, folder_clinique, "data_programme", "list_appoitment")
                break

    frame_container_appointment.place_forget()
    frame_container_see_notebook.place_forget()
    frame_container_cancel_appointment.place(x=80, y=150)
    
    title_date_appoitment = tkinter.Label(frame_container_cancel_appointment, bg="#15AED6", text="Date", font=("Arial", 18, "bold"))
    title_date_appoitment.grid(row=0, column=0, sticky="w")
    
    label_doctor = tkinter.Label(frame_container_cancel_appointment, bg="#15AED6", text="Medecin", font=("Arial", 18, "bold"))
    label_doctor.grid(row=0, column=1, padx=75)
    
    i = 1
    for appoitment in list_appointment:
        if appoitment["phone"] == _ID["phone"]:
            date = appoitment["data_appointment"]
            specialist = appoitment["choice_specialist"]
            
            label_date = tkinter.Label(frame_container_cancel_appointment, text=date, bg="#15AED6", fg="#1C1C1C", font=("Rubik", 13))
            label_date.grid(row=i, column=0, sticky="w")
        
            label_specialist = tkinter.Label(frame_container_cancel_appointment, text=specialist, bg="#15AED6", fg="#1C1C1C", font=("Rubik", 13))
            label_specialist.grid(row=i, column=1, sticky="w", padx=75, pady=10)
            
            bnt_cancel = tkinter.Button(frame_container_cancel_appointment, text="Anuler", bg="#0e7993", fg="#1C1C1C", font=("Rubik", 13 , "bold"))
            bnt_cancel.grid(row=i, column=2)  
            bnt_cancel["command"] = partial(delete_appointment, appoitment["id"], label_date, label_specialist, bnt_cancel)
            i += 1 
    
    
def see_notebook():
    frame_container_appointment.place_forget()
    frame_container_cancel_appointment.place_forget()
    frame_container_see_notebook.place(x=100, y=100)
    
    i = 0
    for item in list_reason:
        print("boucle")
        if item["phone"] == _ID["phone"]:
            print("oui")
            infos_appoitment = item["name_doctor"] + "\t\t\t\t\t\t       "+ item["date"]
            frame_infos = tkinter.Frame(frame_container_see_notebook, bg="#15AED6")
            frame_infos.grid(row=i, column=0)
            
            label_reason = tkinter.Label(frame_infos, text=item["reason"], justify="left", wraplength=350, bg="#15AED6")
            label_reason.grid(row=i, column=0, pady=8, sticky="w")
            
            label_doctor = tkinter.Label(frame_infos, bg="#15AED6", fg="white", text=infos_appoitment)
            label_doctor.grid(row=i+1, column=0, sticky="w")
            
            i += 1


# Fenêtre principale
window = tkinter.Tk()
window.geometry("1080x720")
window.title("Clinique Popo")
window.resizable(False, False)
window["bg"] = "white"

frame_1 = tkinter.Frame(window, bg="white", width=540)
frame_1.pack(side="left", fill="y")

frame_2 = tkinter.Frame(window, bg="#15AED6", width=540)
frame_2.pack(side="right", fill="y")

frame_main = tkinter.Frame(frame_2, bg="#15AED6")
frame_main.place(x=80, y=200)

frame_container_connection = tkinter.Frame(frame_2, bg="#15AED6")
frame_container_registration = tkinter.Frame(frame_2, bg="#15AED6")
frame_container_appointment = tkinter.Frame(frame_2, bg="#15AED6")
frame_container_cancel_appointment = tkinter.Frame(frame_2, bg="#15AED6")
frame_container_see_notebook = tkinter.Frame(frame_2, bg="#15AED6")

frame_container_img = tkinter.Frame(frame_1, bg="white", width=540)
frame_container_img.pack(side="left", fill="y")

frame_title = tkinter.Frame(frame_main, bg="#15AED6")
frame_title.grid(row=0, column=0, pady=20)

image = Image.open(path_img)
image_redimentionner = image.resize((300, 300))
image_final = ImageTk.PhotoImage(image_redimentionner)

image_label = tkinter.Label(frame_container_img, image=image_final, bg='white')
image_label.place(x= 80, y=170)

label_title_1 = tkinter.Label(frame_title, text="Un patrimoine en soins.\n Une réputation d'excellence.", font=("Rubik", 24), bg="#15AED6", fg="white", justify="left")
label_title_1.grid(row=1, column=0, sticky="w")

bnt_register = tkinter.Button(frame_main, text="S'inscrire", bg="#0e7993", width=8, height=2, font=("Arial", 12), command=recording_clients)
bnt_register.grid(row=3, column=0, sticky="w", pady=15)

bnt_connect = tkinter.Button(frame_main, text="Se connecter", bg="#0e7993", width=10, height=2, font=("Arial", 12), command=connection)
bnt_connect.grid(row=4, column=0, sticky="w", pady=5)

window.mainloop()