# Dunder/Special/Magic Methods
# -- __new__ é o que cria o objeto antes do __init__
class Ponto:
    def __init__(self, x, y, z='z') -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:  # Objeto string quando o objeto é chamado
        return f'({self.x}, {self.y}, {self.z})'

    def __repr__(self) -> str:  # Objeto montado de desenvolvedor
        # class_name = self.__class__.__name__
        class_name = type(self).__name__  # Idênticos
        return f'{class_name} (x = {self.x!r}, y = {self.y!r}, z = {self.z!r})'

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __lt__(self, other):
        ponto1 = self.x + self.y
        ponto2 = other.x + other.y
        return ponto1 < ponto2

    def __gt__(self, other):
        ponto1 = self.x + self.y
        ponto2 = other.x + other.y
        return ponto1 > ponto2


#! O !r faz com que o print represente a forma real do objeto


ap = Ponto(1, 2)
ap1 = Ponto(1, 3)
print(ap < ap1)
print(repr(ap))  # E o repr é fall back se o str não existir
print(ap)  # Observe que o str é primeira estância
