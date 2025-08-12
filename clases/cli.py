from tablero import Tablero
from juego import Jueguito

class CLI:
    def __init__(self):
        self.juego = Jueguito()
        self.tablero = Tablero()
    
    def iniciar_juego(self):
        print("¡Bienvenido al Ta-Te-Ti!")
        while True:
            # Mostrar el tablero actual
            Tablero.actualizar_tablero()
            
            # Obtener movimiento del jugador actual
            try:
                posicion = int(input(f"Jugador {self.juego.jugador_actual.simbolo}, elige posición (0-8): "))
                
                # Intentar hacer el movimiento
                if self.juego.hacer_movimiento(posicion):
                    # Verificar si el juego terminó
                    if self.tablero.hay_ganador():
                        self.tablero.mostrar_tablero()
                        print(f"¡Jugador {self.juego.jugador_actual.simbolo} gana!")
                        break
                    elif self.tablero.empate():
                        self.tablero.mostrar_tablero()
                        print("¡Empate!")
                        break
                else:
                    print("Movimiento inválido. Intenta de nuevo.")
            except ValueError:
                print("Por favor ingresa un número entre 0 y 8.")

if __name__ == "__main__":
    cli = CLI()
    cli.iniciar_juego()