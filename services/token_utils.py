"""Token utilities: estimate token counts for strings for different models."""

try:
    import tiktoken
except Exception:
    tiktoken = None


def estimate_tokens(text: str, model: str = "gpt-5.2") -> int:
    """Estimate tokens for `text` for a given model.

    Uses `tiktoken.encoding_for_model` when available, otherwise falls back
    to a conservative character-based heuristic.
    """
    if not text:
        return 0

    try:
        if tiktoken is not None:
            enc = tiktoken.encoding_for_model(model)
            return len(enc.encode(text))
    except Exception:
        # Fall through to fallback heuristic
        pass

    # Conservative fallback (English-like density)
    return len(text) // 4
