class Motor:
    def __init__(self):
        self.numeroCilindros = None
        self.tipo = None
        self.registro = None

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo


class Auto:
    def __init__(self):
        self.modelo = None
        self.precio = None
        self.asientos = []
        self.marca = None
        self.motor = None
        self.registro = None
        self.cantidadCreados = 0

    def cantidadAsientos(self):
        numAsientos = 0
        for i in range(len(self.asientos)):
            if self.asientos[i] != None:
                numAsientos += 1
        return numAsientos

    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for i in range(len(self.asientos)):
                if self.asientos[i] != None:
                    if self.asientos[i].registro != self.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"


class Asiento:
    def __init__(self):
        self.color = None
        self.precio = None
        self.registro = None

    def cambiarColor(self, color):
        if color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco":
            self.color = color
