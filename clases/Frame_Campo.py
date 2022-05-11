from tkinter import *
from tkinter import messagebox
import time
import random
import threading

from clases.Carta import *

class Frame_Campo(Frame):
    pass
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.listaCartas = []

        super().__init__()

        self.primeraCarta = ''
        self.segundaCarta = ''

        #messagebox.showinfo("sda", "sdfa")

        #Llenar la lista
        for i in range(12):#Número de cartas existentes
            for j in range(2): #Número de veces que aparecerá la carta
                self.listaCartas.append(i + 1)
        
        #Barajar la lista
        random.shuffle(self.listaCartas)

        x = 0 #Filas 
        y = 0 #Columnas
        num_carta = 1 #Se pone con el fin de visualizar e identificar un número de carta al jugador
        for c in self.listaCartas:#CartaId
            Carta(self, c).ubicar_carta(x, y)
            Label(self, text=f"{num_carta}", font=("times",15,"bold"), fg="DeepSkyBlue4").grid(row=x, column=y, sticky="nw")
            num_carta+=1
            if y == 5: #Número de Columnas + 1 en que se distribuirán las cartas
                y = 0
                x+=1
            else:
                y+=1


    #Función que recibe un objeto y lo carga. Solo pueden existir dos cartas activas en el tiempo
    #Una vez haya dos cartas activas, permite la carga y emplea un hilo que se ejecuta a los dos segundos, evaluando si las cartas son iguales ó no lo son
    def obtener_carta(self, carta):
        #La primera condicional permite que solo se evalue dos cartas a  la vez y controla que le usuario no escoja más cartas
        if self.primeraCarta == '' or self.segundaCarta == '':
            if self.primeraCarta == '':
                self.primeraCarta = carta

            elif self.segundaCarta == '':
                self.segundaCarta = carta

                evaluacion = threading.Thread(target=self.evaluar_cartas)
                evaluacion.start()
        else:
            carta.esconder_cara()
    
    #Hilo que evalua si las cartas son iguales ó no lo son.
    def evaluar_cartas(self):   
        time.sleep(2)
        if self.primeraCarta.id == self.segundaCarta.id: 
            #Cartas iguales
            self.jugadores.incrementar_puntaje_jugador()
            
        else:
            #Cartas diferentes
            #print(self.jugadores.incrementar_puntaje_jugador())

            #Devolver Cartas a su estado original
            self.primeraCarta.esconder_cara()
            self.segundaCarta.esconder_cara()
        
        self.primeraCarta = ''
        self.segundaCarta = ''
        self.jugadores.activar_turno()

            
    