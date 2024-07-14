import PyPDF2

from base_utils import base_utils

def pdf_to_text(pdf_path) : 

    pdf = PyPDF2.PdfReader(pdf_path)

    text = '\n'.join([
        pdf.pages[page_number].extract_text()
        for page_number 
        in range(len(pdf.pages))
    ])

    return text

def extract_toc(text) : 

    table_of_contents = [
        line 
        for line 
        in text.split('\n')
        if base_utils.is_toc(line)
    ]

    return table_of_contents