# ============================================================
#  cannon.py  –  Clases Canon y Bala
# ============================================================

import pygame
import math
from settings import *


class Bala:
    def __init__(self, x, y, angulo_grados):
        self.x = float(x)
        self.y = float(y)
        self.radio = RADIO_BALA
        self.activa = True

        rad = math.radians(angulo_grados)
        self.vx =  VELOCIDAD_BALA * math.cos(rad)
        self.vy = -VELOCIDAD_BALA * math.sin(rad)  # y crece hacia abajo

    def actualizar(self):
        self.x += self.vx
        self.y += self.vy
        # Desactivar si sale de pantalla
        if self.x < 0 or self.x > ANCHO or self.y < 0 or self.y > ALTO:
            self.activa = False

    def dibujar(self, pantalla):
        pos = (int(self.x), int(self.y))
        pygame.draw.circle(pantalla, AMARILLO, pos, self.radio)
        pygame.draw.circle(pantalla, NARANJA,  pos, self.radio, 2)


class Canon:
    def __init__(self):
        self.x = CANON_X
        self.y = CANON_Y
        self.angulo = 90   # 90° = apunta directo hacia arriba
        self.bala = None

    # ----- control -----

    def apuntar(self, mouse_x, mouse_y):
        dx = mouse_x - self.x
        dy = self.y - mouse_y          # invertido porque y crece hacia abajo
        angulo = math.degrees(math.atan2(dy, dx))
        self.angulo = max(15, min(165, angulo))  # limitar para no disparar hacia abajo

    def disparar(self):
        # Solo se puede disparar si no hay bala activa
        if self.bala is None or not self.bala.activa:
            rad = math.radians(self.angulo)
            tip_x = self.x + LARGO_CANON * math.cos(rad)
            tip_y = self.y - LARGO_CANON * math.sin(rad)
            self.bala = Bala(tip_x, tip_y, self.angulo)

    # ----- update / draw -----

    def actualizar(self):
        if self.bala and self.bala.activa:
            self.bala.actualizar()

    def dibujar(self, pantalla):
        # Base del cañón (rectángulo) - fondo negro, borde rojo
        base_rect = pygame.Rect(self.x - 30, self.y - 20, 60, 40)
        pygame.draw.rect(pantalla, NEGRO, base_rect)
        pygame.draw.rect(pantalla, ROJO, base_rect, 3)

        # Ruedas (cuadrados) - fondo negro, borde amarillo, más separados
        for ox in (-28, 28):
            wheel_rect = pygame.Rect(self.x + ox - 10, self.y + 8, 20, 20)
            pygame.draw.rect(pantalla, NEGRO,       wheel_rect)
            pygame.draw.rect(pantalla, AMARILLO, wheel_rect, 2)

        # Cañón (cuerpo) - borde negro con centro azul
        rad = math.radians(self.angulo)
        ex = int(self.x + LARGO_CANON * math.cos(rad))
        ey = int(self.y - LARGO_CANON * math.sin(rad))
        pygame.draw.line(pantalla, NEGRO, (self.x, self.y), (ex, ey), 14)
        pygame.draw.line(pantalla, AZUL, (self.x, self.y), (ex, ey), 8)

        # Bala
        if self.bala and self.bala.activa:
            self.bala.dibujar(pantalla)

    def obtener_bala(self):
        return self.bala
