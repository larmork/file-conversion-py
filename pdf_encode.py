from PyPDF2 import PdfFileWriter, PdfFileReader
from getpass import getpass

pdfwriter = PdfFileWriter()
pdf = PdfFileRader(input("PDF file name: "))

for page in range(pdf.numPages):
    pdfwriter.add_page(pdf.page[page])

password = getpass(prompt='enter passcode: ')
pdfwriter.encrypt(password)

with open('protected.pdf', 'wb') as file:
    pdfwriter.write(file)