from interpreter import draw
from chessPictures import *

cab_bl = knight
cab_ng = knight.negative()
fila = cab_bl.join(cab_ng)
draw(fila.up(fila.negative()))