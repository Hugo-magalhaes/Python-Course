class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, nome_motor):
        self._motor = nome_motor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, nome_fabricante):
        self._fabricante = nome_fabricante

    # def ficha(self):
    #     print(self.carro, self._motor,
    #           self._fabricante)
    #     return


class Motor:
    def __init__(self, nome_motor):
        self._nome_motor = nome_motor
        self.carros = []

    @property
    def nome_motor(self):
        return self._nome_motor

    def add_motor_carro(self, carro):
        if isinstance(carro, Carro):
            self.carros.append(carro)


class Fabricante:
    def __init__(self, nome_fabricante):
        self._nome_fabricante = nome_fabricante
        self.carros = []

    @property
    def nome_fabricante(self):
        return self._nome_fabricante

    def add_fabricante_carro(self, carro):
        if isinstance(carro, Carro):
            self.carros.append(carro)


c1 = Carro('Fiesta')
c1.fabricante = Fabricante('Ford')
c1.motor = Motor('1.0')
print(c1.nome, c1.fabricante.nome_fabricante, c1.motor.nome_motor)
# c1.ficha()
