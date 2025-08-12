from jugador import Jugador

class Tablero:
    def __init__(self):
        
        self.celdas = [" " for _ in range(9)]

    def mostrar_tablero(self):
        # Muestra el tablero actualizado
        print(f"{self.celdas[0]}|{self.celdas[1]}|{self.celdas[2]}")
        print("-" * 5)
        print(f"{self.celdas[3]}|{self.celdas[4]}|{self.celdas[5]}")
        print("-" * 5)
        print(f"{self.celdas[6]}|{self.celdas[7]}|{self.celdas[8]}")

    def actualizar_tablero(self, posicion):
        # Coloca la ficha (X/O) en la posición elegida
        if self.celdas[posicion] == " ":  # Si la casilla está vacía
            self.celdas[posicion] = Jugador.elegir_movimiento(posicion)
            return True  # Jugada válida
        else:
            return False  # Casilla ocupada
    def hay_ganador(self):
        self.jugada_ganador={
            (0, 4, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (2, 4, 6)
        }
    def empate(self):
        self.jugada_empate={
            (0, 4, 5),
            (0, 1, 2),
            (3, 4, 8),
            (3, 4, 5),
            (6, 7, 5),
            (6, 7, 8)
        }