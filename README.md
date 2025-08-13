# Ta-Te-Ti (Tres en Línea)

## Descripción

Este es un juego clásico de Ta-Te-Ti (Tres en Línea) implementado en Python. El juego permite enfrentar a un jugador humano contra una inteligencia artificial simple.

## Características

- **Modo de juego**: Humano vs IA
- **Interfaz**: Línea de comandos (CLI)
- **Tablero**: 3x3 con posiciones numeradas del 0 al 8
- **Símbolos**: X para el jugador humano, O para la IA
- **IA**: Juega movimientos aleatorios en posiciones disponibles

## Estructura del Proyecto

```
computaci-n-2025-08-05-ta-te-ti-lucas-hm/
├── clases/
│   ├── __init__.py
│   ├── cli.py          # Punto de entrada principal
│   ├── juego.py        # Lógica principal del juego
│   ├── jugador.py      # Clase Jugador (humano e IA)
│   └── tablero.py      # Clase Tablero y lógica del juego
├── tests/              # Pruebas unitarias
│   ├── __init__.py
│   ├── test_juego.py
│   ├── test_jugador.py
│   └── test_tablero.py
└── README.md
```

## Cómo Ejecutar el Juego

### Requisitos
- Python 3.x instalado en tu sistema

### Instrucciones de Ejecución

1. **Navega al directorio del proyecto:**
   ```bash
   cd computaci-n-2025-08-05-ta-te-ti-lucas-hm
   ```

2. **Ejecuta el juego:**
   ```bash
   python clases/cli.py
   ```

### Cómo Jugar

1. **Posiciones del tablero:**
   ```
   0|1|2
   -----
   3|4|5
   -----
   6|7|8
   ```

2. **Turnos:**
   - El jugador humano (X) siempre comienza
   - La IA (O) responde automáticamente
   - Los turnos se alternan hasta que haya un ganador o empate

3. **Objetivo:**
   - Formar una línea horizontal, vertical o diagonal con tu símbolo
   - El primer jugador en lograrlo gana

4. **Movimientos:**
   - Ingresa un número del 0 al 8 para colocar tu símbolo
   - Solo puedes jugar en posiciones vacías
   - El juego valida automáticamente los movimientos

## Ejecutar Pruebas

Para ejecutar las pruebas unitarias:

```bash
python -m pytest tests/
```

## Clases Principales

- **`Jueguito`**: Clase principal que maneja el flujo del juego
- **`Tablero`**: Gestiona el estado del tablero y verifica victorias/empates
- **`Jugador`**: Representa tanto jugadores humanos como IA
- **`cli.py`**: Punto de entrada para ejecutar el juego

## Autor

Desarrollado como proyecto de programación en Python.
