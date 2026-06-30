from backend.schemas.document import ExtractedDocument
from backend.schemas.file import UploadedFileMetaData

from backend.services.processors.txt_processor import extract_text as extract_txt_text
from backend.services.processors.pdf_processor import extract_text as extract_pdf_text
from backend.services.processors.docx_processor import extract_text as extract_docx_text


def process_document(file_metadata : UploadedFileMetaData) -> ExtractedDocument:
    PROCESSORS = {
        ".txt" : extract_txt_text,
        ".pdf" : extract_pdf_text,
        ".docx" : extract_docx_text
    }

    processor = PROCESSORS.get(file_metadata.extension)

    if processor is None:
        raise ValueError(
            f"Unsupported file type: {file_metadata.extension}"
        )
    
    text = processor(file_metadata.file_path)

    return ExtractedDocument(
        original_filename = file_metadata.original_filename,
        stored_filename = file_metadata.stored_filename,
        file_path = file_metadata.file_path,
        extension = file_metadata.extension,
        extracted_text = text
    )