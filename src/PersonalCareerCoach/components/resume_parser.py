import PyPDF2

class ResumeParser:
    def __init__(self):
        pass

    def parse_pdf(self, file):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    def extract_skills(self, text):
        # Implement skill extraction logic here
        pass

    def extract_experience(self, text):
        # Implement experience extraction logic here
        pass