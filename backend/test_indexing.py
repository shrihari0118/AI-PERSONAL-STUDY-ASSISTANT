from backend.services.indexing_service import index_document
from backend.schemas.file import UploadedFileMetaData

uploaded_file = UploadedFileMetaData(
    original_filename="Shri harihara suthan Resume (1).pdf",
    stored_filename="b0a09b5e-2131-4790-9691-2cdd7a7d147d.pdf",
    file_path="backend/uploads/b0a09b5e-2131-4790-9691-2cdd7a7d147d.pdf",
    extension=".pdf"
)

result = index_document(uploaded_file)

print(result)