#from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import sys

#Procedimientos
from procedimientos.pro_game import *

class Frame_Superior(Frame):
    pass
    def __init__(self):
        super().__init__()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.config(bg="deep sky blue")
        self.lb_titulo = Label(self, text="Juego de cartas Familia", font=("Times", 18, "bold"), bg="deep sky blue", foreground="white")
        self.lb_titulo.grid(row=0, column=0)

        
        #Botón para Salir del sistema
        self.img_salir = Image.open(".\img\salir.png")
        self.img_salir = self.img_salir.resize((70,40), Image.ANTIALIAS)
        self.img_salir = ImageTk.PhotoImage(self.img_salir)
        self.btn_salir = Button(self, image=self.img_salir, command=salir, borderwidth=0, bg="deep sky blue")
        self.btn_salir.grid(row=0, column=1)
    