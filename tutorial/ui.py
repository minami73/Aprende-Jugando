# ============================================================
#  ui.py  –  HUD ( Heads-Up Display )
#  Muestra las vidas, el timer, la pregunta y las instrucciones
#  Este archivo está casi completo, puedes personalizar colores/posiciones
# ============================================================

import pygame
from settings import *

HUD_ALTO = 140


class HUD:
    def __init__(self, fuente, fuente_timer, fuente_pequena):
        self.fuente    = fuente
        self.f_timer   = fuente_timer
        self.f_pequena = fuente_pequena

    # ---------- VIDAS ----------
    def dibujar_vidas(self, pantalla, vidas):
        radio = 13
        for i in range(vidas):
            cx = 30 + i * 34
            # PISTA: Círculos rojos con borde negro (grosor 3)
            pygame.draw.circle(pantalla, ROJO, (cx, 30), radio)
            pygame.draw.circle(pantalla, NEGRO, (cx, 30), radio, 3)

    # ---------- TIMER ----------
    def dibujar_timer(self, pantalla, segundos):
        # PISTA: Verde si > 10 segundos, rojo si <= 10
        color = VERDE if segundos > 10 else ROJO
        num   = self.f_timer.render(str(max(0, segundos)), True, color)
        label = self.f_pequena.render("TIEMPO", True, BLANCO)
        pantalla.blit(num,   num.get_rect(topright=(ANCHO - 14, 10)))
        pantalla.blit(label, label.get_rect(topright=(ANCHO - 14, 50)))

    # ---------- PREGUNTA ----------
    def dibujar_pregunta(self, pantalla, texto, numero, total):
        # "Pregunta X / Y"
        etiq = self.fuente.render(f"Pregunta  {numero} / {total}", True, AMARILLO)
        pantalla.blit(etiq, etiq.get_rect(centerx=ANCHO // 2, y=15))

        # Caja de la pregunta
        BOX_X = 80
        BOX_Y = 112
        BOX_W = ANCHO - 160
        BOX_H = 88

        box = pygame.Rect(BOX_X, BOX_Y, BOX_W, BOX_H)
        # PISTA: Fondo azul oscuro con borde negro de 3px
        pygame.draw.rect(pantalla, AZUL_OSCURO, box, border_radius=10)
        pygame.draw.rect(pantalla, NEGRO,       box, 3,  border_radius=10)

        # Ajuste de texto
        margen = 24
        max_w  = BOX_W - margen * 2
        palabras = texto.split()
        lineas, linea = [], ""
        for p in palabras:
            prueba = (linea + " " + p).strip()
            if self.fuente.size(prueba)[0] <= max_w:
                linea = prueba
            else:
                if linea:
                    lineas.append(linea)
                linea = p
        if linea:
            lineas.append(linea)

        alto_texto = len(lineas) * self.fuente.get_height()
        sy = BOX_Y + (BOX_H - alto_texto) // 2
        for l in lineas:
            s = self.fuente.render(l, True, BLANCO)
            pantalla.blit(s, s.get_rect(centerx=ANCHO // 2, y=sy))
            sy += self.fuente.get_height()

    # ---------- INSTRUCCIONES ----------
    def dibujar_instrucciones(self, pantalla):
        txt = self.f_pequena.render(
            "Mueve el raton para apuntar  |  Clic para disparar", True, GRIS
        )
        pantalla.blit(txt, txt.get_rect(centerx=ANCHO // 2, bottom=ALTO - 6))


# ============================================================
#  💡 TAREA: Prueba cambiar las posiciones (números en y=, etc.)
#  Pista: Cambia valores como y=15, y=30, BOX_Y=112, etc.
#         y observa cómo se mueve cada elemento en la pantalla
# ============================================================