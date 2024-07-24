from utils.outlook import Outlook
from utils.pdf_converter import PDFConverter
from utils.google_drive import GoogleDrive

def main():
    outlook = Outlook()
    emails = outlook.get_all_emails()
    
    pdf_converter = PDFConverter()
    pdf_emails = pdf_converter.convert_emails_to_pdfs(emails)
    
    google_drive = GoogleDrive()
    google_drive.upload_pdfs(pdf_emails)
    
if __name__ == "__main__":
    main()
