import fitz
import os
from pathlib import Path
#necessario para utilização do script.
#pip install PyMuPDF

#necessario para utilização do script
#pip pyPdf 

path = r"{}".format(Path().absolute()) #Mudar para o caminho da sua pasta
pdflist = os.listdir(path)


print("##############################################")
print("#####Developer By: @V4anderson 16/08/2021#####")
print("##############################################")
print("")
print("")
qtd = 9999
for x in range(int(qtd)):
    pagina=x #Escolher a página do documento


    for pdf in pdflist:
        if pdf.endswith(".pdf"):
            doc = fitz.open(pdf)
            page = doc.loadPage(pagina-1)
            matriz = fitz.Matrix(4, 4)
            pix = page.getPixmap(matrix=matriz)
            output = "Documento{0}.jpg".format(x)
            print(output)
            pix.writePNG(output)
