"""Token utilities: estimate token counts for strings for different models."""

try:
    import tiktoken
except Exception:
    tiktoken = None


def estimate_tokens(text: str, model: str = "gpt-5.2") -> int:
    """
    Estimate the number of tokens in a text string.
    Uses tiktoken for OpenAI models, or falls back to a character-based approximation.

    Args:
        text: The text to estimate tokens for
        model: The model to use for estimation (default: gpt-5.2)

    Returns:
        Estimated token count
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
