from tablero import Tablero
from jugador import Jugador
from juego import jueguito

# Opcional: Exporta las clases para que puedan usarse con `from tateti import ...`
__all__ = ['Tablero', 'Jugador', 'Juego']

# Opcional: Añade una función de conveniencia para iniciar el juego rápidamente
def iniciar_juego(modo="humano_vs_ia"):
    """
    Inicia una partida de Ta-Te-Ti.
    Modos disponibles:
    - "humano_vs_ia" (default): 1 jugador humano vs IA.
    - "humano_vs_humano": 2 jugadores humanos.
    """
    juego = jueguito()
    
    if modo == "humano_vs_humano":
        juego.jugador_actual.tipo = "humano"  # Cambia el Jugador O a humano
    
    juego.iniciar()