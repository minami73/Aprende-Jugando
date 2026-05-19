// ============================================================
//  game.js  –  Lógica principal del juego (una partida)
// ============================================================

import { PREGUNTAS } from './questions.js';
import {
    ANCHO, ALTO, VERDE_OSCURO, NEGRO_PURO, NEGRO,
    VIDAS, TIEMPO_PREGUNTA, POSICIONES_X, BLOQUE_Y, MENSAJE_Y,
    ROJO, VERDE, BLANCO
} from './settings.js';
import { Canon } from './cannon.js';
import { Bloque } from './blocks.js';
import { HUD } from './ui.js';

export class Juego {
    constructor() {
        this.hud = new HUD();
        this.fuenteBloqueTamano = 22;
        this.fGrandeTamano = 38;
        this._reiniciar();
    }

    _reiniciar() {
        this.preguntas = this._shuffle([...PREGUNTAS]);
        this.indice = 0;
        this.vidas = VIDAS;
        this.puntaje = 0;
        this.timerMs = TIEMPO_PREGUNTA * 1000;
        this.canon = new Canon();
        this.bloques = [];
        this.mensaje = '';
        this.colorMensaje = BLANCO;
        this.msgTimer = 0;
        this.delayMs = 0;
        this.terminado = false;
        this.bloqueCorrecto = null;
        this.sigPregunta = false;
        this._cargarPregunta();
    }

    _shuffle(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
        return array;
    }

    _cargarPregunta() {
        this.canon.bala = null;
        this.bloqueCorrecto = null;
        this.sigPregunta = false;

        if (this.indice >= this.preguntas.length) {
            this.terminado = true;
            return;
        }

        const pregunta = this.preguntas[this.indice];
        this.timerMs = TIEMPO_PREGUNTA * 1000;

        const opciones = pregunta.opciones.map((texto, idx) => ({ idx, texto }));
        this._shuffle(opciones);

        this.bloques = [];
        for (let i = 0; i < opciones.length; i++) {
            const esCorrecto = opciones[i].idx === pregunta.correcta;
            this.bloques.push(new Bloque(POSICIONES_X[i], BLOQUE_Y, opciones[i].texto, esCorrecto));
        }
    }

    _mostrarMensaje(texto, color, frames = 90) {
        this.mensaje = texto;
        this.colorMensaje = color;
        this.msgTimer = frames;
    }

    actualizar(dt) {
        if (this.terminado) return;

        if (this.delayMs > 0) {
            this.delayMs -= dt;
            if (this.delayMs <= 0) {
                this.delayMs = 0;
                if (this.sigPregunta) {
                    this.indice++;
                    this.sigPregunta = false;
                }
                this._cargarPregunta();
            }
            if (this.msgTimer > 0) this.msgTimer--;
            return;
        }

        this.timerMs -= dt;
        if (this.timerMs <= 0) {
            this.timerMs = 0;
            this.vidas--;
            this._mostrarMensaje('Tiempo agotado!', ROJO);
            if (this.vidas <= 0) {
                this.terminado = true;
            } else {
                this.delayMs = 1200;
            }
            return;
        }

        this.canon.actualizar();
        for (const b of this.bloques) {
            b.actualizar();
        }

        if (this.bloqueCorrecto && this.bloqueCorrecto.destello === 0) {
            this.bloqueCorrecto.destruir();
            this.bloqueCorrecto = null;
        }
        if (this.msgTimer > 0) this.msgTimer--;

        const bala = this.canon.obtenerBala();
        if (bala && bala.activa) {
            for (const bloque of this.bloques) {
                if (bloque.verificarColision(bala)) {
                    bala.activa = false;
                    if (bloque.esCorrecto) {
                        bloque.destellar();
                        this.puntaje++;
                        this._mostrarMensaje('Correcto!', VERDE);
                        this.sigPregunta = true;
                        this.delayMs = 1000;
                        this.bloqueCorrecto = bloque;
                    } else {
                        bloque.sacudir();
                        this.vidas--;
                        this._mostrarMensaje('Incorrecto!', ROJO);
                        if (this.vidas <= 0) {
                            this.terminado = true;
                        }
                    }
                    break;
                }
            }
        }
    }

    manejarEvento(mouseX, mouseY, disparando) {
        if (this.terminado || this.delayMs > 0) return;
        this.canon.apuntar(mouseX, mouseY);
        if (disparando) {
            this.canon.disparar();
        }
    }

    dibujar(ctx) {
        ctx.fillStyle = `rgb(${NEGRO.join(',')})`;
        ctx.fillRect(0, 0, ANCHO, ALTO);

        ctx.fillStyle = `rgb(${VERDE_OSCURO.join(',')})`;
        ctx.fillRect(0, ALTO - 70, ANCHO, 70);
        ctx.strokeStyle = `rgb(${NEGRO_PURO.join(',')})`;
        ctx.lineWidth = 6;
        ctx.beginPath();
        ctx.moveTo(0, ALTO - 70);
        ctx.lineTo(ANCHO, ALTO - 70);
        ctx.stroke();

        for (const b of this.bloques) {
            b.dibujar(ctx, this.fuenteBloqueTamano);
        }

        this.canon.dibujar(ctx);

        this.hud.dibujarVidas(ctx, this.vidas);
        this.hud.dibujarTimer(ctx, Math.floor(this.timerMs / 1000));
        if (this.indice < this.preguntas.length) {
            this.hud.dibujarPregunta(
                ctx,
                this.preguntas[this.indice].pregunta,
                this.indice + 1,
                this.preguntas.length
            );
        }
        this.hud.dibujarInstrucciones(ctx);

        if (this.msgTimer > 0) {
            ctx.font = `bold ${this.fGrandeTamano}px Arial`;
            ctx.fillStyle = `rgb(${this.colorMensaje.join(',')})`;
            ctx.textAlign = 'center';
            ctx.fillText(this.mensaje, ANCHO / 2, MENSAJE_Y);
        }
    }

    esFin() {
        return this.terminado;
    }

    gano() {
        return this.puntaje === this.preguntas.length;
    }

    estadisticas() {
        return { puntaje: this.puntaje, total: this.preguntas.length };
    }
}