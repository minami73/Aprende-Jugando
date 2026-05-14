# ============================================================
#  ui.py  –  HUD (vidas, timer, pregunta, instrucciones)
#
#  Layout en 1280x720:
#  ┌──────────────────────────────────────────────────────────┐
#  │ ●●●  (vidas, izq)   Pregunta X/Y (centro)   30 (timer)  │  y 0-40
#  │ ──────────────────────────────────────────────────────── │
#  │           [ caja de la pregunta, h=88 ]                  │  y 44-132
#  └──────────────────────────────────────────────────────────┘
# ============================================================

import pygame
from settings import *

# Alto reservado para toda la zona del HUD (usada en game.py para cálculos)
HUD_ALTO = 140


class HUD:
    def __init__(self, fuente, fuente_timer, fuente_pequena):
        """
        fuente       → tamaño normal  (preguntas, etiquetas)
        fuente_timer → tamaño grande  (número del timer)
        fuente_pequena → tamaño chico (instrucciones, "TIEMPO")
        """
        self.fuente    = fuente
        self.f_timer   = fuente_timer
        self.f_pequena = fuente_pequena

    # ---------------------------------------------------------------- vidas

    def dibujar_vidas(self, pantalla, vidas):
        radio = 13
        for i in range(vidas):
            cx = 30 + i * 34
            pygame.draw.circle(pantalla, ROJO,   (cx, 30), radio)
            pygame.draw.circle(pantalla, NEGRO_PURO, (cx, 30), radio, 3)

    # --------------------------------------------------------------- timer

    def dibujar_timer(self, pantalla, segundos):
        color = VERDE if segundos > 10 else ROJO
        num   = self.f_timer.render(str(max(0, segundos)), True, color)
        label = self.f_pequena.render("TIEMPO", True, BLANCO)
        pantalla.blit(num,   num.get_rect(topright=(ANCHO - 14, 10)))
        pantalla.blit(label, label.get_rect(topright=(ANCHO - 14, 50)))

    # ------------------------------------------------------------- pregunta

    def dibujar_pregunta(self, pantalla, texto, numero, total):
        # --- "Pregunta X / Y" centrado en la primera fila ---
        etiq = self.fuente.render(f"Pregunta  {numero} / {total}", True, AMARILLO)
        pantalla.blit(etiq, etiq.get_rect(centerx=ANCHO // 2, y=15))

# --- caja de la pregunta ---
        BOX_X = 80
        BOX_Y = 112
        BOX_W = ANCHO - 160
        BOX_H = 88
        box = pygame.Rect(BOX_X, BOX_Y, BOX_W, BOX_H)
        pygame.draw.rect(pantalla, AZUL_OSCURO, box, border_radius=10)
        pygame.draw.rect(pantalla, NEGRO_PURO,       box, 3,  border_radius=10)

        # ajuste de texto al ancho de la caja
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

    # --------------------------------------------------------- instrucciones

    def dibujar_instrucciones(self, pantalla):
        txt = self.f_pequena.render(
            "Mueve el raton para apuntar  |  Clic para disparar", True, GRIS
        )
        pantalla.blit(txt, txt.get_rect(centerx=ANCHO // 2, bottom=ALTO - 6))
