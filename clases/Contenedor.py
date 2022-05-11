from tkinter import *
from tkinter import messagebox
from clases.Frame_Superior import *
from clases.Frame_Jugadores import *
from clases.Frame_Campo import *

class Contendor(Frame):
    pass
    def __init__(self, main_w):
        super().__init__()
        #Control para crear campos de cartas
        self.campo_creado = 0

        #Configuación de Ventana
        main_w.title("Juego de Cartas de la Familia Vanegas Ruiz")
        main_w.iconbitmap(".\img\moroni.ico")
        main_w.config(bg="dodger blue")
        main_w.columnconfigure(0, weight=1)
        main_w.columnconfigure(1, weight=1)

        #Frame Superior
        Frame_Superior().grid(row=0, column=0, columnspan=2, sticky="we")

        #Frame Jugadores
        self.crear_jugadores()
    

    #Funciones Jugadores
    def crear_jugadores(self):
        self.jugadores = Frame_Jugadores(self)
        self.jugadores.grid(row=1, column=0, padx=20, pady=20, sticky="nw")
    
    def reset_jugadores(self):
        self.jugadores.grid_forget()
        self.crear_jugadores()

    #Funciones Campo
    def crear_campo(self):
        self.campo = Frame_Campo(self.jugadores)
        self.campo.config(bg="dodger blue")
        self.campo.grid(row=1, column=1, sticky="snew")
        self.campo_creado = 1
    
    def reset_campo(self):
        try:
            self.campo.grid_forget()
            self.crear_campo()
        except:
            messagebox.showinfo("Atención", "Debes iniciar primero una partida")
    
    