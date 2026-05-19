# ============================================================
#  settings.py  –  Constantes globales del juego
# ============================================================

# Pantalla
ANCHO = 1280
ALTO  = 720
FPS   = 60
TITULO = "Aprende Jugando – Finanzas"

# Colores  (R, G, B) - Paleta desaturada
BLANCO      = (245, 245, 245)
NEGRO_PURO  = (0,   0,   0)
NEGRO       = (30,  30,  30)
GRIS        = (150, 150, 150)
AZUL        = (100, 145, 175)
AZUL_OSCURO = (40,  60,  90)
ROJO        = (165, 85,  85)
VERDE       = (90,  140, 90)
VERDE_OSCURO= (45,  100, 55)
AMARILLO    = (200, 180, 60)
NARANJA     = (180, 120, 70)
CELESTE     = (150, 175, 195)

# Jugabilidad
VIDAS          = 3
TIEMPO_PREGUNTA = 30   # segundos por pregunta

# Cañón
CANON_X     = ANCHO // 2
CANON_Y     = ALTO - 85          # sentado sobre el suelo
LARGO_CANON = 60
VELOCIDAD_BALA = 12
RADIO_BALA     = 11

# Bloques de respuesta
BLOQUE_ANCHO = 290               # más anchos para que el texto quepa
BLOQUE_ALTO  = 100
BLOQUE_Y     = 325               # bloques más arriba, cerca de la pregunta
POSICIONES_X = [330, 800, 1270]  # centrados en 1600px

# Posición vertical del mensaje de feedback (Correcto / Incorrecto / Tiempo)
# Zona despejada entre bloques (y≈350) y cañón (y≈600)
MENSAJE_Y    = 490
