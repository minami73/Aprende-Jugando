// ============================================================
//  settings.js  –  Constantes globales del juego
// ============================================================

export const ANCHO = 1280;
export const ALTO = 720;
export const TITULO = "Aprende Jugando – Finanzas";

// Colores  (R, G, B) - Paleta desaturada
export const BLANCO = [245, 245, 245];
export const NEGRO_PURO = [0, 0, 0];
export const NEGRO = [30, 30, 30];
export const GRIS = [150, 150, 150];
export const AZUL = [100, 145, 175];
export const AZUL_OSCURO = [40, 60, 90];
export const ROJO = [165, 85, 85];
export const VERDE = [90, 140, 90];
export const VERDE_OSCURO = [45, 100, 55];
export const AMARILLO = [200, 180, 60];
export const NARANJA = [180, 120, 70];
export const CELESTE = [150, 175, 195];

// Jugabilidad
export const VIDAS = 3;
export const TIEMPO_PREGUNTA = 30;

// Cañón
export const CANON_X = Math.floor(ANCHO / 2);
export const CANON_Y = ALTO - 85;
export const LARGO_CANON = 60;
export const VELOCIDAD_BALA = 12;
export const RADIO_BALA = 11;

// Bloques de respuesta
export const BLOQUE_ANCHO = 290;
export const BLOQUE_ALTO = 100;
export const BLOQUE_Y = 325;
export const POSICIONES_X = [260, 640, 1020];  // Centrados para 1280px (margen 115px, bloque 290px, espacio 90px)

// Posición vertical del mensaje de feedback
export const MENSAJE_Y = 490;

// FPS
export const FPS = 60;