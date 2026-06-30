import docx

def extract_text(file_path : str) -> str:

    document = docx.Document(file_path)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text