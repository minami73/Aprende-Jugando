// ============================================================
//  main.js  –  Punto de entrada del juego
// ============================================================

import { ANCHO, ALTO, TITULO } from './settings.js';
import { PantallaInicio, PantallaFin } from './screens.js';
import { Juego } from './game.js';

class Main {
    constructor() {
        this.canvas = document.getElementById('canvas');
        this.canvas.width = ANCHO;
        this.canvas.height = ALTO;
        this.ctx = this.canvas.getContext('2d');

        this.estado = 'inicio';
        this.juego = null;
        this.mouseX = 0;
        this.mouseY = 0;
        this.ultimoTiempo = 0;

        this.pInicio = new PantallaInicio();
        this.pFin = new PantallaFin();

        this._configurarEventos();
        requestAnimationFrame((t) => this._bucle(t));
    }

    _configurarEventos() {
        this.canvas.addEventListener('mousemove', (e) => {
            const rect = this.canvas.getBoundingClientRect();
            this.mouseX = e.clientX - rect.left;
            this.mouseY = e.clientY - rect.top;

            if (this.estado === 'jugando' && this.juego) {
                this.juego.manejarEvento(this.mouseX, this.mouseY, false);
            }
        });

        this.canvas.addEventListener('mousedown', (e) => {
            if (e.button !== 0) return;

            if (this.estado === 'inicio') {
                const resultado = this.pInicio.manejarClick(this.mouseX, this.mouseY);
                if (resultado === 'jugar') {
                    this.juego = new Juego();
                    this.estado = 'jugando';
                }
            } else if (this.estado === 'jugando' && this.juego) {
                this.juego.manejarEvento(this.mouseX, this.mouseY, true);
            } else if (this.estado === 'fin') {
                const resultado = this.pFin.manejarClick(this.mouseX, this.mouseY);
                if (resultado === 'reiniciar') {
                    this.juego = new Juego();
                    this.estado = 'jugando';
                } else if (resultado === 'menu') {
                    this.estado = 'inicio';
                }
            }
        });
    }

    _bucle(timestamp) {
        const dt = timestamp - this.ultimoTiempo;
        this.ultimoTiempo = timestamp;

        if (this.estado === 'jugando' && this.juego) {
            this.juego.actualizar(dt);
            if (this.juego.esFin()) {
                this.estado = 'fin';
            }
        }

        if (this.estado === 'inicio') {
            this.pInicio.dibujar(this.ctx, this.mouseX, this.mouseY);
        } else if (this.estado === 'jugando' && this.juego) {
            this.juego.dibujar(this.ctx);
        } else if (this.estado === 'fin') {
            const stats = this.juego.estadisticas();
            this.pFin.dibujar(this.ctx, this.juego.gano(), stats.puntaje, stats.total, this.mouseX, this.mouseY);
        }

        requestAnimationFrame((t) => this._bucle(t));
    }
}

window.addEventListener('DOMContentLoaded', () => {
    new Main();
});