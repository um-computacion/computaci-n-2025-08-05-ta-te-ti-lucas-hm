import random

class Jugador:
    def __init__(self, numero_jugador, tipo="humano", nombre=None):
        self.simbolo = "X" if numero_jugador == 1 else "O"
        self.tipo = tipo
        self.nombre = nombre or f"Jugador {numero_jugador}"

    def elegir_movimiento(self, tablero):
        if self.tipo == "humano":
            while True:
                try:
                    posicion = int(input(f"{self.nombre} ({self.simbolo}), elige posición (0-8): "))
                    if 0 <= posicion <= 8 and tablero.celdas[posicion] == " ":
                        return posicion
                    print("¡Posición inválida o ocupada! Intenta de nuevo.")
                except ValueError:
                    print("Ingresa un número del 0 al 8.")
        else:
            posiciones_vacias = [i for i, celda in enumerate(tablero.celdas) if celda == " "]
            return random.choice(posiciones_vacias)