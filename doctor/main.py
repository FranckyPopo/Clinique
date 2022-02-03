import tkinter
from fonctions_doctor import fonctionnality_doctor

window = tkinter.Tk()
window.geometry("1080x720")
window.title("Clinique Popo")
window.minsize(1080, 720)

frame_1 = tkinter.Frame(window, bg="#FFFFFF", width=540)
frame_1.pack(fill="y", side="left")

frame_2 = tkinter.Frame(window, bg="#15AED6", width=540)
frame_2.pack(fill="y", side="right")

image = None

window.mainloop()