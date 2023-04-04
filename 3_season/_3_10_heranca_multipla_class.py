class A:
    def metodo(self):
        print('A')


class B:
    def metodo(self):
        print('B')


class C:
    def metodo(self):
        print('C')


class D(B, C):
    ...
    # def metodo(self):
    #     print('D')


print(D.metodo())
