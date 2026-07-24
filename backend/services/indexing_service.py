from backend.schemas.file import UploadedFileMetaData
from backend.schemas.IndexingResult import IndexingResult
from backend.services.processors.document_processor import process_document
from backend.services.chunk_service import create_chunks
from backend.services.embedding_service import generate_embeddings
from backend.services.chroma_service import store_embeddings

def index_document(uploaded_file : UploadedFileMetaData) -> IndexingResult:
    document = process_document(uploaded_file.file_path)

    return IndexingResult(
        success = True,
        message = "Document extracted successfully",
        chunks_created = 0,
        embeddings_stored = 0
    )