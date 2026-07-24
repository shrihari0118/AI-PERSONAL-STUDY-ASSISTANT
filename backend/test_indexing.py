from backend.services.indexing_service import index_document
from backend.schemas.file import UploadedFileMetaData

uploaded_file = UploadedFileMetaData(
    original_filename="sample.pdf",
    stored_filename="sample.pdf",
    file_path="backend/uploads/sample.pdf",
    extension=".pdf"
)

result = index_document(uploaded_file)

print(result)