from config import FAST_MODEL, MAX_RETRIES
from utils.api import call_llm
from utils.parser import parse_json_response
from rag.retriever import get_retriever

# Load retriever only once
retriever = get_retriever()


def run_agent(
    system_prompt,
    user_input,
    model=FAST_MODEL,
    temperature=0.2,
    max_tokens=900
):
    """
    Generic AI Agent with RAG support.
    """

    # Retrieve only the most relevant document
    docs = retriever.invoke(user_input)

    context = ""
    if docs:
        context = docs[0].page_content[:200]

    final_prompt = f"""
Knowledge:
{context}

Task:
{user_input}

Instructions:
- Use the knowledge only if it is relevant.
- Return ONLY valid JSON.
- Do NOT use markdown.
- Do NOT include explanations.
"""

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": final_prompt
        }
    ]

    for attempt in range(MAX_RETRIES):

        try:

            response = call_llm(
                messages=messages,
                model=model,
                temperature=temperature,
                max_tokens=max_tokens,
                show_debug=True
            )

            print("\n" + "=" * 80)
            print("RESPONSE TYPE:")
            print(type(response))
            print("=" * 80)

            print("RAW RESPONSE:")
            print(response)
            print("=" * 80)

            print("RESPONSE REPR:")
            print(repr(response))
            print("=" * 80)

            if response is None:
                raise ValueError("LLM returned no response.")

            if not isinstance(response, str):
                raise ValueError(
                    f"Expected string but got {type(response)}"
                )

            if not response.strip():
                raise ValueError("LLM returned an empty response.")

            parsed = parse_json_response(response)

            print("PARSED JSON:")
            print(parsed)
            print("=" * 80)

            return parsed

        except Exception as e:

            print("\n" + "=" * 70)
            print(f"Retry Attempt : {attempt + 1}/{MAX_RETRIES}")
            print(f"Reason        : {e}")
            print("=" * 70)

            if attempt == MAX_RETRIES - 1:
                raise