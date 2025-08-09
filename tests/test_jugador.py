import unittest
from unittest.mock import patch
from clases.jugador import Jugador

class TestJugador(unittest.TestCase):
    def setUp(self):
        """Prepara un tablero simulado para las pruebas."""
        self.tablero_simulado = type('TableroSimulado', (), {'celdas': [" "] * 9})()

    # --- Tests de inicialización ---
    def test_jugador1_es_X(self):
        jugador = Jugador(numero_jugador=1)
        self.assertEqual(jugador.simbolo, "X")

    def test_jugador2_es_O(self):
        jugador = Jugador(numero_jugador=2)
        self.assertEqual(jugador.simbolo, "O")

    def test_numero_jugador_invalido(self):
        with self.assertRaises(ValueError):
            Jugador(numero_jugador=3)

    # --- Tests de movimientos humanos ---
    @patch('builtins.input', side_effect=['4'])  # Simula input "4"
    def test_movimiento_humano_valido(self, mock_input):
        jugador = Jugador(numero_jugador=1, tipo="humano")
        posicion = jugador.elegir_movimiento(self.tablero_simulado)
        self.assertEqual(posicion, 4)

    @patch('builtins.input', side_effect=['10', '2'])  # Primero inválido, luego válido
    def test_movimiento_humano_invalido_luego_valido(self, mock_input):
        jugador = Jugador(numero_jugador=1, tipo="humano")
        posicion = jugador.elegir_movimiento(self.tablero_simulado)
        self.assertEqual(posicion, 2)

    # --- Tests de IA ---
    def test_movimiento_IA_valido(self):
        jugador = Jugador(numero_jugador=2, tipo="ia")
        self.tablero_simulado.celdas = ["X", " ", " ", " ", " ", " ", " ", " ", " "]
        posicion = jugador.elegir_movimiento(self.tablero_simulado)
        self.assertIn(posicion, [1, 2, 3, 4, 5, 6, 7, 8])  # Debe elegir una casilla vacía

    def test_movimiento_IA_con_tablero_lleno(self):
        jugador = Jugador(numero_jugador=2, tipo="ia")
        self.tablero_simulado.celdas = ["X"] * 9  # Todas ocupadas
        with self.assertRaises(IndexError):  # random.choice([]) lanza IndexError
            jugador.elegir_movimiento(self.tablero_simulado)

if __name__ == '__main__':
    unittest.main()