import asyncio
from pyppeteer import launch
from PyPDF2 import PdfReader, PdfWriter

width = 10
height = 10

async def render_pdf(svg_content, pdf_filename):
    browser = await launch(headless=True)
    page = await browser.newPage()

    await page.setContent(svg_content)

    await asyncio.sleep(2)

    # Convert mm to inches (1 mm = 0.0393701 inches)
    # width_inches = width_mm * 0.0393701
    # height_inches = height_mm * 0.0393701

    await page.pdf({
        'path': pdf_filename,
        'width': f'{width}in',
        'height': f'{height}in'
    })

    await browser.close()
    print(f"PDF is ready for '{pdf_filename}'")



async def output_pdf(svg_filename, pdf_filename):
    with open(svg_filename, 'r') as svg_file:
        svg_content = svg_file.read()

    await render_pdf(svg_content, pdf_filename)


import cairosvg

def convert_svg_to_pdf(svg_file, output_pdf):
    dpi = 72
    cairosvg.svg2pdf(url=svg_file,
                     write_to=output_pdf,
                     output_width=width * dpi,  # Convert inches to points (1 inch = 72 points)
                     output_height=height * dpi,
                     dpi=dpi)





async def main():
    # Step 1: Convert text-heavy SVG to PDF using CairoSVG
    convert_svg_to_pdf('./originals/text_effects.svg', 'text.pdf')

    # Step 2: Render complex/dynamic images with Pyppeteer
    await output_pdf("originals/text_effects.svg", 'image.pdf')
    # await render_image_with_pyppeteer('https://example.com/dynamic-content', 'image.png')
    # You can convert the rendered image.png to PDF if needed

    # Step 3: Combine PDFs into a single page
    output_pdf_path = 'combined.pdf'

    writer = PdfWriter()

    # Add page 0 of text.pdf
    with open('text.pdf', 'rb') as text_pdf:
        reader = PdfReader(text_pdf)
        page = reader.pages[0]
        writer.add_page(page)

    # Add page 0 of image.pdf
    with open('image.pdf', 'rb') as image_pdf:
        reader = PdfReader(image_pdf)
        page = reader.pages[0]
        writer.add_page(page)

    with open(output_pdf_path, 'wb') as out_pdf:
        writer.write(out_pdf)

    print(f"Combined PDF is ready at '{output_pdf_path}'")


# Run the asyncio event loop to execute the async functions
asyncio.run(main())
