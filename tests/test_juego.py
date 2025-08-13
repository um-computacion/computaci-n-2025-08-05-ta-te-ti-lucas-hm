import unittest
from unittest.mock import patch, MagicMock
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
        self.mock_jugador_o.simbolo = "O"
        self.mock_jugador_o.nombre = "IA"
        
        # Parcheamos las clases originales
        self.patcher_tablero = patch('juego.Tablero', return_value=self.mock_tablero)
        self.patcher_jugador = patch('juego.Jugador')
        self.patcher_jugador.start().side_effect = [self.mock_jugador_x, self.mock_jugador_o]
        
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
    
    def test_cambiar_turno(self):
        """Prueba el cambio de turno entre jugadores"""
        # Turno inicial es X
        self.assertEqual(self.juego.jugador_actual, self.mock_jugador_x)
        
        # Cambiamos turno
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.jugador_actual, self.mock_jugador_o)
        
        # Cambiamos de nuevo
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.jugador_actual, self.mock_jugador_x)
    
    @patch('builtins.print')
    def test_iniciar_muestra_bienvenida(self, mock_print):
        """Prueba que se muestre el mensaje de bienvenida"""
        self.mock_tablero.hay_ganador.return_value = True  # Para terminar inmediatamente
        self.juego.iniciar()
        mock_print.assert_any_call("\n¡Bienvenido al Ta-Te-Ti!")
    
    def test_jugador_humano_elige_movimiento(self):
        """Prueba que se llame a elegir_movimiento del jugador actual"""
        self.mock_tablero.hay_ganador.return_value = True  # Para terminar después de 1 movimiento
        self.mock_jugador_x.elegir_movimiento.return_value = 0
        
        self.juego.iniciar()
        self.mock_jugador_x.elegir_movimiento.assert_called_once_with(self.mock_tablero)
    
    def test_movimiento_valido_actualiza_tablero(self):
        """Prueba que un movimiento válido actualiza el tablero"""
        self.mock_tablero.hay_ganador.return_value = True  # Para terminar después de 1 movimiento
        self.mock_jugador_x.elegir_movimiento.return_value = 0
        self.mock_tablero.actualizar_tablero.return_value = True
        
        self.juego.iniciar()
        self.mock_tablero.actualizar_tablero.assert_called_once_with(0, "X")
    
    def test_movimiento_invalido_muestra_error(self):
        """Prueba que un movimiento inválido muestra mensaje de error"""
        self.mock_tablero.hay_ganador.side_effect = [False, True]  # Terminar después de 2 intentos
        self.mock_jugador_x.elegir_movimiento.side_effect = [0, 1]
        self.mock_tablero.actualizar_tablero.side_effect = [False, True]
        
        with patch('builtins.print') as mock_print:
            self.juego.iniciar()
            mock_print.assert_any_call("Movimiento inválido. Intenta de nuevo.")
    
    def test_juego_detecta_ganador(self):
        """Prueba que el juego detecta cuando hay un ganador"""
        self.mock_tablero.hay_ganador.return_value = True
        self.mock_jugador_x.elegir_movimiento.return_value = 0
        self.mock_tablero.actualizar_tablero.return_value = True
        
        with patch('builtins.print') as mock_print:
            self.juego.iniciar()
            mock_print.assert_any_call(f"¡{self.mock_jugador_x.nombre} gana!")
    
    def test_juego_detecta_empate(self):
        """Prueba que el juego detecta empate"""
        self.mock_tablero.hay_ganador.return_value = False
        self.mock_tablero.empate.return_value = True
        self.mock_jugador_x.elegir_movimiento.return_value = 0
        self.mock_tablero.actualizar_tablero.return_value = True
        
        with patch('builtins.print') as mock_print:
            self.juego.iniciar()
            mock_print.assert_any_call("¡Empate!")

if __name__ == '__main__':
    unittest.main()