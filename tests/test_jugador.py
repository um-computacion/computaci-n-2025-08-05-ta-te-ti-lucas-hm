import unittest
from unittest.mock import patch, MagicMock
from clases.jugador import Jugador
from clases.tablero import Tablero

class TestJugador(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.tablero = Tablero()
        self.jugador_x = Jugador(1, tipo="humano", nombre="Jugador 1")
        self.jugador_o = Jugador(2, tipo="ia", nombre="IA")
    
    def test_jugador_creacion_correcta(self):
        """Test que verifica que se crea un jugador correctamente"""
        jugador = Jugador(1, tipo="humano", nombre="Test")
        self.assertEqual(jugador.simbolo, "X")
        self.assertEqual(jugador.tipo, "humano")
        self.assertEqual(jugador.nombre, "Test")
    
    def test_jugador_o_tiene_simbolo_o(self):
        """Test que verifica que el jugador 2 tiene símbolo O"""
        jugador = Jugador(2, tipo="humano", nombre="Test")
        self.assertEqual(jugador.simbolo, "O")
    
    def test_ia_elige_movimiento_valido(self):
        """Test que verifica que la IA elige un movimiento válido"""
        # Crear un tablero con algunas posiciones ocupadas
        self.tablero.celdas = ["X", " ", "O", " ", "X", " ", " ", " ", " "]
        
        # La IA debería elegir una posición vacía
        posicion = self.jugador_o.elegir_movimiento(self.tablero)
        
        # Verificar que la posición elegida está vacía
        self.assertIn(posicion, [1, 3, 5, 6, 7, 8])
        self.assertEqual(self.tablero.celdas[posicion], " ")
    
    @patch('builtins.input', return_value='4')
    def test_jugador_humano_llena_posicion_valida(self, mock_input):
        """Test que verifica que un jugador humano llena una posición válida"""
        # Verificar que la posición 4 está vacía inicialmente
        self.assertEqual(self.tablero.celdas[4], " ")
        
        # El jugador elige la posición 4
        posicion = self.jugador_x.elegir_movimiento(self.tablero)
        
        # Verificar que se eligió la posición correcta
        self.assertEqual(posicion, 4)
        
        # Verificar que la posición sigue vacía (el tablero no se actualiza en elegir_movimiento)
        self.assertEqual(self.tablero.celdas[4], " ")
    
    def test_actualizar_tablero_con_movimiento_jugador(self):
        """Test que verifica que se actualiza el tablero cuando un jugador hace un movimiento"""
        # Verificar que la posición 0 está vacía
        self.assertEqual(self.tablero.celdas[0], " ")
        
        # Actualizar el tablero con el movimiento del jugador
        resultado = self.tablero.actualizar_tablero(0, self.jugador_x.simbolo)
        
        # Verificar que la actualización fue exitosa
        self.assertTrue(resultado)
        
        # Verificar que la posición ahora tiene el símbolo del jugador
        self.assertEqual(self.tablero.celdas[0], "X")
    
    def test_no_se_puede_ocupar_posicion_ya_ocupada(self):
        """Test que verifica que no se puede ocupar una posición ya ocupada"""
        # Ocupar la posición 0
        self.tablero.actualizar_tablero(0, "X")
        self.assertEqual(self.tablero.celdas[0], "X")
        
        # Intentar ocupar la misma posición con otro símbolo
        resultado = self.tablero.actualizar_tablero(0, "O")
        
        # Verificar que la actualización falló
        self.assertFalse(resultado)
        
        # Verificar que la posición sigue con el símbolo original
        self.assertEqual(self.tablero.celdas[0], "X")
    
    def test_ia_llena_posicion_aleatoria(self):
        """Test que verifica que la IA llena una posición aleatoria vacía"""
        # Crear un tablero con solo algunas posiciones vacías
        self.tablero.celdas = ["X", "O", "X", "O", "X", "O", " ", " ", " "]
        
        # La IA elige una posición
        posicion = self.jugador_o.elegir_movimiento(self.tablero)
        
        # Verificar que la posición elegida está entre las vacías
        self.assertIn(posicion, [6, 7, 8])
        
        # Verificar que la posición elegida está vacía
        self.assertEqual(self.tablero.celdas[posicion], " ")
    
    def test_jugador_humano_no_puede_elegir_posicion_invalida(self):
        """Test que verifica que el jugador humano no puede elegir posiciones inválidas"""
        # Ocupar algunas posiciones
        self.tablero.actualizar_tablero(0, "X")
        self.tablero.actualizar_tablero(1, "O")
        
        # Verificar que las posiciones ocupadas no se pueden actualizar
        self.assertFalse(self.tablero.actualizar_tablero(0, "X"))
        self.assertFalse(self.tablero.actualizar_tablero(1, "O"))
        
        # Verificar que las posiciones siguen con sus valores originales
        self.assertEqual(self.tablero.celdas[0], "X")
        self.assertEqual(self.tablero.celdas[1], "O")

if __name__ == '__main__':
    unittest.main()