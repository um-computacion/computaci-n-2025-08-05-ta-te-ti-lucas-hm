import unittest
from unittest.mock import patch, MagicMock

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from clases.juego import Jueguito

class TestJueguito(unittest.TestCase):
    def setUp(self):
        """Configuración inicial para cada test"""
        # Mockeamos las dependencias
        self.mock_tablero = MagicMock()
        self.mock_jugador_x = MagicMock()
        self.mock_jugador_o = MagicMock()
        
        # Configuramos los mocks
        self.mock_jugador_x.simbolo = "X"
        self.mock_jugador_x.nombre = "Jugador 1"
        self.mock_jugador_x.tipo = "humano"
        self.mock_jugador_o.simbolo = "O"
        self.mock_jugador_o.nombre = "IA"
        self.mock_jugador_o.tipo = "ia"
        
        # Parcheamos las clases originales (¡cambiamos 'juego' por 'clases.juego'!)
        self.patcher_tablero = patch('clases.juego.Tablero', return_value=self.mock_tablero)
        self.patcher_jugador = patch('clases.juego.Jugador')
        
        # Configuramos el side effect para devolver nuestros mocks
        self.mock_jugador = self.patcher_jugador.start()
        self.mock_jugador.side_effect = [self.mock_jugador_x, self.mock_jugador_o]
        
        self.mock_tablero_class = self.patcher_tablero.start()
        
        # Instanciamos el juego
        self.juego = Jueguito()
        
    def tearDown(self):
        """Limpieza después de cada test"""
        patch.stopall()
    
    def test_inicializacion(self):
        """Prueba que el juego se inicialice correctamente"""
        self.mock_tablero_class.assert_called_once()
        self.assertEqual(self.juego.jugador_actual, self.mock_jugador_x)
        # Verificamos que se crearon ambos jugadores
        self.assertEqual(self.mock_jugador.call_count, 2)
    
    # ... (mantén el resto de tus tests igual) ...

if __name__ == '__main__':
    unittest.main()