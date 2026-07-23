from config import LLM_PROVIDER
from utils.openrouter import call_openrouter
from utils.groq_api import call_groq


def call_llm(
    messages,
    model,
    temperature=0.3,
    max_tokens=900,
    show_debug=False
):
    """
    Call the configured LLM provider.
    """

    provider = LLM_PROVIDER.lower()

    if show_debug:
        print("=" * 60)
        print(f"Provider : {provider}")
        print(f"Model    : {model}")
        print("=" * 60)

    try:

        if provider == "openrouter":
            return call_openrouter(
                messages=messages,
                model=model,
                temperature=temperature,
                max_tokens=max_tokens,
                show_debug=show_debug,
            )

        elif provider == "groq":
            return call_groq(
                messages=messages,
                model=model,
                temperature=temperature,
                max_tokens=max_tokens,
                show_debug=show_debug,
            )

        else:
            raise ValueError(
                f"Unsupported LLM provider: {LLM_PROVIDER}"
            )

    except Exception as e:
        raise Exception(f"LLM Provider Error: {e}")