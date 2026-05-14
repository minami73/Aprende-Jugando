# MAPA DEL PROYECTO - Aprende Jugando

## Archivos del Proyecto

| Archivo | Descripción |
|---------|-------------|
| main.py | Punto de entrada, inicializa pygame, fuentes y bucle principal |
| settings.py | Constantes globales (resolución, colores, posiciones) |
| cannon.py | Clases Canon y Bala |
| blocks.py | Clase Bloque (opciones de respuesta) |
| ui.py | HUD (vidas, timer, pregunta, instrucciones) |
| game.py | Lógica principal del juego |
| screens.py | Pantallas de inicio y fin |
| questions.py | Base de datos de preguntas |

---

## main.py
Punto de entrada. Inicializa pygame, crea fuentes y maneja el bucle principal del juego.

- **Líneas 18-25**: Fuentes (titulo, grande, normal, bloque, pequena)
- **Líneas 41-81**: Bucle principal (estados: inicio -> jugando -> fin)

---

## settings.py
Constantes globales del juego.

- **Línea 6-7**: Resolución (ANCHO=1600, ALTO=900)
- **Línea 11-22**: Paleta de colores (BLANCO, NEGRO, AZUL, ROJO, VERDE, AMARILLO, NARANJA, CELESTE)
- **Línea 25**: VIDAS = 3
- **Línea 26**: TIEMPO_PREGUNTA = 30 segundos
- **Línea 28-33**: CAÑÓN (CANON_X, CANON_Y, LARGO_CANON, VELOCIDAD_BALA, RADIO_BALA)
- **Línea 35-39**: BLOQUES (BLOQUE_ANCHO, BLOQUE_ALTO, BLOQUE_Y, POSICIONES_X)
- **Línea 43**: MENSAJE_Y (posición del feedback)

---

## cannon.py
Clases del cañón y la bala.

### Clase Bala (Líneas 10-31)
- __init__: posición, ángulo, velocidad
- actualizar: movimiento y detección de salida de pantalla
- dibujar: círculo amarillo con borde naranja

### Clase Canon (Líneas 34-87)
- __init__: posición, ángulo inicial=90° (vertical)
- apuntar: calcula ángulo según posición del mouse
- disparar: crea una Bala desde la punta del cañón
- dibujar:
  - Línea 64-67: Base (rectángulo negro con borde rojo)
  - Líneas 70-73: Ruedas (cuadrados negros con borde amarillo)
  - Líneas 76-80: Tubo (línea gruesa azul con borde negro)

---

## blocks.py
Clase Bloque (las opciones de respuesta).

- **Líneas 11-20**: __init__ (cx, cy, texto, es_correcto, activo, sacudida, destello)
- **Líneas 23-27**: verificar_colision (detecta si una bala toca el bloque)
- **Líneas 29-31**: destruir (desactiva el bloque)
- **Líneas 33-34**: sacudir (inicia animación de vibración)
- **Líneas 36-37**: destellar (inicia animación de destello)
- **Líneas 39-43**: actualizar (decrementa contadores de animación)
- **Líneas 47-61**: _ajustar_texto (ajusta texto al ancho del bloque)
- **Líneas 63-92**: dibujar (rectángulo, borde 3px negro, texto)

---

## ui.py
HUD (Heads-Up Display).

### Vida (Líneas 32-37)
- dibujar_vidas: círculos rojos con borde negro de 3px

### Timer (Líneas 41-46)
- dibujar_timer: número grande (verde si >10s, rojo si <=10s) + etiqueta "TIEMPO"

### Pregunta (Líneas 50-85)
- dibujar_pregunta:
  - "Pregunta X/Y" centrado arriba
  - Caja de pregunta (rectángulo azul oscuro con borde negro de 3px)
  - Texto de la pregunta ajustado al ancho

### Instrucciones (Líneas 89-92)
- dibujar_instrucciones: texto en el pie de pantalla

---

## game.py
Lógica principal del juego.

- **Líneas 15-22**: __init__ (recibe pantalla y fuentes)
- **Líneas 26-40**: _reiniciar (inicializa todo para una nueva partida)
- **Líneas 43-60**: _cargar_pregunta (carga la sig. pregunta, mezcla opciones)
- **Líneas 64-67**: _mostrar_mensaje (muestra "Correcto!", "Incorrecto!", etc.)
- **Líneas 71-126**: actualizar
  - Pausa entre preguntas (delay_ms)
  - Cuenta regresiva del timer
  - Actualizar cañón y bloques
  - Detección de colisión bala-bloque
  - Manejo de respuesta correcta (destello, mensaje, delay) e incorrecta (sacudida, mensaje, perder vida)
- **Líneas 130-136**: manejar_evento (mouse motion y click)
- **Líneas 140-175**: dibujar
  - Fondo negro
  - Suelo verde (70px de alto)
  - Bloques de respuestas
  - Cañón
  - HUD (vidas, timer, pregunta)
  - Mensaje de feedback

---

## screens.py
Pantallas de inicio y fin.

### PantallaInicio (Líneas 12-53)
- **Línea 21**: Fondo negro
- **Líneas 24-31**: Título "Aprende" (amarillo) + "Jugando" (blanco) + subtítulo "Finanzas - Nivel Secundaria"
- **Líneas 33-43**: Botón JUGAR (rectángulo verde, borde blanco)
- **Líneas 45-47**: Créditos en el pie

### PantallaFin (Líneas 56-99)
- **Línea 66**: Fondo negro
- **Líneas 68-79**: Título "GANASTE" (amarillo) o "GAME OVER" (rojo) + subtítulo + puntaje
- **Líneas 81-84**: Botones "Reiniciar" y "Menú Principal" (fondo azul, borde negro de 3px)
- **Líneas 86-88**: Créditos en el pie

---

## questions.py
Base de datos de preguntas. Cada pregunta es un diccionario:
```python
{
    "pregunta": "texto de la pregunta",
    "opciones": ["opción A", "opción B", "opción C", "opción D"],
    "correcta": 0  # índice de la respuesta correcta (0-3)
}
```

---

## Colores utilizados
| Color | RGB | Usado en |
|-------|-----|----------|
| NEGRO | (30, 30, 30) | Fondos, bordes |
| BLANCO | (245, 245, 245) | Textos, bordes |
| AZUL | (100, 145, 175) | Bloques de respuesta |
| AZUL_OSCURO | (40, 60, 90) | Caja de pregunta |
| ROJO | (165, 85, 85) | Vidas, Pasto (era verde), Base cañón |
| VERDE | (90, 140, 90) | Destello correcto |
| AMARILLO | (200, 180, 60) | Título, bordes bloques sacudida |
| NARANJA | (180, 120, 70) | - |
| CELESTE | (150, 175, 195) | - |

---

## Posiciones importantes
- Título inicio: y=100 y y=210
- Subtítulo: y=340
- Botón JUGAR: y=420
- Bloque pregunta: BOX_Y=112, BOX_X=80, BOX_W=ANCHO-160
- Bloques respuestas: Y=325, X=[330, 800, 1270]
- Cañón: CANON_Y=ALTO-85=815
- Suelo: Y=ALTO-70=830, altura=70
- Timer: corner superior derecha (ANCHO-14, 10) y (ANCHO-14, 50)
- Vidas: Y=30, X inicial=30
- Pregunta X/Y: Y=15