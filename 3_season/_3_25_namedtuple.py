#  Namedtuples é uma forma de utilizar tuplas imutáveis para criar um dado
# ou base
# Namedtuples é só para dados, sem métodos

from collections import namedtuple
from typing import NamedTuple

Carta = namedtuple('Carta', ['valor', 'naipe'])

as_espadas = Carta('A', 'espadas')

print(as_espadas._fields)
print(as_espadas._field_defaults)
print(as_espadas._asdict())


class Carta1(NamedTuple):
    valor: str = 'Valor'
    naipe: str = 'Naipe'


as_espadas1 = Carta1('A', 'espadas')

print(as_espadas1._fields)
print(as_espadas1._field_defaults)
print(as_espadas1._asdict())
