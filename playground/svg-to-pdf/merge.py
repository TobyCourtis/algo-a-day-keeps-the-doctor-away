from PyPDF2 import PdfReader, PdfWriter


def overlay_pdfs(top_pdf_path, bottom_pdf_path, output_pdf_path):
    # Open the top PDF (FOO at the top)
    with open(top_pdf_path, 'rb') as top_file:
        top_pdf = PdfReader(top_file)
        top_page = top_pdf.pages[0]  # Assuming there's only one page in top PDF

        # Open the bottom PDF (BAR at the bottom)
        with open(bottom_pdf_path, 'rb') as bottom_file:
            bottom_pdf = PdfReader(bottom_file)
            bottom_page = bottom_pdf.pages[0]  # Assuming there's only one page in bottom PDF

            # Create a new PDF writer
            output_pdf = PdfWriter()

            # Overlay the pages: Place bottom page first, then top page
            bottom_page.merge_page(top_page)

            # Add the merged page to the output PDF
            output_pdf.add_page(bottom_page)

            # Write the output PDF to a file
            with open(output_pdf_path, 'wb') as out_file:
                output_pdf.write(out_file)

    print(f"Overlay PDF saved to '{output_pdf_path}'")


# Example usage:
overlay_pdfs('text.pdf', 'image.pdf', 'overlayed_output.pdf')
