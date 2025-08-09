from tablero import Tablero
from juego import jueguito  # Necesitarás importar la clase Juego

class CLI:
    def __init__(self):
        self.juego = jueguito()  # Creamos una instancia del juego
    
    def iniciar_juego(self):
        print("¡Bienvenido al Ta-Te-Ti!")
        while True:
            # Mostrar el tablero actual
            self.juego.tablero_mostrar()
            
            # Obtener movimiento del jugador actual
            try:
                posicion = int(input(f"Jugador {self.juego.jugador_actual.simbolo}, elige posición (0-8): "))
                
                # Intentar hacer el movimiento
                if self.juego.hacer_movimiento(posicion):
                    # Verificar si el juego terminó
                    if self.juego.tablero.hay_ganador():
                        self.juego.tablero.mostrar()
                        print(f"¡Jugador {self.juego.jugador_actual.simbolo} gana!")
                        break
                    elif self.juego.tablero.empate():
                        self.juego.tablero.mostrar()
                        print("¡Empate!")
                        break
                else:
                    print("Movimiento inválido. Intenta de nuevo.")
            except ValueError:
                print("Por favor ingresa un número entre 0 y 8.")

if __name__ == "__main__":
    cli = CLI()
    cli.iniciar_juego()