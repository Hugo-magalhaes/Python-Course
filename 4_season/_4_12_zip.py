import os
import shutil
from pathlib import Path
from zipfile import ZipFile

CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP = CAMINHO_RAIZ / 'aula_186_zip'
CAMINHO_ZIPADO = CAMINHO_RAIZ / 'aula_186.zip'
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'aula_186_descomp'

shutil.rmtree(CAMINHO_ZIP, ignore_errors=True)
Path.unlink(CAMINHO_ZIPADO, missing_ok=True)
shutil.rmtree(str(CAMINHO_ZIPADO).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

CAMINHO_ZIP.mkdir(exist_ok=True)


def cria_arquivos(qtd: int, zip_dir: Path):
    for i in range(qtd):
        texto = 'arquivo_%s' % i
        with open(zip_dir / f'{texto}.txt', 'w') as arq:
            arq.write(texto)


cria_arquivos(10, CAMINHO_ZIP)

# -- Criando o zip
with ZipFile(CAMINHO_ZIPADO, 'w') as zip:
    for roots, dirs, files in os.walk(CAMINHO_ZIP):
        for file in files:
            zip.write(os.path.join(roots, file), file)

#  ! Lendo o zip
with ZipFile(CAMINHO_ZIPADO, 'r') as zip:
    for arq in zip.namelist():
        print(arq)

#  ? Desempacotando o zip
with ZipFile(CAMINHO_ZIPADO, 'r') as zip:
    zip.extractall()
