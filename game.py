# ============================================================
#  game.py  –  Lógica principal del juego (una partida)
# ============================================================

import pygame
import random
from settings import *
from questions import PREGUNTAS
from cannon import Canon
from blocks import Bloque
from ui import HUD


class Juego:
    def __init__(self, pantalla, fuentes):
        self.pantalla  = pantalla
        self.fuente    = fuentes["normal"]
        self.f_grande  = fuentes["grande"]
        self.f_pequena = fuentes["pequena"]
        self.f_bloque  = fuentes["bloque"]   # fuente más chica para el texto de los bloques
        self.hud       = HUD(fuentes["normal"], fuentes["grande"], fuentes["pequena"])
        self._reiniciar()

    # ------------------------------------------------------------------ setup

    def _reiniciar(self):
        self.preguntas = random.sample(PREGUNTAS, len(PREGUNTAS))
        self.indice    = 0
        self.vidas     = VIDAS
        self.puntaje   = 0
        self.timer_ms  = TIEMPO_PREGUNTA * 1000
        self.canon     = Canon()
        self.bloques   = []
        self.mensaje       = ""
        self.color_mensaje = BLANCO
        self.msg_timer     = 0
        self.delay_ms      = 0
        self.terminado     = False
        self.bloque_correcto = None
        self.sig_pregunta = False
        self._cargar_pregunta()

    def _cargar_pregunta(self):
        self.canon.bala = None
        self.bloque_correcto = None
        self.sig_pregunta = False
        if self.indice >= len(self.preguntas):
            self.terminado = True
            return

        pregunta = self.preguntas[self.indice]
        self.timer_ms = TIEMPO_PREGUNTA * 1000

        opciones = list(enumerate(pregunta["opciones"]))
        random.shuffle(opciones)

        self.bloques = []
        for i, (idx_orig, texto) in enumerate(opciones):
            es_correcto = (idx_orig == pregunta["correcta"])
            self.bloques.append(
                Bloque(POSICIONES_X[i], BLOQUE_Y, texto, es_correcto)
            )

    # ----------------------------------------------------------------- helpers

    def _mostrar_mensaje(self, texto, color, frames=90):
        self.mensaje       = texto
        self.color_mensaje = color
        self.msg_timer     = frames

    # ------------------------------------------------------------------ update

    def actualizar(self, dt):
        if self.terminado:
            return

        # Pausa entre preguntas
        if self.delay_ms > 0:
            self.delay_ms -= dt
            if self.delay_ms <= 0:
                self.delay_ms = 0
                if self.sig_pregunta:
                    self.indice += 1
                    self.sig_pregunta = False
                self._cargar_pregunta()
            if self.msg_timer > 0:
                self.msg_timer -= 1
            return

        # Cuenta regresiva
        self.timer_ms -= dt
        if self.timer_ms <= 0:
            self.timer_ms = 0
            self.vidas -= 1
            self._mostrar_mensaje("Tiempo agotado!", ROJO)
            if self.vidas <= 0:
                self.terminado = True
            else:
                self.delay_ms = 1200
            return

        # Actualizar cañón y bloques
        self.canon.actualizar()
        for b in self.bloques:
            b.actualizar()
        if self.bloque_correcto and self.bloque_correcto.destello == 0:
            self.bloque_correcto.destruir()
            self.bloque_correcto = None
        if self.msg_timer > 0:
            self.msg_timer -= 1

        # Detección de colisión bala-bloque
        bala = self.canon.obtener_bala()
        if bala and bala.activa:
            for bloque in self.bloques:
                if bloque.verificar_colision(bala):
                    bala.activa = False
                    if bloque.es_correcto:
                        bloque.destellar()
                        self.puntaje += 1
                        self._mostrar_mensaje("Correcto!", VERDE)
                        self.sig_pregunta = True
                        self.delay_ms = 1000
                        self.bloque_correcto = bloque
                    else:
                        bloque.sacudir()
                        self.vidas -= 1
                        self._mostrar_mensaje("Incorrecto!", ROJO)
                        if self.vidas <= 0:
                            self.terminado = True
                    break

    # ------------------------------------------------------------------ eventos

    def manejar_evento(self, evento):
        if self.terminado or self.delay_ms > 0:
            return
        if evento.type == pygame.MOUSEMOTION:
            self.canon.apuntar(*evento.pos)
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            self.canon.disparar()

    # ------------------------------------------------------------------ dibujo

    def dibujar(self):
        # Cielo
        self.pantalla.fill(NEGRO)

        # Suelo
        pygame.draw.rect(self.pantalla, VERDE_OSCURO,
                         (0, ALTO - 70, ANCHO, 70))
        pygame.draw.line(self.pantalla, NEGRO_PURO,
                         (0, ALTO - 70), (ANCHO, ALTO - 70), 6)

        # Bloques  (usan fuente más pequeña para que el texto quepa)
        for b in self.bloques:
            b.dibujar(self.pantalla, self.f_bloque)

        # Cañón
        self.canon.dibujar(self.pantalla)

        # HUD
        self.hud.dibujar_vidas(self.pantalla, self.vidas)
        self.hud.dibujar_timer(self.pantalla, int(self.timer_ms / 1000))
        if self.indice < len(self.preguntas):
            self.hud.dibujar_pregunta(
                self.pantalla,
                self.preguntas[self.indice]["pregunta"],
                self.indice + 1,
                len(self.preguntas),
            )
        self.hud.dibujar_instrucciones(self.pantalla)

        # Mensaje de feedback (Correcto / Incorrecto / Tiempo)
        # Se muestra en MENSAJE_Y: zona despejada entre bloques y cañón
        if self.msg_timer > 0:
            msg = self.f_grande.render(self.mensaje, True, self.color_mensaje)
            self.pantalla.blit(
                msg, msg.get_rect(center=(ANCHO // 2, MENSAJE_Y))
            )

    # ------------------------------------------------------------------ estado

    def es_fin(self):
        return self.terminado

    def gano(self):
        return self.puntaje == len(self.preguntas)

    def estadisticas(self):
        return self.puntaje, len(self.preguntas)
