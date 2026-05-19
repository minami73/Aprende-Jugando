// ============================================================
//  cannon.js  –  Clases Bala y Canon
// ============================================================

import {
    ANCHO, ALTO, CANON_X, CANON_Y,
    LARGO_CANON, VELOCIDAD_BALA, RADIO_BALA,
    AMARILLO, NARANJA, AZUL, NEGRO, ROJO, NEGRO_PURO
} from './settings.js';

export class Bala {
    constructor(x, y, anguloGrados) {
        this.x = x;
        this.y = y;
        this.radio = RADIO_BALA;
        this.activa = true;

        const rad = anguloGrados * Math.PI / 180;
        this.vx = VELOCIDAD_BALA * Math.cos(rad);
        this.vy = -VELOCIDAD_BALA * Math.sin(rad);
    }

    actualizar() {
        this.x += this.vx;
        this.y += this.vy;

        if (this.x < 0 || this.x > ANCHO || this.y < 0 || this.y > ALTO) {
            this.activa = false;
        }
    }

    dibujar(ctx) {
        if (!this.activa) return;

        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radio, 0, Math.PI * 2);
        ctx.fillStyle = `rgb(${AMARILLO.join(',')})`;
        ctx.fill();

        ctx.strokeStyle = `rgb(${NARANJA.join(',')})`;
        ctx.lineWidth = 2;
        ctx.stroke();
    }
}

export class Canon {
    constructor() {
        this.x = CANON_X;
        this.y = CANON_Y;
        this.angulo = 90;
        this.bala = null;
    }

    apuntar(mouseX, mouseY) {
        const dx = mouseX - this.x;
        const dy = this.y - mouseY;
        let angulo = Math.atan2(dy, dx) * 180 / Math.PI;
        this.angulo = Math.max(15, Math.min(165, angulo));
    }

    disparar() {
        if (this.bala === null || !this.bala.activa) {
            const rad = this.angulo * Math.PI / 180;
            const tipX = this.x + LARGO_CANON * Math.cos(rad);
            const tipY = this.y - LARGO_CANON * Math.sin(rad);
            this.bala = new Bala(tipX, tipY, this.angulo);
        }
    }

    actualizar() {
        if (this.bala && this.bala.activa) {
            this.bala.actualizar();
        }
    }

    dibujar(ctx) {
        // Base del cañón
        ctx.fillStyle = `rgb(${NEGRO.join(',')})`;
        ctx.strokeStyle = `rgb(${ROJO.join(',')})`;
        ctx.lineWidth = 3;

        const baseX = this.x - 30;
        const baseY = this.y - 20;
        this._roundRect(ctx, baseX, baseY, 60, 40, 8);
        ctx.fill();
        ctx.stroke();

        // Ruedas
        ctx.fillStyle = `rgb(${NEGRO.join(',')})`;
        ctx.strokeStyle = `rgb(${AMARILLO.join(',')})`;
        ctx.lineWidth = 2;

        for (const ox of [-28, 28]) {
            this._roundRect(ctx, this.x + ox - 10, this.y + 8, 20, 20, 4);
            ctx.fill();
            ctx.stroke();
        }

        // Tubo del cañón
        const rad = this.angulo * Math.PI / 180;
        const ex = this.x + LARGO_CANON * Math.cos(rad);
        const ey = this.y - LARGO_CANON * Math.sin(rad);

        ctx.beginPath();
        ctx.moveTo(this.x, this.y);
        ctx.lineTo(ex, ey);
        ctx.strokeStyle = `rgb(${NEGRO.join(',')})`;
        ctx.lineWidth = 14;
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(this.x, this.y);
        ctx.lineTo(ex, ey);
        ctx.strokeStyle = `rgb(${AZUL.join(',')})`;
        ctx.lineWidth = 8;
        ctx.stroke();

        // Bala
        if (this.bala && this.bala.activa) {
            this.bala.dibujar(ctx);
        }
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

    obtenerBala() {
        return this.bala;
    }
}