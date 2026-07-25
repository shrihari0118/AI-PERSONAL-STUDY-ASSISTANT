from backend.schemas.file import UploadedFileMetaData
from backend.schemas.IndexingResult import IndexingResult
from backend.services.processors.document_processor import process_document
from backend.services.chunk_service import create_chunks
from backend.services.embedding_service import generate_embeddings
from backend.services.chroma_service import store_embeddings

def index_document(uploaded_file : UploadedFileMetaData) -> IndexingResult:
    document = process_document(uploaded_file)
    chunks = create_chunks(
        text = document.extracted_text,
        document_id = document.stored_filename
    )
    embedded_chunks = generate_embeddings(chunks)
    store_embeddings(embedded_chunks)

    return IndexingResult(
        success = True,
        message = "Document indexed successfully",
        chunks_created = len(chunks),
        embeddings_stored = len(embedded_chunks)
    )