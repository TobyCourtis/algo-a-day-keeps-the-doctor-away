import asyncio
import pdfkit
from pyppeteer import launch

async def render_pdf(svg_content, pdf_filename, icc_profile_path=None):
    browser = await launch(headless=True)
    page = await browser.newPage()

    await page.setContent(svg_content)

    await asyncio.sleep(2)

    pdf_options = {
        'path': pdf_filename,
        'format': 'A4',
        'printBackground': True,
        'preferCSSPageSize': True,
        'colorMode': 'cmyk',
        'margin': {
            'top': '0.5cm',
            'right': '0.5cm',
            'bottom': '0.5cm',
            'left': '0.5cm'
        }
    }

    if icc_profile_path:
        pdf_options['colorProfile'] = icc_profile_path

    await page.pdf(pdf_options)

    await browser.close()
    print(f"PDF is ready for '{pdf_filename}'")

def output_pdf(svg_filename, pdf_filename, icc_profile_path=None):
    with open(svg_filename, 'r') as svg_file:
        svg_content = svg_file.read()

    asyncio.get_event_loop().run_until_complete(render_pdf(svg_content, pdf_filename, icc_profile_path))

filenames = [
    "originals/curved_text.svg",
    "originals/element_clipping.svg",
    "originals/images.svg",
    "originals/text_effects.svg",
    "originals/view_mask.svg",
]

icc_profile_path = "path/to/your/icc_profile.icc"

for name in filenames:
    svg_filename = name
    pdf_filename = f"./output/{name.split('/')[-1].split('.')[0]}.pdf"
    output_pdf(svg_filename, pdf_filename, icc_profile_path)
