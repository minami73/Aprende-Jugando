# ============================================================
#  main.py  –  Punto de entrada del juego
#  ¡Casi todo está listo! Solo falta configurar algo pequeño
# ============================================================

import pygame
import sys
from settings import *
from screens import PantallaInicio, PantallaFin
from game import Juego


def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption(TITULO)
    reloj = pygame.time.Clock()

    # ---------- FUENTES ----------
    # PISTA: Si quieres cambiar el tamaño de las fuentes, cambia los números
    fuentes = {
        "titulo"  : pygame.font.SysFont("Arial", 82, bold=True),
        "grande"  : pygame.font.SysFont("Arial", 38, bold=True),
        "normal"  : pygame.font.SysFont("Arial", 30, bold=True),
        "bloque"  : pygame.font.SysFont("Arial", 22, bold=True),
        "pequena" : pygame.font.SysFont("Arial", 18, bold=True),
    }

    # ---------- PANTALLAS ----------
    p_inicio = PantallaInicio(pantalla,
                              fuentes["titulo"],
                              fuentes["normal"],
                              fuentes["pequena"])
    p_fin    = PantallaFin   (pantalla,
                              fuentes["titulo"],
                              fuentes["normal"],
                              fuentes["pequena"])

    # Estado del juego: "inicio" | "jugando" | "fin"
    estado = "inicio"
    juego  = None

    # ---------- BUCLE PRINCIPAL ----------
    while True:
        dt = reloj.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if estado == "inicio":
                resultado = p_inicio.manejar_evento(evento)
                if resultado == "jugar":
                    juego  = Juego(pantalla, fuentes)
                    estado = "jugando"

            elif estado == "jugando":
                juego.manejar_evento(evento)

            elif estado == "fin":
                resultado = p_fin.manejar_evento(evento)
                if resultado == "reiniciar":
                    juego  = Juego(pantalla, fuentes)
                    estado = "jugando"
                elif resultado == "menu":
                    estado = "inicio"

        # ---------- ACTUALIZAR ----------
        if estado == "jugando":
            juego.actualizar(dt)
            if juego.es_fin():
                estado = "fin"

        # ---------- DIBUJAR ----------
        if estado == "inicio":
            p_inicio.dibujar()
        elif estado == "jugando":
            juego.dibujar()
        elif estado == "fin":
            pt, tot = juego.estadisticas()
            p_fin.dibujar(juego.gano(), pt, tot)

        pygame.display.flip()


if __name__ == "__main__":
    main()


# ============================================================
#  💡 TAREA: Cambia los números de las fuentes para probar diferentes tamaños
#  Pista: Solo cambia los números (ej: 82 -> 100) y observa el cambio
# ============================================================