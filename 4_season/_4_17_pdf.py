from pathlib import Path

from PyPDF2 import PdfMerger, PdfReader, PdfWriter

RAIZ = Path(__file__).parent
RELATORIO = RAIZ/'R20230210.pdf'

reader = PdfReader(RELATORIO)

print(len(reader.pages))

# for page in reader.pages:
#     print(page)

page0 = reader.pages[0]

# - Capta o texto do pdf

print(page0.extract_text())
print(page0.images)

imagem0 = page0.images[0]

# - Obtém imagens do pdf

# with open(RAIZ/imagem0.name, 'wb') as imagem:
#     imagem.write(imagem0.data)

writer = PdfWriter()
# writer.add_page(page0)

# - Cria um pdf com uma página do pdf original

# with open(RAIZ/'PAGE0.pdf', 'wb') as pdf:
#     writer.write(pdf)


# - Cria um pdf com todas as páginas do pdf original

# writer = PdfWriter()
# with open(RAIZ/'NOVO_PDF.pdf', 'wb') as pdf:
#     for page in reader.pages:
#         writer.add_page(page)
#     writer.write(pdf)

# - Cria dois pdf com cada a página do pdf original

# for i, page in enumerate(reader.pages):
#     writer = PdfWriter()
#     with open(RAIZ/f'page{i}.pdf', 'wb') as pdf:
#         writer.add_page(page)
#         writer.write(pdf)

# - Junta os pdfs

merger = PdfMerger()

# files = [
#     RAIZ/'page0.pdf',
#     RAIZ/'page1.pdf',
# ]

# for file in files:
#     merger.append(file)

# merger.write(RAIZ / 'merged.pdf')
# merger.close()
