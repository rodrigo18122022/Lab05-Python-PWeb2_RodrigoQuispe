from colors import *


class Picture:
    def __init__(self, img):
        self.img = img

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        if color not in inverter:
            return color
        return inverter[color]

    def verticalMirror(self):
        """ Devuelve el espejo vertical de la imagen """
        vertical = []
        for value in self.img:
            vertical.append(value[::-1])
        return Picture(vertical)

    def horizontalMirror(self):
        """ Devuelve el espejo horizontal de la imagen """
        horizontal = list(reversed(self.img))
        return Picture(horizontal)

    def negative(self):
        """ Devuelve un negativo de la imagen """
        negative = []
        for line in self.img:
            linea_invertida = ""
            for char in line:
                linea_invertida += self._invColor(char)
            negative.append(linea_invertida)
        return Picture(negative)

    def join(self, p):
        """ Devuelve una nueva figura poniendo la figura del argumento 
            al lado derecho de la figura actual """
        joined = []
        for line1, line2 in zip(self.img, p.img):
            joined.append(line1 + line2)
        return Picture(joined)

    def up(self, p):
        combinada = self.img + p.img
        return Picture(combinada)

    def under(self, p):
        """ Devuelve una nueva figura poniendo la figura p sobre la
            figura actual """
        combinada = []
        for line1, line2 in zip(p.img, self.img):
            linea_combinada = ''
            for c1, c2 in zip(line1, line2):
                linea_combinada += c1 if c1 != ' ' else c2
            combinada.append(linea_combinada)
        return Picture(combinada)

    def horizontalRepeat(self, n):
        """ Devuelve una nueva figura repitiendo la figura actual al costado
            la cantidad de veces que indique el valor de n """
        imagen_repetida = []
        for linea in self.img:
            linea_repetida = linea * n
            imagen_repetida.append(linea_repetida)
        return Picture(imagen_repetida)

    def verticalRepeat(self, n):
        imagen_repetidav = self.img * n
        return Picture(imagen_repetidav)

    # Extra: Sólo para realmente viciosos
    def rotate(self):
        """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
        o antihorario"""

        # En sentido Horario
        transpuesta = []
        for i in range(len(self.img[0])):
            new_fila = []
            for j in range(len(self.img)):
                new_fila.append(self.img[j][i])
            transpuesta.append(new_fila)

        rotada = []
        for row in transpuesta:
            rotada.append(''.join(row[::-1]))

        return Picture(rotada)
