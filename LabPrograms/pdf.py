from PyPDF2 import PdfWriter, PdfReader

num = int(input("enter the pages to combine:"))

pdf1 = open('pdf1.pdf', 'rb')
pdf2 = open('pdf2.pdf', 'rb')

writer = PdfWriter()

pdfReader = PdfReader(pdf1)
page = pdfReader.pages[num - 1]
writer.add_page(page)

pdfReader = PdfReader(pdf2)
page = pdfReader.pages[num-1]
writer.add_page(page)

with open('output.pdf', 'wb') as output:
    writer.write(output)
