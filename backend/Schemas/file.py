from pydantic import BaseModel

class UploadedFileMetaData(BaseModel):
    original_filename : str
    stored_filename : str
    file_path : str
    extension : str

class DocumentUploadResponse(BaseModel):
    success : bool
    message : str
    filename : str | None = None
    error : str | None = None