import re
import fitz  # PyMuPDF
from docx import Document



def detect_file_type(file):
    """
    Detect the file type based on the uploaded file's name.
    """
    filename = file.name.lower()
    if filename.endswith('.pdf'):
        return 'pdf'
    elif filename.endswith('.docx'):
        return 'docx'
    elif filename.endswith('.txt'):
        return 'txt'
    else:
        raise ValueError("Unsupported file type. Please upload a .pdf, .docx, or .txt file.")


def parse_pdf(file):
    """
    Parse PDF file-like object using PyMuPDF (fitz)
    """
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def parse_docx(file):
    """
    Parse a DOCX file-like object and extract text.
    """
    doc = Document(file)
    text = '\n'.join([para.text for para in doc.paragraphs])
    return text


def parse_txt(file):
    """
    Parse a TXT file-like object and extract text.
    """
    return file.read().decode('utf-8')


def clean_text(text):
    """
    Clean the extracted text by removing extra spaces and newlines.
    """
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def parse_resume(file):
    """
    Parse a resume file-like object (from Streamlit) and return clean text.
    """
    file_type = detect_file_type(file)

    if file_type == 'pdf':
        text = parse_pdf(file)
    elif file_type == 'docx':
        text = parse_docx(file)
    elif file_type == 'txt':
        text = parse_txt(file)
    else:
        raise ValueError("Unsupported file type.")

    return clean_text(text)
