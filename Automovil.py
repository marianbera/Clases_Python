class Automovil:
    ruedas = 4
    def __init__(self,color,marca,aceleracion,velocidad):
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad

    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion
        return self.velocidad

    def frena(self):
        self.velocidad = self.velocidad - self.aceleracion
        return self.velocidad