# Import libraries
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
def odd_and_even_creator(path):

    # Extracting all the contents in the directory corresponding to path
    l_files = os.listdir(path)
    # Instantiating the path of the file
    file_path = f'{path}\\{l_files[0]}'
    pdf = PdfFileReader(file_path)
    # Getting the total number of pages from the file
    # and checking if they are wether odd or even number
    pages_number = PdfFileReader.getNumPages(pdf)

    if pages_number > 1:
        #Creating lists and pdfs for even and odd numbers by separate
        odd_numbers_list = list(range(0,pages_number,2))
        even_numbers_list = list(range(1,pages_number,2))
        new_odd_pdf = PdfFileWriter()
        new_even_pdf = PdfFileWriter()

        # Odd section
        for number in odd_numbers_list:
            new_odd_pdf.addPage(pdf.getPage(number))
        
        # Even section
        for number in even_numbers_list:
            new_even_pdf.addPage(pdf.getPage(number))

        with open(r'G:\Mi unidad\Codigo\Printing Automatization\New Documents\new_odd_pdf.pdf','wb') as f:
            new_odd_pdf.write(f)

        with open(r'G:\Mi unidad\Codigo\Printing Automatization\New Documents\new_even_pdf.pdf','wb') as f:
            new_even_pdf.write(f)  

        return ('Your new pdfs were created and are ready to print')  
    
    else:
        return ('El archivo tiene una sola carilla')