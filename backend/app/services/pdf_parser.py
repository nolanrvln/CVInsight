import pdfplumber

def test_pdf_extraction(pdf_path):
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # General information about the PDF
        print(f"Number of pages: {len(pdf.pages)}")

        # Extraction page by page
        for i, page in enumerate(pdf.pages):
            print(f"\n--- Page {i + 1} ---")
            text = page.extract_text()
            print(text if text else "No text found on this page.")

            # Bonus: See structure of the page
            print(f"Layout information: {len(page.extract_table())} tables found.")

if __name__ == "__main__":
    # Test the PDF extraction with a sample PDF file
    test_pdf_extraction("../../../docs/sample.pdf")