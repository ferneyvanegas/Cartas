from tkinter import *
from PIL import Image, ImageTk
from functools import partial #Para pasar parámetros a funcion con el command del botón
#Clases
from clases.Jugador import *

class Frame_Jugadores(Frame):
    def __init__(self, contenedor):
        super().__init__()

        self.config(bg="dodger blue")
        self.contenedor = contenedor
        self.jugadores = []
        self.turno = 0

        #PANEL DE OPCIONES

        #Botón para reiniciar Puntajes
        self.btn_reset_score = Image.open(".\img\\reset_score.png")
        self.btn_reset_score = self.btn_reset_score.resize((30, 30), Image.ANTIALIAS)
        self.btn_reset_score = ImageTk.PhotoImage(self.btn_reset_score)

        
        reset_juego = Button(self, image=self.btn_reset_score, borderwidth=0, command=self.reset_puntajes, bg="dodger blue")
        reset_juego.grid(row=0, column=0, sticky="we")
        
        #Botón para reiniciar Jugadores
        self.btn_reset_player = Image.open(".\img\\reset-player.png")
        self.btn_reset_player = self.btn_reset_player.resize((30, 30), Image.ANTIALIAS)
        self.btn_reset_player = ImageTk.PhotoImage(self.btn_reset_player)

        reset_juego = Button(self, image=self.btn_reset_player, borderwidth=0, command=self.contenedor.reset_jugadores, bg="dodger blue")
        reset_juego.grid(row=0, column=1, sticky="we")

        #Botón para reiniciar el Juego
        self.btn_reload = Image.open(".\img\\reload.png")
        self.btn_reload = self.btn_reload.resize((30, 30), Image.ANTIALIAS)
        self.btn_reload = ImageTk.PhotoImage(self.btn_reload)

        reset_juego = Button(self, image=self.btn_reload, borderwidth=0, command=self.contenedor.reset_campo, bg="dodger blue")
        reset_juego.grid(row=0, column=2, sticky="we")

        #Botón para iniciar a Jugar
        self.btn_play = Image.open(".\img\play.png")
        self.btn_play = self.btn_play.resize((30, 30), Image.ANTIALIAS)
        self.btn_play = ImageTk.PhotoImage(self.btn_play)

        iniciar_juego = Button(self, image=self.btn_play, borderwidth=0, command=self.activar_turno, bg="dodger blue")
        iniciar_juego.grid(row=0, column=3,  sticky="we")

        #Creación de nuevos jugadores
        #===================================================================
        Label(self, text="Nuevo Jugador", font=("Times", 12, "bold"), bg="dodger blue", foreground="white").grid(row=1, column=0, columnspan=3, sticky="we")

        self.nick = StringVar()
        self.txt_jugador = Entry(self, textvariable=self.nick, font=("times", 15, "bold"), bg="goldenrod2", fg="black", borderwidth=0)
        self.txt_jugador.grid(row=2, column=0, columnspan=3)

        self.btn_add = Image.open(".\img\plus.png")
        self.btn_add = self.btn_add.resize((30, 30), Image.ANTIALIAS)
        self.btn_add = ImageTk.PhotoImage(self.btn_add)
        self.btn_crear = Button(self, image=self.btn_add, command=self.crear_jugador, borderwidth=0, bg="dodger blue")
        self.btn_crear.grid(row=2, column=3)
        #===================================================================

        #Listado de Jugadores
        self.group = LabelFrame(self)
        self.group.grid(row=3, column=0, columnspan=4, sticky="we")
    
    #Función para crear y mostrar Jugadores
    def crear_jugador(self):
        if len(self.nick.get()) > 0 and len(self.nick.get()) < 15:
            #Se agrega el jugador a la lista
            nuevo_jugador = Jugador(self.nick.get(), 0, len(self.jugadores) + 1)
            self.jugadores.append(nuevo_jugador)
            self.nick.set("")

            self.visualizar_jugadores()
    
    #Funcion para quitar un jugador
    def eliminar_jugador(self, turno):
        #Elimina el objeto del array según el turno recibido
        for i in self.jugadores:
            if i.turno == turno:
                self.jugadores.pop(turno - 1)

        self.reasignar_turnos(turno)
        self.visualizar_jugadores()

    #Función para reasignar turnos. Se hace necesaria cada vez que se elimina un jugador
    def reasignar_turnos(self, turno_eliminado):
        turno_nuevo = 1
        for i in self.jugadores:
            i.turno = turno_nuevo
            turno_nuevo+=1
        #Si el turno eliminado fue el último que estaba activo, entonces el nuevo activo es el primero
        if self.turno > len(self.jugadores):
            self.turno = 1
        #Si el turno eliminado era anterior al turno actual, entonces el turno actual ahora estará un número antes
        elif self.turno > turno_eliminado:
            self.turno-=1

    #Función para activar un turno
    def activar_turno(self):
        if self.turno == len(self.jugadores):
            self.turno = 1
        elif  len(self.jugadores) != 0:
            self.turno+=1 #Avanza el turno en uno

        self.visualizar_jugadores()
        
        if self.contenedor.campo_creado == 0:
            self.contenedor.crear_campo()

    #Función para mostrar jugadores en el Frame
    def visualizar_jugadores(self):
        #Se elimina el LabelFrame
        self.group.destroy()
        self.group = LabelFrame(self, text="Jugadores", font=("Times", 12, "bold"), bg="dodger blue")
        self.group.grid(row=3, column=0, columnspan=4, sticky="we")

        #Ícono jugador
        self.avatar = Image.open(".\img\jugador_avatar.png")
        self.avatar = self.avatar.resize((30, 30), Image.ANTIALIAS)
        self.avatar = ImageTk.PhotoImage(self.avatar)

        #Ícono jugador con turno activo
        self.avatar_activo = Image.open(".\img\jugador_avatar_activo.png")
        self.avatar_activo = self.avatar_activo.resize((30, 30), Image.ANTIALIAS)
        self.avatar_activo = ImageTk.PhotoImage(self.avatar_activo)

        #Ícono moneda
        self.moneda = Image.open(".\img\moneda.png")
        self.moneda = self.moneda.resize((30, 30), Image.ANTIALIAS)
        self.moneda = ImageTk.PhotoImage(self.moneda)

        #Ícono borrar jugador
        self.borrar = Image.open(".\img\delete.png")
        self.borrar = self.borrar.resize((20, 20), Image.ANTIALIAS)
        self.borrar = ImageTk.PhotoImage(self.borrar)

        row_activa = 0

        for i in self.jugadores:
            #Se agrega el label al nuevo LabelFrame

            #Jugador
            if i.turno == self.turno:
                Label(self.group, image=self.avatar_activo, font=("times",15,"bold"), fg="DeepSkyBlue4", bg="dodger blue").grid(row=row_activa, column=0)

                Label(self.group, text=i, font=("times",15,"bold"), fg="green2", bg="dodger blue").grid(row=row_activa, column=1, sticky="w")
            else:
                Label(self.group, image=self.avatar, font=("times",15,"bold"), fg="DeepSkyBlue4", bg="dodger blue").grid(row=row_activa, column=0)

                Label(self.group, text=i, font=("times",15,"bold"), fg="white", bg="dodger blue").grid(row=row_activa, column=1, sticky="w")
            
            #Monedas (Puntaje)
            Label(self.group, image=self.moneda, font=("times",15,"bold"), fg="yellow", bg="dodger blue").grid(row=row_activa, column=2, padx=10)

            Label(self.group, text=f"x{i.puntaje}", font=("times",15,"bold"), fg="yellow", bg="dodger blue").grid(row=row_activa, column=3, sticky="w")
            
            #Botón Eliminar
            indice = i.turno - 1
            Button(self.group, image=self.borrar, command=partial(self.eliminar_jugador, i.turno), borderwidth=0, bg="dodger blue").grid(row=row_activa, column=4, padx=40)

            row_activa+=1
    
    def incrementar_puntaje_jugador(self):       
        for i in self.jugadores:
            if self.turno == i.turno:
                i.incrementar_puntaje()
    
    def reset_puntajes(self):
        for i in self.jugadores:
            i.puntaje = 0
        self.turno = 1
        self.visualizar_jugadores()
        
    





