from tkinter import *
from PIL import Image, ImageTk


class Carta():
    #Valores de estado: 0=Oculta 1=Revelada 2=Encontrada(Bloqueada)
    estado = 0
    posX = 0
    posY = 0
    def __init__(self, campo, index):
        #Identificacion de la Carta
        self.id = index

        #Valor de la carta
        self.faceAlfa = Image.open(f".\img\cartas\{index}.png")
        self.faceAlfa = self.faceAlfa.resize((100, 110), Image.ANTIALIAS)
        self.faceAlfa = ImageTk.PhotoImage(self.faceAlfa)

        #Valor de la carta cuando está oculta
        self.faceBeta = Image.open(f".\img\cartas\\0.png")
        self.faceBeta = self.faceBeta.resize((110, 120), Image.ANTIALIAS)
        self.faceBeta = ImageTk.PhotoImage(self.faceBeta)

        #Se crea la carta y se mantiene la referencia a su imagen
        self.carta = Label(campo, relief="ridge", borderwidth=2, width="110", height="140", bg="white", image=self.faceAlfa)
        self.carta.image_names = self.faceAlfa

        #Se crea la carta volteada y se mantiene la referencia a su imagen
        self.carta_volteada = Label(campo, relief="ridge", borderwidth=2, width="110", height="140", bg="white", image=self.faceBeta)
        self.carta_volteada.image_names = self.faceBeta

        #Con el evento de click izquierdo, se llaama la función accionar_carta
        self.carta_volteada.bind('<Button-1>', lambda accionar :self.accionar_carta(accionar, campo))

    #Función para posicionar una carta
    def ubicar_carta(self, pos_x, pos_y):
        self.posX = pos_x
        self.posY = pos_y
        self.carta.grid(row=pos_x, column=pos_y)
        self.carta_volteada.grid(row=pos_x, column=pos_y)

    #Función para revelar una carta
    def revelar_cara(self):
        # self.carta.config(image=self.faceAlfa)
        # self.carta.image_names = self.faceAlfa
        self.carta_volteada.grid_forget()
        self.estado = 1

    #Función para esconder una carta
    def esconder_cara(self):
        if self.estado != 0:
            # self.carta.config(image=self.faceBeta)
            # self.carta.image_names = self.faceBeta
            self.carta_volteada.grid(row=self.posX, column=self.posY)
            self.estado = 0

    #Función que cambia el estado de una carta, al clickearse sobre ella
    def accionar_carta(self, event, campo):
        if self.estado != 1:
            self.revelar_cara()
            campo.obtener_carta(self)
    

