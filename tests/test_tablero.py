import sys
import os
from pathlib import Path

# Añade el directorio raíz al path de Python
sys.path.append(str(Path(__file__).parent.parent))

from clases.tablero import Tablero
import unittest

class TestTablero(unittest.TestCase):
    def setUp(self):
        """Prepara el tablero para cada test"""
        self.tablero = Tablero()

    def test_actualizar_tablero_valido(self):
        """Prueba movimientos válidos"""
        self.assertTrue(self.tablero.actualizar_tablero(0, "X"))
        self.assertEqual(self.tablero.celdas[0], "X")
        
    def test_actualizar_tablero_invalido(self):
        """Prueba movimientos inválidos"""
        self.tablero.actualizar_tablero(0, "X")
        # Posición ocupada
        self.assertFalse(self.tablero.actualizar_tablero(0, "O"))
        # Posición fuera de rango
        self.assertFalse(self.tablero.actualizar_tablero(9, "X"))

    def test_hay_ganador(self):
        """Prueba detección de ganador"""
        # Horizontal
        self.tablero.actualizar_tablero(0, "X")
        self.tablero.actualizar_tablero(1, "X")
        self.tablero.actualizar_tablero(2, "X")
        self.assertTrue(self.tablero.hay_ganador())

    def test_empate(self):
        """Prueba detección de empate"""
        # Llena el tablero sin ganador
        for i in [0, 1, 2, 3, 4, 6, 7, 8]:
            self.tablero.actualizar_tablero(i, "X" if i % 2 == 0 else "O")
        self.assertFalse(self.tablero.hay_ganador())
        self.assertTrue(self.tablero.empate())

if __name__ == '__main__':
    unittest.main()