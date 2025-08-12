from tablero import Tablero
from jugador import Jugador

class Jueguito:  # Cambiado a mayúscula por convención
    def __init__(self):
        self.tablero = Tablero()
        self.jugador_actual = "X"  # Inicializado correctamente
        self.ganador = None
        self.juego_terminado = False
        # Inicializar jugadores
        self.jugador_x = Jugador(numero_jugador=1, tipo="humano")
        self.jugador_o = Jugador(numero_jugador=2, tipo="ia")  # o "humano" para 2 jugadores

    def cambiar_turno(self):
        """Alterna entre los jugadores X y O."""
        self.jugador_actual = self.jugador_o if self.jugador_actual == self.jugador_x else self.jugador_x

    def hacer_movimiento(self, posicion):
        """
        Intenta realizar un movimiento y actualiza el estado del juego.
        
        Args:
            posicion (int): Posición en el tablero (0-8)
            
        Returns:
            bool: True si el movimiento fue válido
        """
        if not self.juego_terminado and self.tablero.actualizar_tablero(posicion, self.jugador_actual.simbolo):
            if self.verificar_ganador():
                self.ganador = self.jugador_actual
                self.juego_terminado = True
            elif self.verificar_empate():
                self.juego_terminado = True
            else:
                self.cambiar_turno()
            return True
        return False

    def verificar_ganador(self):
        """Verifica si el jugador actual ha ganado."""
        return self.tablero.hay_ganador()

    def verificar_empate(self):
        """Verifica si el juego ha terminado en empate."""
        return self.tablero.empate()

    def iniciar(self):
        """Método principal para iniciar el juego."""
        while not self.juego_terminado:
            self.tablero.mostrar_tablero()
            
            # Obtener movimiento del jugador actual
            if self.jugador_actual.tipo == "humano":
                posicion = self.jugador_actual.elegir_movimiento(self.tablero)
            else:
                print(f"Turno de la IA ({self.jugador_actual.simbolo})...")
                posicion = self.jugador_actual.elegir_movimiento(self.tablero)
            
            # Procesar movimiento
            if not self.hacer_movimiento(posicion):
                print("Movimiento inválido. Intenta de nuevo.")

        # Mostrar resultado final
        self.tablero.mostrar_tablero()
        if self.ganador:
            print(f"¡Jugador {self.ganador.simbolo} gana!")
        else:
            print("¡Empate!")