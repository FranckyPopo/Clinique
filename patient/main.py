import tkinter
import os
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
    
    bnt_connect = tkinter.Button(frame_container_connection, text="Se connecter", width=10, height=2, bg="#0e7993", command=check_connection)
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
    frame_container_img.pack_forget()
    
    frame_menu = tkinter.Frame(frame_1, bg="white")
    frame_menu.place(x=0, y=110)
    
    bnt_appointment = tkinter.Button(frame_menu, text="Prendre rendez-vous", bg="#eaeaea", width=76, height=3)
    bnt_appointment.grid(row=0, column=0, pady=50)
    
    bnt_notebook = tkinter.Button(frame_menu, text="Prendre rendez-vous", bg="#eaeaea", width=76, height=3)
    bnt_notebook.grid(row=1, column=0, pady=50)
    
    bnt_cancel = tkinter.Button(frame_menu, text="Anuler un rendez-vous", bg="#eaeaea", width=76, height=3)
    bnt_cancel.grid(row=2, column=0, pady=50)


    

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

frame_container_img = tkinter.Frame(frame_1, bg="white", width=540)
frame_container_img.pack(side="left", fill="y")

frame_title = tkinter.Frame(frame_main, bg="#15AED6")
frame_title.grid(row=0, column=0, pady=20)

image = Image.open(path_img)
image_redimentionner = image.resize((300, 300))
image_final = ImageTk.PhotoImage(image_redimentionner)

image_label = tkinter.Label(frame_container_img, image=image_final, bg='white')
image_label.place(x= 80, y=170)

label_title_1 = tkinter.Label(frame_title, text="Un patrimoine en soins.", font=("Rubik", 24), bg="#15AED6", fg="white")
label_title_1.grid(row=1, column=0, sticky="w")

label_title_2 = tkinter.Label(frame_title, text="Une réputation d'excellence.", font=("Rubik", 24), bg="#15AED6", fg="white")
label_title_2.grid(row=2, column=0, sticky="w")

bnt_register = tkinter.Button(frame_main, text="S'inscrire", bg="#0e7993", width=8, height=2, font=("Arial", 12), command=recording_clients)
bnt_register.grid(row=3, column=0, sticky="w", pady=15)


bnt_connect = tkinter.Button(frame_main, text="Se connecter", bg="#0e7993", width=10, height=2, font=("Arial", 12), command=connection)
bnt_connect.grid(row=4, column=0, sticky="w", pady=5)


window.mainloop()