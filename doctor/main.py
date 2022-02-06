import os
import tkinter
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
        
    label_title = tkinter.Label(frame_container_connection, text="Connectez-vous", bg="#15AED6", font=("Arial", 24, "bold"))
    label_title.grid(row=0, column=0, pady=15)
    
    label_registation_number = tkinter.Label(frame_container_connection, text="Matricule", bg="#15AED6", font=("Rubik", 16), fg="#1C1C1C")
    label_registation_number.grid(row=1, column=0, sticky="w")
    
    enter_registation_number = tkinter.Entry(frame_container_connection)
    enter_registation_number.grid(row=2, column=0, sticky="w", pady=5)
    
    label_password = tkinter.Label(frame_container_connection, text="Mot de passe:", bg="#15AED6", font=("Rubik", 16), fg="#1C1C1C")
    label_password.grid(row=3, column=0, sticky="w")
    
    enter_password = tkinter.Entry(frame_container_connection)
    enter_password.grid(row=4, column=0, sticky="w", pady=5)
    
    label_error = tkinter.Label(frame_container_connection, text="Impossible de vous connecter", fg="#15AED6", bg="#15AED6", font=("Arial", 12, "bold"))
    label_error.grid(row=5, column=0, sticky="w", pady=7)
    
    bnt_connect = tkinter.Button(frame_container_connection, text="Se connecter", width=10, height=2, bg="#0e7993", command=check_connection, font=("Rubik", 13))
    bnt_connect.grid(row=6, column=0, pady=5, sticky="w")
 
 
def window_doctor():
    frame_container_connection.place_forget()
    frame_container_see_appoitment.place_forget()
    frame_container_see_notebook.place_forget()
    frame_container_img.pack_forget()

    frame_menu = tkinter.Frame(frame_1, bg="white")
    frame_menu.place(x=0, y=110)
    
    bnt_see_appoitment = tkinter.Button(frame_menu, text="Voir les rendez-vous", bg="#eaeaea", width=76, height=3, command=see_appoitment, relief="raised")
    bnt_see_appoitment.grid(row=0, column=0, pady=50)
    
    bnt_fill_notebook = tkinter.Button(frame_menu, text="Remplir un canet de santé", bg="#eaeaea", width=76, height=3, relief="raised")
    bnt_fill_notebook.grid(row=1, column=0, pady=50)
    
    bnt_modify_notebook = tkinter.Button(frame_menu, text="Modifier un canet de sante", bg="#eaeaea", width=76, height=3, relief="raised")
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
    frame_container_see_appoitment.place(x=80, y=150)
    
    title_date_appoitment = tkinter.Label(frame_container_see_appoitment, bg="#15AED6", text="Nom", font=("Arial", 18, "bold"))
    title_date_appoitment.grid(row=0, column=0, sticky="w")
    
    label_doctor = tkinter.Label(frame_container_see_appoitment, bg="#15AED6", text="Prénom", font=("Arial", 18, "bold"))
    label_doctor.grid(row=0, column=1, padx=75)
    
    i = 1
    for appoitment in list_appointment:
        if appoitment["choice_specialist"] == _ID["specialist"]:       
            label_last_name = tkinter.Label(frame_container_see_appoitment, text=appoitment["last_name"], bg="#15AED6", fg="#1C1C1C", font=("Rubik", 13))
            label_last_name.grid(row=i, column=0, sticky="w", padx=75, pady=10)
             
            label_firs_name = tkinter.Label(frame_container_see_appoitment, text=appoitment["firs_name"], bg="#15AED6", fg="#1C1C1C", font=("Rubik", 13))
            label_firs_name.grid(row=i, column=1, sticky="w", padx=75, pady=10)
            
            bnt_cancel = tkinter.Button(frame_container_see_appoitment, text="Accepter", bg="#0e7993", fg="#1C1C1C", font=("Rubik", 13 , "bold"), relief="flat")
            bnt_cancel.grid(row=i, column=2)  
            i += 1 


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
frame_container_see_appoitment = tkinter.Frame(frame_2, bg="#15AED6")
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

label_title_1 = tkinter.Label(frame_title, justify="left", text="Ensemble, prenons soin de \nvotre santé", font=("Rubik", 24), bg="#15AED6", fg="white")
label_title_1.grid(row=1, column=0, sticky="w")

bnt_connect = tkinter.Button(frame_main, text="Se connecter", bg="#0e7993", width=10, height=2, font=("Arial", 12), command=connection)
bnt_connect.grid(row=4, column=0, sticky="w", pady=5)


window.mainloop()