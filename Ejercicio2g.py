from interpreter import draw
from chessPictures import *


torre_bl_cas_ng = square.negative().under(rock)
caballo_bl_cas_bl = square.under(knight)
alfil_bl_cas_ng = square.negative().under(bishop)
reyna_bl_cas_bl = square.under(queen)
rey_bl_cas_ng = square.negative().under(king)
alfil_bl_cas_bl = square.under(bishop)
caballo_bl_cas_ng = square.negative().under(knight)
torre_bl_cas_bl = square.under(rock)

fila1 = torre_bl_cas_ng.join(caballo_bl_cas_bl).join(alfil_bl_cas_ng).join(reyna_bl_cas_bl).join(
    rey_bl_cas_ng).join(alfil_bl_cas_bl).join(caballo_bl_cas_ng).join(torre_bl_cas_bl)


peon_bl_cas_bl = square.under(pawn)
peon_bl_cas_ng = square.negative().under(pawn)

fila2 = peon_bl_cas_bl.join(peon_bl_cas_ng).horizontalRepeat(4)


par_casillas = square.negative().join(square)
fila_casillas = par_casillas.horizontalRepeat(4)
bloque_de_casilleros = fila_casillas.negative().up(fila_casillas).verticalRepeat(2)


fila7 = fila2.negative()


fila8 = fila1.negative()


draw(fila8.up(fila7.up(bloque_de_casilleros.up(fila2.up(fila1)))))
