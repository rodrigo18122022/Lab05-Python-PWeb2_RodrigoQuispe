from interpreter import draw
from chessPictures import *

par = square.join(square.negative())
fila1 = par.horizontalRepeat(4)
fila2 = fila1.negative()
draw(fila1.up(fila2).verticalRepeat(2))