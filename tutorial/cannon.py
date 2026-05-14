# ============================================================
#  cannon.py  –  Clases del cañón y la bala
#  La lógica está lista, ¡completa el dibujo!
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
        self.vx = VELOCIDAD_BALA * math.cos(rad)
        self.vy = -VELOCIDAD_BALA * math.sin(rad)

    def actualizar(self):
        self.x += self.vx
        self.y += self.vy
        if self.x < 0 or self.x > ANCHO or self.y < 0 or self.y > ALTO:
            self.activa = False

    def dibujar(self, pantalla):
        pos = (int(self.x), int(self.y))
        pygame.draw.circle(pantalla, AMARILLO, pos, self.radio)
        pygame.draw.circle(pantalla, NARANJA, pos, self.radio, 2)


class Canon:
    def __init__(self):
        self.x = CANON_X
        self.y = CANON_Y
        self.angulo = 90
        self.bala = None

    def apuntar(self, mouse_x, mouse_y):
        dx = mouse_x - self.x
        dy = self.y - mouse_y
        angulo = math.degrees(math.atan2(dy, dx))
        self.angulo = max(15, min(165, angulo))

    def disparar(self):
        if self.bala is None or not self.bala.activa:
            rad = math.radians(self.angulo)
            tip_x = self.x + LARGO_CANON * math.cos(rad)
            tip_y = self.y - LARGO_CANON * math.sin(rad)
            self.bala = Bala(tip_x, tip_y, self.angulo)

    def actualizar(self):
        if self.bala and self.bala.activa:
            self.bala.actualizar()

    def dibujar(self, pantalla):
        # ---------- COMPLETAR: Base del cañón ----------
        # PISTA: Dibuja un rectángulo en la posición del cañón
        #        - Fondo: NEGRO
        #        - Borde: ROJO (grosor 3)
        base_rect = pygame.Rect(self.x - 30, self.y - 20, 60, 40)
        pygame.draw.rect(pantalla, NEGRO, base_rect)
        pygame.draw.rect(pantalla, ROJO, base_rect, 3)

        # ---------- COMPLETAR: Ruedas ----------
        # PISTA: Dibuja dos cuadrados a los lados del cañón
        #        - Posición: a -28 y +28 del centro
        #        - Tamaño: 20x20
        #        - Fondo: NEGRO, Borde: AMARILLO (grosor 2)
        for ox in (-28, 28):
            wheel_rect = pygame.Rect(self.x + ox - 10, self.y + 8, 20, 20)
            pygame.draw.rect(pantalla, NEGRO, wheel_rect)
            pygame.draw.rect(pantalla, AMARILLO, wheel_rect, 2)

        # ---------- COMPLETAR: Tubo del cañón ----------
        # PISTA: Dibuja una línea desde la base hasta la punta
        #        - Calcula la punta con math.radians(self.angulo)
        #        - Línea gruesa (14px) color AZUL
        #        - Línea delgada (8px) color NEGRO
        rad = math.radians(self.angulo)
        ex = int(self.x + LARGO_CANON * math.cos(rad))
        ey = int(self.y - LARGO_CANON * math.sin(rad))
        pygame.draw.line(pantalla, AZUL, (self.x, self.y), (ex, ey), 14)
        pygame.draw.line(pantalla, NEGRO, (self.x, self.y), (ex, ey), 8)

        # ---------- Bala ----------
        if self.bala and self.bala.activa:
            self.bala.dibujar(pantalla)

    def obtener_bala(self):
        return self.bala


# ============================================================
#  💡 AYUDA:
#  - pygame.draw.rect(pantalla, color, rect, grosor)
#  - pygame.draw.line(pantalla, color, (x1,y1), (x2,y2), grosor)
#  - colors disponibles: NEGRO, ROJO, AZUL, AMARILLO, etc.
# ============================================================