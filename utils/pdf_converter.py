from fpdf import FPDF

class PDFConverter:
    def convert_emails_to_pdfs(self, emails):
        pdf_files = []
        for email in emails:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size = 12)
            pdf.multi_cell(0, 10, email['body'])
            pdf_file = f"pdfs/{email['subject']}.pdf"
            pdf.output(pdf_file)
            pdf_files.append(pdf_file)
        return pdf_files
