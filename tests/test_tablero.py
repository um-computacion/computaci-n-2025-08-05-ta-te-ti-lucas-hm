import unittest
from clases.tablero import Tablero

class TestTablero(unittest.TestCase):
    def test_tablero(self):
        tablas = Tablero()
        tablas.hay_ganador(tablas.actualizar_tablero(0, "X"))
        tablas.hay_ganador(tablas.actualizar_tablero(1, "X"))
        tablas.hay_ganador(tablas.actualizar_tablero(2, "X"))
        tablas.hay_ganador(tablas.actualizar_tablero(3, "X"))
        tablas.hay_ganador(tablas.actualizar_tablero(4, "X"))
        tablas.hay_ganador(tablas.actualizar_tablero(5, "X"))
        tablas.hay_ganador(tablas.actualizar_tablero(6, "X"))
        tablas.hay_ganador(tablas.actualizar_tablero(7, "X"))
        tablas.hay_ganador(tablas.actualizar_tablero(8, "X"))
        tablas.empate(tablas.actualizar_tablero(0, "X"))
        tablas.empate(tablas.actualizar_tablero(1, "X"))
        tablas.empate(tablas.actualizar_tablero(2, "o"))
        tablas.empate(tablas.actualizar_tablero(3, "X"))
        tablas.empate(tablas.actualizar_tablero(4, "o"))
        tablas.empate(tablas.actualizar_tablero(5, "X"))
        tablas.empate(tablas.actualizar_tablero(6, "o"))
        tablas.empate(tablas.actualizar_tablero(7, "X"))
        tablas.empate(tablas.actualizar_tablero(8, "o"))

if __name__ == '__main__':
    unittest.main()