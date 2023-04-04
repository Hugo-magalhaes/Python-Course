from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, msg) -> None:  # Type anottations or type hints
        self.msg = msg

    @abstractmethod  # A assinatura do método enviar é diferente
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self):  # Diferente desse aqui
        print(f'Email enviando... {self.msg}')
#  Porque aqui não retorna booleano nem nada = None


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:  # Aqui a assinatura esta igual
        print(f'SMS enviando... {self.msg}')
        return True  # E retorna algo -> bool


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    if notificacao_enviada:
        print('enviada', notificacao_enviada)
    else:
        print('não enviada', notificacao_enviada)


ns = NotificacaoEmail('testando')
notificar(ns)
n = NotificacaoSMS('testando')
notificar(n)
