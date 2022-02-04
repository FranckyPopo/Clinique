import tkinter
from PIL import Image, ImageTk

window = tkinter.Tk()
window.geometry("1080x720")
window.title("Clinique Popo")
window.resizable(False, False)
window["bg"] = "black"

frame_1 = tkinter.Frame(window, bg="white", width=540)
frame_1.pack(side="left", fill="y")

frame_2 = tkinter.Frame(window, bg="#15AED6", width=540)
frame_2.pack(side="right", fill="y")

frame_container = tkinter.Frame(frame_2, bg="#15AED6")
frame_container.place(x=80, y=200)

frame_title = tkinter.Frame(frame_container, bg="#15AED6")
frame_title.grid(row=0, column=0, pady=20)

image = Image.open(r'C:\Users\HP\Documents\Projet_Nan\clinique\img\png-clipart-health-care-logo-no-cards-s-love-blue.jpeg')
image_redimentionner = image.resize((300, 300))
image_final = ImageTk.PhotoImage(image_redimentionner)

image_label = tkinter.Label(frame_1, image=image_final, bg='white')
image_label.place(x= 140, y=210)

label_title_1 = tkinter.Label(frame_title, text="Un patrimoine en soins.", font=("Rubik", 24), bg="#15AED6", fg="white")
label_title_1.grid(row=1, column=0, sticky="w")

label_title_2 = tkinter.Label(frame_title, text="Une réputation d'excellence.", font=("Rubik", 24), bg="#15AED6", fg="white")
label_title_2.grid(row=2, column=0, sticky="w")

bnt_register = tkinter.Button(frame_container, text="S'inscrire", bg="#0e7993", width=8, height=2, font=("Arial", 12))
bnt_register.grid(row=3, column=0, sticky="w", pady=15)

bnt_connect = tkinter.Button(frame_container, text="Se connecter", bg="#0e7993", width=10, height=2, font=("Arial", 12))
bnt_connect.grid(row=4, column=0, sticky="w", pady=5)


window.mainloop()