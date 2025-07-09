import pdfkit
import os

def generate_pdf_from_html(html_path, output_path):
    wkhtmltopdf_path = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

    config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

    options = {
        'enable-local-file-access': None,  
        'encoding': "UTF-8",
        'quiet': '', 
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'margin-right': '0.75in',
    }

    try:
        pdfkit.from_file(html_path, output_path, configuration=config, options=options)
        print("PDF generation successful.")
    except OSError as e:
        print("Error during PDF generation:", e)
