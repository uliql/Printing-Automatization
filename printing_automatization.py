# Import libraries
from pdf_creator import odd_and_even_creator
import os, time

path = "G:\Mi unidad\Codigo\Printing Automatization\Documents to Print"
# Call the creator function with the path argument
new_pdfs = odd_and_even_creator(path)
new_odd_pdf = new_pdfs[0]
new_even_pdf = new_pdfs[1]
print('The new files were created and are ready to print')
with open(r'G:\Mi unidad\Codigo\Printing Automatization\New Format Documents\new_odd_pdf.pdf','wb') as f:
    new_odd_pdf.write(f)

with open(r'G:\Mi unidad\Codigo\Printing Automatization\New Format Documents\new_even_pdf.pdf','wb') as f:
    new_even_pdf.write(f)
input('Press enter to print the odd pages first')
os.startfile(r"G:\Mi unidad\Codigo\Printing Automatization\New Format Documents\new_odd_pdf.pdf", 'print')
print('Once the odd pages are printed, rotate 180° the pages')
input('After you have already rotated the pages, press enter to print the even pages')
os.startfile(r"G:\Mi unidad\Codigo\Printing Automatization\New Format Documents\new_even_pdf.pdf", 'print')
