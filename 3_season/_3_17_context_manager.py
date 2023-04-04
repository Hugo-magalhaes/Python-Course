class MyContextManager:
    def __init__(self, path_, mode_) -> None:
        self.path_ = path_
        self.mode_ = mode_
        self._arquivo = None

    def __enter__(self):
        print('Enter')
        self._arquivo = open(self.path_, self.mode_, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('Exit')
        self._arquivo.close()

        # raise class_exception('Ta cagado') #recria a exceção

        print(class_exception)
        print(exception_)
        print(traceback_)
        # exception_.add_note('Acrescenta nota')
        return True  # Cancela qualquer exceção do with


inst = MyContextManager('teste.txt', 'w')
with inst as algo:
    algo.write('algo', 123)
