import os
import cairosvg
import asyncio
from PyPDF2 import PdfFileWriter, PdfFileReader
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from svgpathtools import svg2paths2


def svg_to_pdf(svg_filename, pdf_filename):
    try:
        if not os.path.exists(os.path.dirname(pdf_filename)):
            os.makedirs(os.path.dirname(pdf_filename))
        cairosvg.svg2pdf(url=svg_filename, write_to=pdf_filename)
        print(f"PDF is ready: {pdf_filename}")
    except Exception as e:
        print(f"Error converting SVG to PDF: {e}")


def add_text_to_pdf(pdf_filename, text, x, y, font_size, font_name='Helvetica'):
    try:
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        pdfmetrics.registerFont(TTFont(font_name, f'{font_name}.ttf'))
        can.setFont(font_name, font_size)
        can.drawString(x, y, text)
        can.save()

        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        existing_pdf = PdfFileReader(open(pdf_filename, "rb"))
        output = PdfFileWriter()

        for i in range(existing_pdf.getNumPages()):
            page = existing_pdf.getPage(i)
            page.mergePage(new_pdf.getPage(0))
            output.addPage(page)

        output_stream = open(f"output_{pdf_filename}", "wb")
        output.write(output_stream)
        output_stream.close()
        print(f"Final PDF with text is ready: output_{pdf_filename}")
    except Exception as e:
        print(f"Error adding text to PDF: {e}")


def extract_and_replicate_text(svg_filename, pdf_filename):
    try:
        paths, attributes, svg_attributes = svg2paths2(svg_filename)

        for attr in attributes:
            if 'd' in attr:
                path_data = attr['d']
                print(f"Path data: {path_data}")
            if 'text' in attr:
                text_content = attr['text']
                print(f"Text content: {text_content}")

    except Exception as e:
        print(f"Error extracting and replicating text: {e}")


svg_filename = 'originals/curved_text.svg'
pdf_filename = 'output/output.pdf'

svg_to_pdf(svg_filename, pdf_filename)
extract_and_replicate_text(svg_filename, pdf_filename)
