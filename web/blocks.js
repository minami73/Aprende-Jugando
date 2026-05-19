// ============================================================
//  blocks.js  –  Clase Bloque (opciones de respuesta)
// ============================================================

import { BLOQUE_ANCHO, BLOQUE_ALTO, AZUL, ROJO, VERDE, BLANCO, NEGRO_PURO } from './settings.js';

export class Bloque {
    constructor(cx, cy, texto, esCorrecto) {
        this.cx = cx;
        this.cy = cy;
        this.ancho = BLOQUE_ANCHO;
        this.alto = BLOQUE_ALTO;
        this.texto = texto;
        this.esCorrecto = esCorrecto;
        this.activo = true;
        this.sacudida = 0;
        this.destello = 0;
    }

    verificarColision(bala) {
        if (!this.activo || bala === null || !bala.activa) return false;

        return (
            Math.abs(bala.x - this.cx) <= this.ancho / 2 + bala.radio &&
            Math.abs(bala.y - this.cy) <= this.alto / 2 + bala.radio
        );
    }

    destruir() {
        this.activo = false;
    }

    sacudir() {
        this.sacudida = 25;
    }

    destellar() {
        this.destello = 20;
    }

    actualizar() {
        if (this.sacudida > 0) this.sacudida--;
        if (this.destello > 0) this.destello--;
    }

    dibujar(ctx, fuente) {
        if (!this.activo) return;

        let ox = 0;
        if (this.sacudida > 0) {
            ox = Math.floor(Math.random() * 7) - 3;
        }

        const rx = this.cx - this.ancho / 2 + ox;
        const ry = this.cy - this.alto / 2;

        let colorFondo = this.sacudida > 0 ? ROJO : AZUL;
        let colorBorde = NEGRO_PURO;

        if (this.destello > 0) {
            if (Math.floor(this.destello / 3) % 2 === 0) {
                colorFondo = VERDE;
                colorBorde = NEGRO_PURO;
            } else {
                colorFondo = [180, 255, 180];
                colorBorde = VERDE;
            }
        }

        ctx.fillStyle = `rgb(${colorFondo.join(',')})`;
        ctx.strokeStyle = `rgb(${colorBorde.join(',')})`;
        ctx.lineWidth = 3;

        this._roundRect(ctx, rx, ry, this.ancho, this.alto, 12);
        ctx.fill();
        ctx.stroke();

        const lineas = this._ajustarTexto(ctx, fuente);
        const altoLinea = 24;
        const totalAlto = lineas.length * altoLinea;
        let sy = this.cy - totalAlto / 2;

        ctx.fillStyle = `rgb(${BLANCO.join(',')})`;
        ctx.font = `bold ${fuente}px Arial`;
        ctx.textAlign = 'center';

        for (const linea of lineas) {
            ctx.fillText(linea, this.cx + ox, sy + fuente * 0.7);
            sy += altoLinea;
        }
    }

    _ajustarTexto(ctx, fuente) {
        const palabras = this.texto.split(' ');
        const lineas = [];
        let linea = '';
        const maxAncho = this.ancho - 14;

        ctx.font = `bold ${fuente}px Arial`;

        for (const p of palabras) {
            const prueba = (linea + ' ' + p).trim();
            const metrics = ctx.measureText(prueba);

            if (metrics.width <= maxAncho) {
                linea = prueba;
            } else {
                if (linea) lineas.push(linea);
                linea = p;
            }
        }
        if (linea) lineas.push(linea);

        return lineas;
    }

    _roundRect(ctx, x, y, w, h, r) {
        ctx.beginPath();
        ctx.moveTo(x + r, y);
        ctx.lineTo(x + w - r, y);
        ctx.quadraticCurveTo(x + w, y, x + w, y + r);
        ctx.lineTo(x + w, y + h - r);
        ctx.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
        ctx.lineTo(x + r, y + h);
        ctx.quadraticCurveTo(x, y + h, x, y + h - r);
        ctx.lineTo(x, y + r);
        ctx.quadraticCurveTo(x, y, x + r, y);
        ctx.closePath();
    }
}