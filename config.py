import os
from dotenv import load_dotenv

# Token limits and defaults for model providers
model_token_limits = {
    "OpenAI API:gpt-5.2": {"default": 128000, "max": 400000},
    "OpenAI API:gpt-5-mini": {"default": 64000, "max": 400000},
    "OpenAI API:gpt-5-nano": {"default": 64000, "max": 400000},
    "OpenAI API:gpt-5.2-pro": {"default": 128000, "max": 400000},
    "OpenAI API:gpt-5": {"default": 128000, "max": 400000},
    "OpenAI API:gpt-4.1": {"default": 128000, "max": 1000000},
    "Anthropic API:claude-sonnet-4-5-20250929": {"default": 64000, "max": 200000},
    "Anthropic API:claude-haiku-4-5-20251001": {"default": 64000, "max": 200000},
    "Anthropic API:claude-opus-4-5-20251101": {"default": 64000, "max": 200000},
    "Mistral API:mistral-large-2512": {"default": 64000, "max": 128000},
    "Mistral API:mistral-medium-2508": {"default": 64000, "max": 128000},
    "Mistral API:mistral-small-2506": {"default": 24000, "max": 32000},
    "Mistral API:ministral-14b-2512": {"default": 64000, "max": 128000},
    "Mistral API:ministral-8b-2512": {"default": 64000, "max": 128000},
    "Mistral API:magistral-medium-2509": {"default": 32000, "max": 40000},
    "Mistral API:magistral-small-2509": {"default": 32000, "max": 40000},
    "Google AI API:gemini-3-pro-preview": {"default": 200000, "max": 1000000},
    "Google AI API:gemini-3-flash-preview": {"default": 200000, "max": 1000000},
    "Google AI API:gemini-2.5-flash": {"default": 200000, "max": 1000000},
    "Google AI API:gemini-2.5-flash-lite": {"default": 200000, "max": 1000000},
    "Google AI API:gemini-2.5-pro": {"default": 200000, "max": 1000000},
    "Groq API:openai/gpt-oss-120b": {"default": 64000, "max": 128000},
    "Groq API:openai/gpt-oss-20b": {"default": 64000, "max": 128000},
    "Groq API:llama-3.3-70b-versatile": {"default": 64000, "max": 128000},
    "Groq API:llama-3.1-8b-instant": {"default": 64000, "max": 131072},
    "Groq API:deepseek-r1-distill-llama-70b": {"default": 64000, "max": 128000},
    "Groq API:moonshotai/kimi-k2-instruct": {"default": 64000, "max": 128000},
    "Groq API:qwen/qwen3-32b": {"default": 64000, "max": 128000},
    "Ollama:default": {"default": 8000, "max": 32000},
    "LM Studio Server:default": {"default": 8000, "max": 32000},
}


def load_env(session_state: dict):
    """Load environment variables into a provided session_state-like dict.

    This function intentionally does not import Streamlit so it can be
    tested in isolation. Pass `st.session_state` from the app when used.
    """
    # Load .env file if present
    if os.path.exists(".env"):
        load_dotenv(".env")

    # Map environment variables into the provided state dict if present
    mappings = {
        "GITHUB_API_KEY": "github_api_key",
        "OPENAI_API_KEY": "openai_api_key",
        "ANTHROPIC_API_KEY": "anthropic_api_key",
        "GOOGLE_API_KEY": "google_api_key",
        "MISTRAL_API_KEY": "mistral_api_key",
        "GROQ_API_KEY": "groq_api_key",
    }

    for env_name, state_key in mappings.items():
        value = os.getenv(env_name)
        if value:
            session_state[state_key] = value

    # Local endpoints with sensible defaults
    session_state.setdefault("ollama_endpoint", os.getenv("OLLAMA_ENDPOINT", "http://localhost:11434"))
    session_state.setdefault("lm_studio_endpoint", os.getenv("LM_STUDIO_ENDPOINT", "http://localhost:1234"))
