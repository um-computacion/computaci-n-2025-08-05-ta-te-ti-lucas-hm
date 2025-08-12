from clases.juego import jueguito
from clases.tablero import Tablero
from clases.jugador import Jugador
from clases.juego import jueguito  # Cambié "jueguito" a "Juego" para seguir convenciones

# Exporta las clases/funciones principales para importación directa
__all__ = ['Tablero', 'Jugador', 'Juego', 'iniciar_juego']

def iniciar_juego(modo="humano_vs_ia"):
    """
    Inicia una partida de Ta-Te-Ti.
    
    Args:
        modo (str): Tipo de partida. Opciones:
            - "humano_vs_ia" (default): 1 humano vs IA
            - "humano_vs_humano": 2 jugadores humanos
    """
    juego = jueguito()  # Instancia del juego
    
    if modo == "humano_vs_humano":
        # Cambia ambos jugadores a humanos
        juego.jugador_actual.tipo = "humano"
        juego.jugador_actual.tipo = "humano"
    elif modo == "humano_vs_ia":
        # Asegura que el jugador O sea IA
        juego.jugador_actual.tipo = "ia"
    else:
        raise ValueError(f"Modo '{modo}' no reconocido. Usar 'humano_vs_ia' o 'humano_vs_humano'")
    
    juego.iniciar()  # Comienza la partida


# Ejemplo de cómo se usaría desde otro archivo:
if __name__ == "__main__":
    print("¡Bienvenido al Ta-Te-Ti!")
    iniciar_juego(modo="humano_vs_humano")  # Cambiar modo si se desea