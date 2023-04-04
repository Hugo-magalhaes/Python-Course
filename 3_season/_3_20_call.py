#  callable signifca poder chamar com os parantêses

class MyCall:
    def __init__(self, phone) -> None:
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'esta chamado', self.phone)
