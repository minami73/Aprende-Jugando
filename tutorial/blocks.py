# ============================================================
#  blocks.py  –  Clase Bloque (las opciones de respuesta)
#  ¡Casi todo está listo! Aquí se dibujan los bloques de respuestas
# ============================================================

import pygame
import random
from settings import *


class Bloque:
    def __init__(self, cx, cy, texto, es_correcto):
        self.cx = cx          # centro x
        self.cy = cy          # centro y
        self.ancho = BLOQUE_ANCHO
        self.alto  = BLOQUE_ALTO
        self.texto = texto
        self.es_correcto = es_correcto
        self.activo = True
        self.sacudida = 0
        self.destello = 0

    # ---------- LÓGICA ----------

    def verificar_colision(self, bala):
        if not self.activo or bala is None or not bala.activa:
            return False
        # PISTA: Compara las posiciones de la bala y el bloque
        return (abs(bala.x - self.cx) <= self.ancho / 2 + bala.radio and
                abs(bala.y - self.cy) <= self.alto  / 2 + bala.radio)

    def destruir(self):
        self.activo = False

    def sacudir(self):
        # PISTA: ¿Cuántos frames quieres que dure la animación?
        self.sacudida = 25

    def destellar(self):
        self.destello = 20

    def actualizar(self):
        if self.sacudida > 0:
            self.sacudida -= 1
        if self.destello > 0:
            self.destello -= 1

    # ---------- DIBUJO ----------

    def _ajustar_texto(self, fuente):
        palabras = self.texto.split()
        lineas, linea = [], ""
        for p in palabras:
            prueba = (linea + " " + p).strip()
            if fuente.size(prueba)[0] <= self.ancho - 14:
                linea = prueba
            else:
                if linea:
                    lineas.append(linea)
                linea = p
        if linea:
            lineas.append(linea)
        return lineas

    def dibujar(self, pantalla, fuente):
        if not self.activo:
            return

        # Efecto de sacudida (vibración)
        ox = random.randint(-3, 3) if self.sacudida > 0 else 0
        rx = self.cx - self.ancho // 2 + ox
        ry = self.cy - self.alto  // 2

        rect = pygame.Rect(rx, ry, self.ancho, self.alto)

        # ---------- COMPLETAR: Colores ----------
        # PISTA: ¿Qué color quieres cuando está sacudido? ¿Y normalmente?
        #        - Normal: fondo AZUL, borde NEGRO
        #        - Sacudido: fondo ROJO, borde AMARILLO
        color_fondo = ROJO if self.sacudida > 0 else AZUL
        color_borde = AMARILLO if self.sacudida > 0 else NEGRO

        # Efecto de destello (cuando es正确答案)
        if self.destello > 0:
            if (self.destello // 3) % 2 == 0:
                color_fondo = VERDE
                color_borde = NEGRO
            else:
                color_fondo = (180, 255, 180)
                color_borde = VERDE

        # PISTA: Dibuja el rectángulo con borde de 3px
        pygame.draw.rect(pantalla, color_fondo, rect, border_radius=12)
        pygame.draw.rect(pantalla, color_borde, rect, 3, border_radius=12)

        # Texto del bloque
        lineas = self._ajustar_texto(fuente)
        total_h = len(lineas) * fuente.get_height()
        sy = self.cy - total_h // 2

        for linea in lineas:
            surf = fuente.render(linea, True, BLANCO)
            pantalla.blit(surf, surf.get_rect(centerx=self.cx + ox, y=sy))
            sy += fuente.get_height()


# ============================================================
#  💡 TAREA EXTRA:
#  - Prueba cambiar los colores de los bloques
#  - ¿Qué pasa si cambias el tiempo de 'sacudida' o 'destello'?
# ============================================================