from tablero import Tablero
from jugador import Jugador

class Jueguito:
    def __init__(self):
        self.tablero = Tablero()
        self.jugador_x = Jugador(1, tipo="humano", nombre="Jugador 1")
        self.jugador_o = Jugador(2, tipo="ia", nombre="IA")
        self.jugador_actual = self.jugador_x

    def cambiar_turno(self):
        self.jugador_actual = self.jugador_o if self.jugador_actual == self.jugador_x else self.jugador_x

    def iniciar(self):
        print("\n¡Bienvenido al Ta-Te-Ti!")
        print("Posiciones del tablero:")
        print("0|1|2\n-----\n3|4|5\n-----\n6|7|8\n")

        while True:
            self.tablero.mostrar_tablero()
            posicion = self.jugador_actual.elegir_movimiento(self.tablero)
            
            if self.tablero.actualizar_tablero(posicion, self.jugador_actual.simbolo):
                if self.tablero.hay_ganador():
                    self.tablero.mostrar_tablero()
                    print(f"¡{self.jugador_actual.nombre} gana!")
                    break
                elif self.tablero.empate():
                    self.tablero.mostrar_tablero()
                    print("¡Empate!")
                    break
                self.cambiar_turno()
            else:
                print("Movimiento inválido. Intenta de nuevo.")