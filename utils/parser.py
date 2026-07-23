import json
import re


def parse_json_response(text):
    """
    Clean and parse JSON responses returned by LLMs.
    """

    if text is None:
        raise ValueError("LLM returned an empty response.")

    text = text.strip()

    if not text:
        raise ValueError("LLM returned a blank response.")

    # Remove Markdown code blocks
    text = re.sub(r"^```json\s*", "", text)
    text = re.sub(r"^```\s*", "", text)
    text = re.sub(r"\s*```$", "", text)

    text = text.strip()

    # Extract only the JSON object
    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1:
        raise ValueError("No valid JSON object found in the response.")

    text = text[start:end + 1]

    try:
        return json.loads(text)

    except json.JSONDecodeError as e:
        print("\n========== INVALID JSON ==========\n")
        print(text)
        print("\n==================================\n")

        raise ValueError(
            f"Invalid JSON returned by LLM: {e}"
        ) from e