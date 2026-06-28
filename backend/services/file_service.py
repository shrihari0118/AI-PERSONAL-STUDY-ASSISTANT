from pathlib import Path
from uuid import uuid4
from fastapi import UploadFile
from Schemas.file import UploadedFileMetaData

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOADS_DIR = BASE_DIR/"uploads"

async def save_uploaded_file(file:UploadFile) -> UploadedFileMetaData:

    UPLOADS_DIR.mkdir(parents=True, exist_ok = True)

    original_filename = file.filename or "uploaded_file"
    file_extension = Path(original_filename).suffix.lower()

    unique_filename = f"{uuid4()}{file_extension}"
    file_path = UPLOADS_DIR / unique_filename

    file_content = await file.read()

    with open(file_path, "wb") as saved_file:
        saved_file.write(file_content)

    return UploadedFileMetaData(
        original_filename = original_filename,
        stored_filename = unique_filename,
        file_path = str(file_path),
        extension = file_extension
    )