class Jugador:
    def __init__(self, numero_jugador, tipo="humano", nombre=None):
        """
        Asigna "X" al primer jugador y "O" al segundo.
        Si se quiere personalizar, se puede pasar el símbolo directamente.
        """
        if numero_jugador == 1:
            self.simbolo = "X"
        elif numero_jugador == 2:
            self.simbolo = "O"
        else:
            raise ValueError("Número de jugador debe ser 1 o 2.")

        self.tipo = tipo        # "humano" o "ia"
        self.nombre = nombre    # Opcional (ej: "Jugador 1")

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
        else:  # IA básica (elige aleatoriamente)
            from random import choice
            posiciones_vacias = [i for i, celda in enumerate(tablero.celdas) if celda == " "]
            return choice(posiciones_vacias)