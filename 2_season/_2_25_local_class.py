global valor  # Agora uma global vale para todos


def asda(valor):
    valor_f = valor  # Variavel local vale só aqui

    def asdae(vv):
        nonlocal valor_f  # agora uma variável não local vale aqui agora também
        vv += valor_f
        return vv
    return valor
