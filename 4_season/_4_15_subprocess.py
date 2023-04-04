import subprocess
import sys

print(sys.platform)
cmd = ['ping', '127.0.0.1']

# - Comando de pc no jupyter começam com !
# - Comando %%timeit no jupyter contabiliza o tempo de processo
# Se shell = True envie os args em uma string só
#  E não como uma lista
proc = subprocess.run(
    cmd,
    text=True,
    encoding='cp850'
)


proc.args
proc.returncode
proc.stderr
print(proc.stdout)
