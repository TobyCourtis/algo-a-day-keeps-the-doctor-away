import asyncio
from pyppeteer import launch


async def render_pdf(svg_content, pdf_filename):
    browser = await launch(headless=True)
    page = await browser.newPage()

    await page.setContent(svg_content)

    await asyncio.sleep(2)

    await page.pdf({
        'path': pdf_filename,
        'format': 'A4'
    })

    await browser.close()
    print(f"PDF is ready for '{pdf_filename}'")


def output_pdf(svg_filename, pdf_filename):
    with open(svg_filename, 'r') as svg_file:
        svg_content = svg_file.read()

    asyncio.get_event_loop().run_until_complete(render_pdf(svg_content, pdf_filename))


filenames = [
    "originals/curved_text.svg",
    "originals/element_clipping.svg",
    "originals/images.svg",
    "originals/text_effects.svg",
    "originals/view_mask.svg",
]

for name in filenames:
    svg_filename = name
    pdf_filename = f"./output/{name.split('/')[-1].split('.')[0]}.pdf"
    output_pdf(svg_filename, pdf_filename)
