import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clases.jugador import Jugador
import unittest

class TestJugador(unittest.TestCase):
    def test_jugador_creation(self):
        jugador = Jugador(1, tipo="humano", nombre="Test")
        self.assertEqual(jugador.simbolo, "X")

if __name__ == '__main__':
    unittest.main()