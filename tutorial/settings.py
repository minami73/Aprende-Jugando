# ============================================================
#  settings.py  –  Constantes del juego ( ¡NO TOCAR! )
#  Este archivo está completo, aquí se configuran las opciones
# ============================================================

# ---------- PANTALLA ----------
ANCHO = 1600
ALTO  = 900
FPS   = 60
TITULO = "Aprende Jugando – Finanzas"

# ---------- COLORES (R, G, B) ----------
BLANCO      = (245, 245, 245)
NEGRO       = (30,   30,   30)
GRIS        = (150, 150, 150)
AZUL        = (100, 145, 175)
AZUL_OSCURO = (40,  60,  90)
ROJO        = (165, 85,  85)
VERDE       = (90,  140, 90)
VERDE_OSCURO= (60,  100, 60)
AMARILLO    = (200, 180, 60)
NARANJA     = (180, 120, 70)
CELESTE     = (150, 175, 195)

# ---------- JUGABILIDAD ----------
VIDAS          = 3
TIEMPO_PREGUNTA = 30   # segundos por pregunta

# ---------- CAÑÓN ----------
CANON_X     = ANCHO // 2
CANON_Y     = ALTO - 85
LARGO_CANON = 60
VELOCIDAD_BALA = 12
RADIO_BALA     = 11

# ---------- BLOQUES DE RESPUESTA ----------
BLOQUE_ANCHO = 290
BLOQUE_ALTO  = 100
BLOQUE_Y     = 325
POSICIONES_X = [330, 800, 1270]

# ---------- MENSAJE FEEDBACK ----------
MENSAJE_Y    = 490


# ============================================================
#  💡 TAREA: Cambia los colores arriba para personalizar el juego!
#  Pista: Busca los colores y cambia los números (R, G, B)
# ============================================================