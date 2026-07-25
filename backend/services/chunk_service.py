from backend.schemas.chunk import Chunk

def create_chunks(text : str, document_id = str, chunk_size : int = 500, overlap : int = 100) ->list[Chunk]:
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("Overlap value is invalid")
    
    text = text.strip()

    if not text:
        return []
    
    chunks = []
    start = 0
    step = chunk_size - overlap

    while start < len(text):
        current_chunk = Chunk(
            chunk_id = f"{document_id.stored_filename}_chunk_{len(chunks)}",
            text = text[start:start+chunk_size]
        )
        chunks.append(current_chunk)
        start += step

    return chunks