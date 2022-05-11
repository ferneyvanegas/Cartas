class Jugador:
    def __init__(self, nick, puntaje, turno):
        self.nick = nick
        self.puntaje = puntaje
        self.turno = turno
    
    def incrementar_puntaje(self):
        self.puntaje+=1
    
    def restablecer_puntaje(self):
        self.puntaje = 0
    
    def __str__(self):
        return f"{self.turno}: {self.nick}"