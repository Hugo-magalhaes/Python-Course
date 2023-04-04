# Abstração
#  Nome desse arquivo : Template Method
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    # Esse erro define que a superclasse não deveria ser usada
    def _log(self, msg):
        raise NotImplementedError(
            'Implemnete o método Log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print(f'Salvando na Log:  {msg_formatada}')

        with open(LOG_FILE, 'a', encoding='utf8') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')
            arquivo.write('\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    # l = Log()
    # l._log('qualquer coisa')
    lf = LogFileMixin()
    lf.log_error('Qualquer coisa')
    lf.log_success('Qualquer coisa')
    li = LogPrintMixin()
    li.log_error('Qualquer coisa')
    li.log_success('Que Legal')
