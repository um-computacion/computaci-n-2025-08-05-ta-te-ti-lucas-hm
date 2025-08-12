class Tablero:
    def __init__(self):
        self.celdas = [" " for _ in range(9)]
        self.lineas_ganadoras = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontales
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Verticales
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]

    def mostrar_tablero(self):
        print(f"\n{self.celdas[0]}|{self.celdas[1]}|{self.celdas[2]}")
        print("-" * 5)
        print(f"{self.celdas[3]}|{self.celdas[4]}|{self.celdas[5]}")
        print("-" * 5)
        print(f"{self.celdas[6]}|{self.celdas[7]}|{self.celdas[8]}\n")

    def actualizar_tablero(self, posicion, simbolo):
        if 0 <= posicion <= 8 and self.celdas[posicion] == " ":
            self.celdas[posicion] = simbolo
            return True
        return False

    def hay_ganador(self):
        for linea in self.lineas_ganadoras:
            a, b, c = linea
            if self.celdas[a] != " " and self.celdas[a] == self.celdas[b] == self.celdas[c]:
                return True
        return False

    def empate(self):
        return " " not in self.celdas and not self.hay_ganador()