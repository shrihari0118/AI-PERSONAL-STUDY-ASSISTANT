from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from pathlib import Path
from services.file_service import save_uploaded_file
from Schemas.file import DocumentUploadResponse

router = APIRouter()

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt",
    ".heic",
    ".png",
    ".jpg",
    ".jpeg",
    ".xlsx",
    ".xls"
}


@router.post("/documents/upload", response_model = DocumentUploadResponse)
async def upload_document(file : UploadFile = File(...)):
    
    if not file.filename :
        return JSONResponse(
            status_code = 400,
            content = {
                "success" : False,
                "message" : "File upload failed",
                "filename" : None,
                "error" : "File is missing"
            }
        )
    file_extension = Path(file.filename).suffix.lower()

    if file_extension not in ALLOWED_EXTENSIONS:
        return JSONResponse(
            status_code = 400,
            content = {
                "success" : False,
                "message" : "File upload failed",
                "filename" : None,
                "error" : "Unsupported file type"
            }
        )
    
    saved_file = await save_uploaded_file(file)

    return DocumentUploadResponse(
        success=True,
        message="File validated successfully",
        filename=file.filename,
        error=None
    )