from pydantic import BaseModel


class ExtractedDocument(BaseModel):
    original_filename : str
    stored_filename : str
    file_path : str
    extension : str
    extracted_text : str