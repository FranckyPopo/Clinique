import tkinter
import os
from PIL import Image, ImageTk
from fonctions.data import get_data, recording_data
from fonctions import fonctionnality

folder_clinique = os.getcwd().replace("patient", "")
folder_img = os.path.join(folder_clinique, "img")
path_img = folder_img + "/" + "—Pngtree—healthcare medical logo vector icon_5059582.png"

folder_data = os.path.join(folder_clinique, "data")
list_patients = get_data(folder_data, "list_patients")
list_appointment = get_data(folder_data, "list_appoitment")


def recording_clients():
    def check_registration():
        last_name = enter_last_name.get()
        firs_name = enter_firs_name.get()
        telephone = enter_phone.get()
        password = enter_password.get()
        
        
        if last_name and firs_name and telephone.isdigit() and password:
            print("oui passe")
            _id = fonctionnality.creation_id(list_patients, "id")
            
            data_patient = {
                "id": _id,
                "last_name": last_name,
                "firs_name": firs_name,
                "telephone": telephone,
                "password": password
            }
            list_patients.append(data_patient)
            recording_data(list_patients, folder_clinique, "data_programme", "list_patients")
            
            label_error["fg"] = "#15AED6"
        else:
            label_error["fg"] = "#FA0000"
    
    for widget in frame_container.winfo_children():
        widget.grid_forget()
        
    frame_container.place(x=150, y=140) 
        
    label_title = tkinter.Label(frame_container, text="Crée votre compte", bg="#15AED6", font=("Arial", 24, "bold"))
    label_title.grid(row=0, column=0, pady=20, sticky="w")
    
    label_last_name = tkinter.Label(frame_container, text="Nom:", bg="#15AED6", font=("Rubik", 16), fg="#1C1C1C")
    label_last_name.grid(row=1, column=0, sticky="w")
    
    enter_last_name = tkinter.Entry(frame_container, width=30)
    enter_last_name.grid(row=2, column=0, sticky="w", pady=5)
    
    label_firs_name = tkinter.Label(frame_container, text="Prénom:", bg="#15AED6", font=("Rubik", 16), fg="#1C1C1C")
    label_firs_name.grid(row=3, column=0, sticky="w")
    
    enter_firs_name = tkinter.Entry(frame_container, width=30)
    enter_firs_name.grid(row=4, column=0, sticky="w", pady=5)
    
    label_phone = tkinter.Label(frame_container, text="Téléphone:", bg="#15AED6", font=("Rubik", 16), fg="#1C1C1C")
    label_phone.grid(row=5, column=0, sticky="w")
    
    enter_phone = tkinter.Entry(frame_container, width=30)
    enter_phone.grid(row=6, column=0, sticky="w", pady=5)
    
    label_password = tkinter.Label(frame_container, text="Mot de passe:", bg="#15AED6", font=("Rubik", 16), fg="#1C1C1C")
    label_password.grid(row=7, column=0, sticky="w")
    
    enter_password = tkinter.Entry(frame_container, width=30)
    enter_password.grid(row=8, column=0, sticky="w", pady=5)

    label_error = tkinter.Label(frame_container, text="Veuillez remplir tout les champs", fg="#15AED6", bg="#15AED6", font=("Arial", 12, "bold"))
    label_error.grid(row=9, column=0, sticky="w", pady=5)
    
    bnt_registration = tkinter.Button(frame_container, text="S'inscrir", bg="#0e7993", width=8, height=2, font=("arial", 13, "bold"), command=check_registration)
    bnt_registration.grid(row=10, column=0, sticky="w", pady=5) 
    

# Fenêtre principale
window = tkinter.Tk()
window.geometry("1080x720")
window.title("Clinique Popo")
window.resizable(False, False)

frame_1 = tkinter.Frame(window, bg="white", width=540)
frame_1.pack(side="left", fill="y")

frame_2 = tkinter.Frame(window, bg="#15AED6", width=540)
frame_2.pack(side="right", fill="y")

frame_container = tkinter.Frame(frame_2, bg="#15AED6")
frame_container.place(x=80, y=200)

frame_title = tkinter.Frame(frame_container, bg="#15AED6")
frame_title.grid(row=0, column=0, pady=20)

image = Image.open(path_img)
image_redimentionner = image.resize((300, 300))
image_final = ImageTk.PhotoImage(image_redimentionner)

image_label = tkinter.Label(frame_1, image=image_final, bg='white')
image_label.place(x= 80, y=170)

label_title_1 = tkinter.Label(frame_title, text="Un patrimoine en soins.", font=("Rubik", 24), bg="#15AED6", fg="white")
label_title_1.grid(row=1, column=0, sticky="w")

label_title_2 = tkinter.Label(frame_title, text="Une réputation d'excellence.", font=("Rubik", 24), bg="#15AED6", fg="white")
label_title_2.grid(row=2, column=0, sticky="w")

bnt_register = tkinter.Button(frame_container, text="S'inscrire", bg="#0e7993", width=8, height=2, font=("Arial", 12), command=recording_clients)
bnt_register.grid(row=3, column=0, sticky="w", pady=15)


bnt_connect = tkinter.Button(frame_container, text="Se connecter", bg="#0e7993", width=10, height=2, font=("Arial", 12))
bnt_connect.grid(row=4, column=0, sticky="w", pady=5)


window.mainloop()