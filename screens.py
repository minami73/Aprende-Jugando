# ============================================================
#  screens.py  –  Pantalla de inicio y pantalla de fin
# ============================================================

import pygame
import sys
from settings import *

CREDITOS = "Elaborado por: [Tu Nombre]   |   Materia: Finanzas   |   2026"


class PantallaInicio:
    def __init__(self, pantalla, fuente_titulo, fuente_normal, fuente_pequena):
        self.pantalla     = pantalla
        self.f_titulo     = fuente_titulo
        self.f_normal     = fuente_normal
        self.f_pequena    = fuente_pequena
        self.btn_jugar    = pygame.Rect(ANCHO // 2 - 110, 420, 220, 64)

    def dibujar(self):
        self.pantalla.fill(NEGRO)

        # Título
        t1 = self.f_titulo.render("Aprende", True, AMARILLO)
        t2 = self.f_titulo.render("Jugando", True, BLANCO)
        self.pantalla.blit(t1, t1.get_rect(centerx=ANCHO // 2, y=100))
        self.pantalla.blit(t2, t2.get_rect(centerx=ANCHO // 2, y=210))

        # Subtítulo materia
        sub = self.f_normal.render("Finanzas  –  Nivel Secundaria", True, CELESTE)
        self.pantalla.blit(sub, sub.get_rect(centerx=ANCHO // 2, y=340))

        # Botón JUGAR
        mouse = pygame.mouse.get_pos()
        color_btn = (40, 170, 60) if self.btn_jugar.collidepoint(mouse) else (25, 120, 40)
        pygame.draw.rect(self.pantalla, color_btn,  self.btn_jugar, border_radius=16)
        pygame.draw.rect(self.pantalla, BLANCO,     self.btn_jugar, 3, border_radius=16)
        texto_btn = self.f_normal.render("JUGAR", True, BLANCO)
        self.pantalla.blit(texto_btn, texto_btn.get_rect(center=self.btn_jugar.center))

        # Créditos
        cr = self.f_pequena.render(CREDITOS, True, GRIS)
        self.pantalla.blit(cr, cr.get_rect(centerx=ANCHO // 2, bottom=ALTO - 12))

    def manejar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if self.btn_jugar.collidepoint(evento.pos):
                return "jugar"
        return None


class PantallaFin:
    def __init__(self, pantalla, fuente_titulo, fuente_normal, fuente_pequena):
        self.pantalla  = pantalla
        self.f_titulo  = fuente_titulo
        self.f_normal  = fuente_normal
        self.f_pequena = fuente_pequena
        self.btn_reiniciar = pygame.Rect(ANCHO // 2 - 130, 360, 260, 60)
        self.btn_menu      = pygame.Rect(ANCHO // 2 - 130, 440, 260, 60)

    def dibujar(self, gano, puntaje, total):
        self.pantalla.fill(NEGRO)

        if gano:
            titulo = self.f_titulo.render("¡GANASTE!", True, AMARILLO)
            sub    = self.f_normal.render("Excelente dominio de Finanzas", True, VERDE)
        else:
            titulo = self.f_titulo.render("GAME OVER", True, ROJO)
            sub    = self.f_normal.render("Sigue practicando, tu puedes!", True, (200, 180, 60))

        self.pantalla.blit(titulo, titulo.get_rect(centerx=ANCHO // 2, y=110))
        self.pantalla.blit(sub,    sub.get_rect(centerx=ANCHO // 2,    y=215))

        pt = self.f_normal.render(f"Puntaje:  {puntaje}  /  {total}", True, BLANCO)
        self.pantalla.blit(pt, pt.get_rect(centerx=ANCHO // 2, y=280))

        mouse = pygame.mouse.get_pos()
        for btn, label in [(self.btn_reiniciar, "Reiniciar"),
                           (self.btn_menu,      "Menu Principal")]:
            color = AZUL if btn.collidepoint(mouse) else AZUL_OSCURO
            pygame.draw.rect(self.pantalla, color,  btn, border_radius=12)
            pygame.draw.rect(self.pantalla, NEGRO_PURO, btn, 3, border_radius=12)
            t = self.f_normal.render(label, True, BLANCO)
            self.pantalla.blit(t, t.get_rect(center=btn.center))

        cr = self.f_pequena.render(CREDITOS, True, GRIS)
        self.pantalla.blit(cr, cr.get_rect(centerx=ANCHO // 2, bottom=ALTO - 12))

    def manejar_evento(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if self.btn_reiniciar.collidepoint(evento.pos):
                return "reiniciar"
            if self.btn_menu.collidepoint(evento.pos):
                return "menu"
        return None
