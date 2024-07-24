import win32com.client

class Outlook:
    def __init__(self):
        self.outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        self.inbox = self.outlook.GetDefaultFolder(6)  # 6 refers to the inbox
    
    def get_all_emails(self):
        emails = []
        for message in self.inbox.Items:
            email_data = {
                'subject': message.Subject,
                'body': message.Body,
                'attachments': self.save_attachments(message.Attachments)
            }
            emails.append(email_data)
        return emails
    
    def save_attachments(self, attachments):
        attachment_files = []
        for attachment in attachments:
            file_path = f"attachments/{attachment.FileName}"
            attachment.SaveAsFile(file_path)
            attachment_files.append(file_path)
        return attachment_files
