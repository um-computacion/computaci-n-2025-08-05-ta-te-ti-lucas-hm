import unittest
from unittest.mock import patch, MagicMock
from clases.juego import Jueguito
from clases.tablero import Tablero
from clases.jugador import Jugador

class TestJuego(unittest.TestCase):
    def setUp(self):
        """Prepara un juego simulado para las pruebas."""
        self.juego = Jueguito()
        # Mock del tablero para controlar su comportamiento
        self.juego.tablero = MagicMock(spec=Tablero)
        # Mocks de jugadores
        self.juego.jugador_x = MagicMock(spec=Jugador)
        self.juego.jugador_o = MagicMock(spec=Jugador)
        self.juego.jugador_x.simbolo = "X"
        self.juego.jugador_o.simbolo = "O"

    # --- Tests de inicialización ---
    def test_inicializacion_correcta(self):
        self.assertEqual(self.juego.jugador_actual.simbolo, "X")
        self.assertIsNone(self.juego.ganador)
        self.assertFalse(self.juego.juego_terminado)

    # --- Tests de cambiar_turno ---
    def test_cambiar_turno_de_X_a_O(self):
        self.juego.jugador_actual = self.juego.jugador_x
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.jugador_actual.simbolo, "O")

    def test_cambiar_turno_de_O_a_X(self):
        self.juego.jugador_actual = self.juego.jugador_o
        self.juego.cambiar_turno()
        self.assertEqual(self.juego.jugador_actual.simbolo, "X")

    # --- Tests de hacer_movimiento ---
    @patch.object(Tablero, 'actualizar', return_value=True)
    def test_movimiento_valido_cambia_turno(self, mock_actualizar):
        self.juego.verificar_ganador = MagicMock(return_value=False)
        self.juego.verificar_empate = MagicMock(return_value=False)
        
        result = self.juego.hacer_movimiento(4)
        self.assertTrue(result)
        mock_actualizar.assert_called_once_with(4, "X")
        self.assertEqual(self.juego.jugador_actual.simbolo, "O")

    @patch.object(Tablero, 'actualizar', return_value=False)
    def test_movimiento_invalido_no_cambia_turno(self, mock_actualizar):
        result = self.juego.hacer_movimiento(4)
        self.assertFalse(result)
        mock_actualizar.assert_called_once_with(4, "X")
        self.assertEqual(self.juego.jugador_actual.simbolo, "X")

    # --- Tests de verificar_ganador ---
    def test_verificar_ganador_true(self):
        self.juego.tablero.hay_ganador.return_value = True
        self.assertTrue(self.juego.verificar_ganador())
        self.juego.tablero.hay_ganador.assert_called_once()

    def test_verificar_ganador_false(self):
        self.juego.tablero.hay_ganador.return_value = False
        self.assertFalse(self.juego.verificar_ganador())

    # --- Tests de verificar_empate ---
    def test_verificar_empate_true(self):
        self.juego.tablero.empate.return_value = True
        self.assertTrue(self.juego.verificar_empate())
        self.juego.tablero.empate.assert_called_once()

    def test_verificar_empate_false(self):
        self.juego.tablero.empate.return_value = False
        self.assertFalse(self.juego.verificar_empate())

    # --- Tests de flujo completo ---
    @patch.object(Jugador, 'elegir_movimiento', return_value=4)
    @patch.object(Tablero, 'mostrar')
    def test_iniciar_juego_humano_vs_humano(self, mock_mostrar, mock_elegir):
        self.juego.jugador_x.tipo = "humano"
        self.juego.jugador_o.tipo = "humano"
        self.juego.tablero.hay_ganador.side_effect = [False, True]  # Segundo movimiento gana
        self.juego.tablero.empate.return_value = False
        
        with patch('builtins.print') as mock_print:
            self.juego.iniciar()
            
            # Verifica que se mostró el tablero y hubo interacción
            self.assertGreaterEqual(mock_mostrar.call_count, 1)
            mock_elegir.assert_called()
            mock_print.assert_any_call("¡Jugador X gana!")

    @patch.object(Jugador, 'elegir_movimiento', return_value=4)
    def test_juego_termina_en_empate(self, mock_elegir):
        self.juego.tablero.hay_ganador.return_value = False
        self.juego.tablero.empate.return_value = True
        
        with patch('builtins.print') as mock_print:
            self.juego.iniciar()
            mock_print.assert_called_with("¡Empate!")

if __name__ == '__main__':
    unittest.main()