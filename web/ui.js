// ============================================================
//  ui.js  –  HUD (vidas, timer, pregunta, instrucciones)
// ============================================================

import { ANCHO, ALTO, ROJO, NEGRO_PURO, VERDE, AMARILLO, BLANCO, GRIS, AZUL_OSCURO } from './settings.js';

export const HUD_ALTO = 140;

export class HUD {
    constructor() {
        this.fuenteTamano = 30;
        this.fTimerTamano = 38;
        this.fPequenaTamano = 18;
    }

    dibujarVidas(ctx, vidas) {
        const radio = 13;
        for (let i = 0; i < vidas; i++) {
            const cx = 30 + i * 34;
            ctx.beginPath();
            ctx.arc(cx, 30, radio, 0, Math.PI * 2);
            ctx.fillStyle = `rgb(${ROJO.join(',')})`;
            ctx.fill();
            ctx.strokeStyle = `rgb(${NEGRO_PURO.join(',')})`;
            ctx.lineWidth = 3;
            ctx.stroke();
        }
    }

    dibujarTimer(ctx, segundos) {
        const color = segundos > 10 ? VERDE : ROJO;

        ctx.font = `bold ${this.fTimerTamano}px Arial`;
        ctx.fillStyle = `rgb(${color.join(',')})`;
        ctx.textAlign = 'right';
        ctx.fillText(Math.max(0, segundos).toString(), ANCHO - 14, 40);

        ctx.font = `bold ${this.fPequenaTamano}px Arial`;
        ctx.fillStyle = `rgb(${BLANCO.join(',')})`;
        ctx.fillText('TIEMPO', ANCHO - 14, 62);
    }

    dibujarPregunta(ctx, texto, numero, total) {
        ctx.font = `bold ${this.fuenteTamano}px Arial`;
        ctx.fillStyle = `rgb(${AMARILLO.join(',')})`;
        ctx.textAlign = 'center';
        ctx.fillText(`Pregunta  ${numero} / ${total}`, ANCHO / 2, 35);

        const BOX_X = 80;
        const BOX_Y = 112;
        const BOX_W = ANCHO - 160;
        const BOX_H = 88;

        ctx.fillStyle = `rgb(${AZUL_OSCURO.join(',')})`;
        ctx.strokeStyle = `rgb(${NEGRO_PURO.join(',')})`;
        ctx.lineWidth = 3;
        this._roundRect(ctx, BOX_X, BOX_Y, BOX_W, BOX_H, 10);
        ctx.fill();
        ctx.stroke();

        const margen = 24;
        const maxW = BOX_W - margen * 2;
        const palabras = texto.split(' ');
        const lineas = [];
        let linea = '';

        ctx.font = `bold ${this.fuenteTamano}px Arial`;

        for (const p of palabras) {
            const prueba = (linea + ' ' + p).trim();
            const metrics = ctx.measureText(prueba);

            if (metrics.width <= maxW) {
                linea = prueba;
            } else {
                if (linea) lineas.push(linea);
                linea = p;
            }
        }
        if (linea) lineas.push(linea);

        const altoTexto = lineas.length * this.fuenteTamano;
        let sy = BOX_Y + (BOX_H - altoTexto) / 2;

        ctx.fillStyle = `rgb(${BLANCO.join(',')})`;
        ctx.textAlign = 'center';

        for (const l of lineas) {
            ctx.fillText(l, ANCHO / 2, sy + this.fuenteTamano * 0.7);
            sy += this.fuenteTamano;
        }
    }

    dibujarInstrucciones(ctx) {
        ctx.font = `bold ${this.fPequenaTamano}px Arial`;
        ctx.fillStyle = `rgb(${GRIS.join(',')})`;
        ctx.textAlign = 'center';
        ctx.fillText('Mueve el raton para apuntar  |  Clic para disparar', ANCHO / 2, ALTO - 6);
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