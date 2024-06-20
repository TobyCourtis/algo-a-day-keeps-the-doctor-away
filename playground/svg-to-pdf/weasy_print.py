from weasyprint import HTML, CSS

# Read the SVG content


# Define the CSS to set the page size
css = CSS(string='''
    @page {
        size: 445.5mm 315mm;
        margin: 0;
    }
    body, html {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
    }
''')


def output_pdf(filename):
    with open(f"originals/{filename}", 'r') as file:
        svg_content = file.read()

    # Set the HTML content with the SVG
    html_content = f"""
        {svg_content}
    """

    # Generate the PDF with the specified CSS
    HTML(filename=f"originals/{filename}").write_pdf(f"./output/{filename.split('.')[0]}.pdf")
    # HTML(string=html_content).write_pdf(f"./output/{filename.split('.')[0]}.pdf", stylesheets=[css])

    print(f'PDF for {filename} is ready.')


filenames = [
    "curved_text.svg",
    "element_clipping.svg",
    "images.svg",
    "text_effects.svg",
    "view_mask.svg",
]

for name in filenames:
    output_pdf(name)
