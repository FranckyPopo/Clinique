import tkinter
from tkinter import messagebox
import os
from datetime import datetime
from PIL import Image, ImageTk
from data import get_data, recording_data

# Chemin pour les images
folder_clinique = os.getcwd().replace("doctor", "")
folder_img = os.path.join(folder_clinique, "img")
path_img = folder_img + "/" + "—Pngtree—healthcare medical logo vector icon_5059582.png"

# Chemin pour les fichiers json 
folder_data = os.path.join(folder_clinique, "data_programme")
list_patients = get_data(folder_data, "list_patients")
list_appointment = get_data(folder_data, "list_appoitment")
list_reason = get_data(folder_data, "list_reason")
list_notebook = get_data(folder_data, "list_notebook")

list_doctors = [
    {
        "name_doctor": "Afri Franck",
        "specialist": "Genéraliste",
        "registation_number": "AAAA1",
        "password": "AAAA1"
    },
    {
        "name_doctor": "Kreto Ariel",
        "specialist": "Dentiste",
        "registation_number": "AAAA2",
        "password": "AAAA2"
    },
    {
        "name_doctor": "Francky Popo",
        "specialist": "Dermatologue",
        "registation_number": "AAAA3",
        "password": "AAAA3"
    },
    {
        "name_doctor": "Francky Pigeon",
        "specialist": "Neurologue",
        "registation_number": "AAAA4",
        "password": "AAAA4"
    },
    {
        "name_doctor": "Francky Popo",
        "specialist": "Génécolgue",
        "registation_number": "AAAA5",
        "password": "AAAA5"
    }
]
_ID = {}

def connection():
    def check_connection():
        password = enter_password.get()
        registation_number = enter_registation_number.get()        

        if password and registation_number:
            for item in list_doctors:
                if item.get("registation_number") == registation_number and item.get("password") == password:
                    label_error["fg"] = "#15AED6"
                    enter_password.delete(0, "end")
                    enter_registation_number.delete(0, "end")
                    
                    # Récupération des information du docteur
                    for key, value in item.items():
                        _ID[key] = value
                    
                    window_doctor()
                    break
            else:
                label_error["fg"] = "#FA0000"    
        else:
            label_error["fg"] = "#FA0000"
    
    frame_main.place_forget()
    
    frame_container_connection.place(x=150, y=140)  
        
    label_title = tkinter.Label(frame_container_connection, text="Connectez-vous", bg="#15AED6", fg="#1C1C1C", font=("Rubik", 24, "bold"))
    label_title.grid(row=0, column=0, pady=15)
    
    label_registation_number = tkinter.Label(frame_container_connection, text="Matricule:", bg="#15AED6", font=("Rubik", 16), fg="#1C1C1C")
    label_registation_number.grid(row=1, column=0, sticky="w")
    
    enter_registation_number = tkinter.Entry(frame_container_connection)
    enter_registation_number.grid(row=2, column=0, sticky="w", pady=5)
    
    label_password = tkinter.Label(frame_container_connection, text="Mot de passe:", bg="#15AED6", font=("Rubik", 16), fg="#1C1C1C")
    label_password.grid(row=3, column=0, sticky="w")
    
    enter_password = tkinter.Entry(frame_container_connection)
    enter_password.grid(row=4, column=0, sticky="w", pady=5)
    
    label_error = tkinter.Label(frame_container_connection, text="Impossible de vous connecter", fg="#15AED6", bg="#15AED6", font=("Rubik   ", 12, "bold"))
    label_error.grid(row=5, column=0, sticky="w", pady=7)
    
    bnt_connect = tkinter.Button(frame_container_connection, text="Se connecter", bg="#0e7993", command=check_connection, font=("Rubik", 13), relief="flat")
    bnt_connect.grid(row=6, column=0, pady=5, sticky="w", ipadx=5, ipady=2)
 
 
def window_doctor():
    frame_container_connection.place_forget()
    frame_container_see_appoitment.place_forget()
    frame_container_see_notebook.place_forget()
    frame_container_img.pack_forget()

    frame_menu = tkinter.Frame(frame_1, bg="white")
    frame_menu.place(x=0, y=110)
    
    bnt_see_appoitment = tkinter.Button(frame_menu, text="Voir les rendez-vous", bg="#eaeaea", width=76, height=3, command=see_appoitment, relief="raised")
    bnt_see_appoitment.grid(row=0, column=0, pady=50)
    
    bnt_fill_notebook = tkinter.Button(frame_menu, text="Remplir un canet de santé", bg="#eaeaea", width=76, height=3, relief="raised", command=fill_notebook)
    bnt_fill_notebook.grid(row=1, column=0, pady=50)
    
    bnt_modify_notebook = tkinter.Button(frame_menu, text="Modifier un canet de sante", bg="#eaeaea", width=76, height=3, relief="raised", command=modify_notebook)
    bnt_modify_notebook.grid(row=2, column=0, pady=50)


def see_appoitment():
    def delete_appointment(id_delete: str, *label_delete):
        for widget in label_delete:
            widget.grid_forget()
        
        for item in list_appointment:
            if item["id"] == id_delete:
                list_appointment.remove(item)
                recording_data(list_appointment, folder_clinique, "data_programme", "list_appoitment")
                break

    frame_container_see_notebook.place_forget()
    frame_container_fill_notebook.place_forget()
    frame_container_modify_notebook.place_forget()
    frame_container_test.place_forget()
    frame_container_see_appoitment.place(x=80, y=150)
    
    title_date_appoitment = tkinter.Label(frame_container_see_appoitment, bg="#15AED6", text="Nom", font=("Rubik", 18, "bold"))
    title_date_appoitment.grid(row=0, column=0, sticky="w")
    
    label_doctor = tkinter.Label(frame_container_see_appoitment, bg="#15AED6", text="Prénom", font=("Rubik", 18, "bold"))
    label_doctor.grid(row=0, column=1, padx=75)
    
    i = 1
    for appoitment in list_appointment:
        if appoitment["choice_specialist"] == _ID["specialist"]:       
            label_last_name = tkinter.Label(frame_container_see_appoitment, text=appoitment["last_name"], bg="#15AED6", fg="#1C1C1C", font=("Rubik", 13))
            label_last_name.grid(row=i, column=0, sticky="w", pady=10)
             
            label_firs_name = tkinter.Label(frame_container_see_appoitment, text=appoitment["firs_name"], bg="#15AED6", fg="#1C1C1C", font=("Rubik", 13))
            label_firs_name.grid(row=i, column=1, sticky="w", padx=75, pady=10)
            
            bnt_cancel = tkinter.Button(frame_container_see_appoitment, text="Accepter", bg="#0e7993", fg="#1C1C1C", font=("Rubik", 13 , "bold"), relief="flat")
            bnt_cancel.grid(row=i, column=2, sticky="w")  
            i += 1 


def fill_notebook():
    def check_fill_notebook():
        id_patient = enter_id.get()
        reason = enter_reason.get(1.0, "end")
        
        for item in list_appointment:
            for patient in list_patients: 
                if item["id"] == id_patient and reason != "\n" and patient["phone"] == item["phone"]:
                    date_day = datetime.today().strftime('%d-%m-%Y')
                    notebook = {
                        "phone": item["phone"],
                        "id": id_patient, 
                        "reason": reason, 
                        "name_doctor": _ID["name_doctor"],
                        "date": date_day
                    }
                    list_notebook.append(notebook)
                    recording_data(list_notebook, folder_clinique, "data_programme", "list_notebook")
                    label_error["fg"] = "#15AED6"

                    enter_id.delete(0, "end")
                    enter_reason.delete(1.0, "end")
                    
                    list_appointment.remove(item)
                    recording_data(list_appointment, folder_clinique, "data_programme", "list_appoitment")

                    messagebox.showinfo("Consultation", "Le carnet a été  remplit avec succès")
                    break
            else:
                label_error["fg"] = "#FA0000"       
    
    frame_container_see_appoitment.place_forget()
    frame_container_see_notebook.place_forget()
    frame_container_modify_notebook.place_forget()
    frame_container_test.place_forget()
    frame_container_fill_notebook.place(x=160, y=140,)
    
    label_id = tkinter.Label(frame_container_fill_notebook, bg="#15AED6", text="Identifiant du rendez-vous", font=("Rubik", 18))
    label_id.grid(row=0, column=0, pady=5, sticky="w")
    
    enter_id = tkinter.Entry(frame_container_fill_notebook, width=37)
    enter_id.grid(row=1, column=0, pady=5, sticky="w")
    
    label_reason= tkinter.Label(frame_container_fill_notebook, bg="#15AED6", text="Motif", font=("Rubik", 18))
    label_reason.grid(row=2, column=0, pady=5, sticky="w")
    
    enter_reason = tkinter.Text(frame_container_fill_notebook, width=20, height=10, font=("time new roman", 14), wrap="word")
    enter_reason.grid(row=3, column=0, pady=5, sticky="w")
    
    label_error = tkinter.Label(frame_container_fill_notebook, bg="#15AED6", fg="#15AED6",  text="Impossible de remplir le canet", font=("Rubik", 13, "bold"))
    label_error.grid(row=4, column=0, pady=5, sticky="w")
    
    bnt_fill_notebook = tkinter.Button(frame_container_fill_notebook, text="Remplir le canet", bg="#0e7993", font=("Rubik", 13), relief="flat", command=check_fill_notebook)
    bnt_fill_notebook.grid(row=5, column=0, pady=5, ipadx=3, ipady=2, sticky="w")
    

def modify_notebook():
    def check_id():

        def recording_new_notebook():
            new_reason = enter_new_reason.get(1.0, "end")
            if new_reason != "\n":
                item["reason"] = new_reason
                recording_data(list_notebook, folder_clinique, "data_programme", "list_notebook")
                enter_new_reason.delete(1.0, "end")
                messagebox.showinfo("Modification", "Le canet du patient a été modifier")
            else:
                label_error_2["fg"] = "#FA0000"
                        
        id_appointment = enter_id_appointment.get()
        for item in list_notebook:
            if item["id"] == id_appointment:
                frame_container_modify_notebook.place_forget()
                frame_container_test.place(x=120, y=180)
                
                label_new_reason = tkinter.Label(frame_container_test, text="Motif:", bg="#15AED6", font=("Rubik", 18))
                label_new_reason.grid(row=0, column=0, sticky="w", pady=5)
                
                enter_new_reason = tkinter.Text(frame_container_test, width=30, height=15)
                enter_new_reason.grid(row=1, column=0, sticky="w", pady=5)
                
                label_error_2 = tkinter.Label(frame_container_test, text="Veuillez remplir le champ", bg="#15AED6", fg="#15AED6",  font=("Rubik", 13, "bold"))
                label_error_2.grid(row=2, column=0, pady=5, sticky="w")
                
                bnt_validate = tkinter.Button(frame_container_test, bg="#0e7993", relief="flat", text="Remplir le canet", command=recording_new_notebook)
                bnt_validate.grid(row=3, column=0, ipadx=3, ipady=2, pady=5, sticky="w")
                break            
        else:
            label_error["fg"] = "red"

    frame_container_fill_notebook.place_forget()
    frame_container_see_appoitment.place_forget()
    frame_container_test.place_forget()
    frame_container_modify_notebook.place(x=150, y=200)
 
    label_id_appointment = tkinter.Label(frame_container_modify_notebook, text="Entrer l'id su rendez-vous", bg="#15AED6", fg="#1C1C1C", font=("Rubik", 18))
    label_id_appointment.grid(row=0, column=0, sticky="w", pady=3)
    
    enter_id_appointment = tkinter.Entry(frame_container_modify_notebook)
    enter_id_appointment.grid(row=1, column=0, sticky="w", pady=3)
    
    label_error = tkinter.Label(frame_container_modify_notebook, text="ID incorrect", bg="#15AED6", fg="#15AED6", font=("Rubik", 13, "bold"))
    label_error.grid(row=2, column=0, sticky="w", pady=3)
    
    bnt_validate_id_appoitment = tkinter.Button(frame_container_modify_notebook, relief="flat", text="Valider", command=check_id, bg="#0e7993")
    bnt_validate_id_appoitment.grid(row=3, column=0, sticky="w", ipadx=3, ipady=2, pady=3)
    

window = tkinter.Tk()
window.geometry("1080x720")
window.title("Clinique Popo")
window.resizable(False, False)

frame_1 = tkinter.Frame(window, bg="white", width=540)
frame_1.pack(side="left", fill="y")

frame_2 = tkinter.Frame(window, bg="#15AED6", width=540)
frame_2.pack(side="right", fill="y")

frame_main = tkinter.Frame(frame_2, bg="#15AED6")
frame_main.place(x=80, y=200)

frame_container_connection = tkinter.Frame(frame_2, bg="#15AED6")
frame_container_see_appoitment = tkinter.Frame(frame_2, bg="#15AED6")
frame_container_see_notebook = tkinter.Frame(frame_2, bg="#15AED6")
frame_container_fill_notebook = tkinter.Frame(frame_2, bg="#15AED6")
frame_container_modify_notebook = tkinter.Frame(frame_2, bg="#15AED6")
frame_container_test = tkinter.Frame(frame_2, bg="#15AED6")

frame_container_img = tkinter.Frame(frame_1, bg="white", width=540)
frame_container_img.pack(side="left", fill="y")

frame_title = tkinter.Frame(frame_main, bg="#15AED6")
frame_title.grid(row=0, column=0, pady=20)

image = Image.open(path_img)
image_redimentionner = image.resize((300, 300))
image_final = ImageTk.PhotoImage(image_redimentionner)

image_label = tkinter.Label(frame_container_img, image=image_final, bg='white')
image_label.place(x= 80, y=170)

label_title_1 = tkinter.Label(frame_title, justify="left", text="Ensemble, prenons soin de \nvotre santé", font=("Rubik", 24), bg="#15AED6", fg="white")
label_title_1.grid(row=1, column=0, sticky="w")

bnt_connect = tkinter.Button(frame_main, text="Se connecter", bg="#0e7993", font=("Rubik", 13), command=connection, relief="flat")
bnt_connect.grid(row=4, column=0, sticky="w", pady=5, ipadx=5, ipady=2)


window.mainloop()