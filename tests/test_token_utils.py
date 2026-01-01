import pytest

from services.token_utils import estimate_tokens


def test_estimate_tokens_with_empty_text():
    assert estimate_tokens("", "gpt-5.2") == 0


def test_estimate_tokens_fallback(monkeypatch):
    # Simulate tiktoken.encoding_for_model raising an error
    import services.token_utils as tu

    class DummyEnc:
        def encode(self, text):
            return [1] * 100

    def fake_encoding_for_model(model):
        raise KeyError("no such model")

    monkeypatch.setattr(tu, "tiktoken", type("X", (), {"encoding_for_model": fake_encoding_for_model}))

    # Fallback should use len(text)//4
    text = "a" * 1000
    assert estimate_tokens(text, "unknown-model") == len(text) // 4


def test_estimate_tokens_with_tiktoken(monkeypatch):
    # Simulate tiktoken.encoding_for_model working
    import services.token_utils as tu

    class Enc:
        def encode(self, text):
            return [0] * (len(text) // 2)

    def fake_encoding_for_model(model):
        return Enc()

    monkeypatch.setattr(tu, "tiktoken", type("X", (), {"encoding_for_model": fake_encoding_for_model}))

    text = "a" * 400
    assert estimate_tokens(text, "gpt-5.2") == len(text) // 2