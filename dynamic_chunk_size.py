def split_text_into_token_chunks(text, max_chunk_size=2000):
    """
    Split text into chunks based on token size to manage token limits.
    """
    words = text.split()
    current_chunk = []
    current_tokens = 0

    for word in words:
        word_token_count = len(word)  # estimate token count; you may refine with tiktoken if needed
        if current_tokens + word_token_count > max_chunk_size:
            yield ' '.join(current_chunk)
            current_chunk = []
            current_tokens = 0

        current_chunk.append(word)
        current_tokens += word_token_count

    # yield the last chunk if it exists
    if current_chunk:
        yield ' '.join(current_chunk)
