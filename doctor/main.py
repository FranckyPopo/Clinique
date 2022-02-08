import tkinter
from PIL import Image, ImageTk
from fonctions_doctor import fonctionnality_doctor

window = tkinter.Tk()
window.geometry("1080x720")
window.title("Clinique Popo")
window.minsize(1080, 720)

window["bg"] = "White"
# frame_1 = tkinter.Frame(window, bg="#FFFFFF", width=540)
# frame_1.pack(fill="y", side="left")

frame_2 = tkinter.Frame(window, bg="#15AED6", width=540)
frame_2.pack(fill="y", side="right")

image = Image.open('/Users/imac-20/Desktop/afri/COURS NAN/COUR_PYTHON_GENERALE/PythonExercice/Clinique/img/kisspng-hospital-logo-clinic-health-care-physician-5b48c1801f8383.2739660215314947841291.gif')
python_image = ImageTk.PhotoImage(image)
image_label = tkinter.Label(window, image=python_image)
image_label.pack()

window.mainloop()