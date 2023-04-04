from threading import Lock, Thread
from time import sleep


# / Executa indepente do main thread
# - Esse código que roda na main thread
class Meuthread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        self.lock = Lock()

        super().__init__()

# ! Isso bloqueia o método por dentro, permitindo uma execução por vez
        def run(self):
            self.lock.acquire()
            sleep(self.texto)
            print(self.tempo)
            self.lock.release()


meu = Meuthread('Thread 1 ', 2)
meu.start()


def dorme(self):
    sleep(self.texto)
    print(self.tempo)


t = Thread(target=dorme, args=('Ola', 14))
t.start()
