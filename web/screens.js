// ============================================================
//  screens.js  –  Pantalla de inicio y pantalla de fin
// ============================================================

import { ANCHO, ALTO, NEGRO, AMARILLO, BLANCO, CELESTE, GRIS, VERDE, ROJO, AZUL, AZUL_OSCURO, NEGRO_PURO } from './settings.js';

const CREDITOS = "Elaborado por: [Tu Nombre]   |   Materia: Finanzas   |   2026";

export class PantallaInicio {
    constructor() {
        this.btnJugar = {
            x: ANCHO / 2 - 110,
            y: 400,
            w: 220,
            h: 64
        };
        this.fTituloTamano = 82;
        this.fNormalTamano = 30;
        this.fPequenaTamano = 18;
    }

    dibujar(ctx, mouseX, mouseY) {
        ctx.fillStyle = `rgb(${NEGRO.join(',')})`;
        ctx.fillRect(0, 0, ANCHO, ALTO);

        ctx.font = `bold ${this.fTituloTamano}px Arial`;
        ctx.textAlign = 'center';
        ctx.fillStyle = `rgb(${AMARILLO.join(',')})`;
        ctx.fillText('Aprende', ANCHO / 2, 100);
        ctx.fillStyle = `rgb(${BLANCO.join(',')})`;
        ctx.fillText('Jugando', ANCHO / 2, 200);

        ctx.font = `bold ${this.fNormalTamano}px Arial`;
        ctx.fillStyle = `rgb(${CELESTE.join(',')})`;
        ctx.fillText('Finanzas  –  Nivel Secundaria', ANCHO / 2, 320);

        const hover = this._colisionBtn(mouseX, mouseY);
        const colorBtn = hover ? '40, 170, 60' : '25, 120, 40';

        ctx.fillStyle = `rgb(${colorBtn})`;
        ctx.strokeStyle = `rgb(${BLANCO.join(',')})`;
        ctx.lineWidth = 3;
        this._roundRect(ctx, this.btnJugar.x, this.btnJugar.y, this.btnJugar.w, this.btnJugar.h, 16);
        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = `rgb(${BLANCO.join(',')})`;
        ctx.font = `bold ${this.fNormalTamano}px Arial`;
        ctx.fillText('JUGAR', this.btnJugar.x + this.btnJugar.w / 2, this.btnJugar.y + this.btnJugar.h / 2 + this.fNormalTamano * 0.35);

        ctx.font = `bold ${this.fPequenaTamano}px Arial`;
        ctx.fillStyle = `rgb(${GRIS.join(',')})`;
        ctx.fillText(CREDITOS, ANCHO / 2, ALTO - 12);
    }

    manejarClick(mouseX, mouseY) {
        if (this._colisionBtn(mouseX, mouseY)) {
            return 'jugar';
        }
        return null;
    }

    _colisionBtn(mx, my) {
        return mx >= this.btnJugar.x && mx <= this.btnJugar.x + this.btnJugar.w &&
               my >= this.btnJugar.y && my <= this.btnJugar.y + this.btnJugar.h;
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

export class PantallaFin {
    constructor() {
        this.btnReiniciar = { x: ANCHO / 2 - 130, y: 340, w: 260, h: 60 };
        this.btnMenu = { x: ANCHO / 2 - 130, y: 420, w: 260, h: 60 };
        this.fTituloTamano = 82;
        this.fNormalTamano = 30;
        this.fPequenaTamano = 18;
    }

    dibujar(ctx, gano, puntaje, total, mouseX, mouseY) {
        ctx.fillStyle = `rgb(${NEGRO.join(',')})`;
        ctx.fillRect(0, 0, ANCHO, ALTO);

        ctx.font = `bold ${this.fTituloTamano}px Arial`;
        ctx.textAlign = 'center';

        if (gano) {
            ctx.fillStyle = `rgb(${AMARILLO.join(',')})`;
            ctx.fillText('GANASTE!', ANCHO / 2, 120);
            ctx.font = `bold ${this.fNormalTamano}px Arial`;
            ctx.fillStyle = `rgb(${VERDE.join(',')})`;
            ctx.fillText('Excelente dominio de Finanzas', ANCHO / 2, 200);
        } else {
            ctx.fillStyle = `rgb(${ROJO.join(',')})`;
            ctx.fillText('GAME OVER', ANCHO / 2, 120);
            ctx.font = `bold ${this.fNormalTamano}px Arial`;
            ctx.fillStyle = `rgb(${AMARILLO.join(',')})`;
            ctx.fillText('Sigue practicando, tu puedes!', ANCHO / 2, 200);
        }

        ctx.font = `bold ${this.fNormalTamano}px Arial`;
        ctx.fillStyle = `rgb(${BLANCO.join(',')})`;
        ctx.fillText(`Puntaje:  ${puntaje}  /  ${total}`, ANCHO / 2, 270);

        for (const btn of [this.btnReiniciar, this.btnMenu]) {
            const hover = this._colisionBtn(mouseX, mouseY, btn);
            ctx.fillStyle = hover ? `rgb(${AZUL.join(',')})` : `rgb(${AZUL_OSCURO.join(',')})`;
            ctx.strokeStyle = `rgb(${NEGRO_PURO.join(',')})`;
            ctx.lineWidth = 3;
            this._roundRect(ctx, btn.x, btn.y, btn.w, btn.h, 12);
            ctx.fill();
            ctx.stroke();

            ctx.fillStyle = `rgb(${BLANCO.join(',')})`;
            ctx.font = `bold ${this.fNormalTamano}px Arial`;
            const label = btn === this.btnReiniciar ? 'Reiniciar' : 'Menu Principal';
            ctx.fillText(label, btn.x + btn.w / 2, btn.y + btn.h / 2 + this.fNormalTamano * 0.35);
        }

        ctx.font = `bold ${this.fPequenaTamano}px Arial`;
        ctx.fillStyle = `rgb(${GRIS.join(',')})`;
        ctx.fillText(CREDITOS, ANCHO / 2, ALTO - 12);
    }

    manejarClick(mouseX, mouseY) {
        if (this._colisionBtn(mouseX, mouseY, this.btnReiniciar)) return 'reiniciar';
        if (this._colisionBtn(mouseX, mouseY, this.btnMenu)) return 'menu';
        return null;
    }

    _colisionBtn(mx, my, btn) {
        return mx >= btn.x && mx <= btn.x + btn.w && my >= btn.y && my <= btn.y + btn.h;
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