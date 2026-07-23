import requests

from config import (
    OPENROUTER_API_KEY,
    OPENROUTER_URL,
    PROJECT_NAME,
    REQUEST_TIMEOUT
)


def call_openrouter(
    messages,
    model,
    temperature=0.3,
    max_tokens=900,
    show_debug=False
):

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://localhost",
        "X-Title": PROJECT_NAME
    }

    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }

    try:

        response = requests.post(
            OPENROUTER_URL,
            headers=headers,
            json=payload,
            timeout=REQUEST_TIMEOUT
        )

        if show_debug:
            print("=" * 80)
            print("STATUS :", response.status_code)
            print("=" * 80)
            print(response.text)

        response.raise_for_status()

        result = response.json()

        if show_debug:
            print("=" * 80)
            print("JSON RESPONSE")
            print(result)
            print("=" * 80)

        if "choices" not in result:
            raise Exception(f"No 'choices' field found.\n{result}")

        if len(result["choices"]) == 0:
            raise Exception("Choices array is empty.")

        message = result["choices"][0].get("message")

        if message is None:
            raise Exception(f"No message found.\n{result}")

        content = message.get("content")

        if content is None:
            raise Exception(f"No content found.\n{result}")

        return content

    except requests.exceptions.Timeout:
        raise Exception("OpenRouter request timed out.")

    except requests.exceptions.ConnectionError:
        raise Exception("Unable to connect to OpenRouter.")

    except requests.exceptions.HTTPError:
        raise Exception(
            f"OpenRouter HTTP Error {response.status_code}: {response.text}"
        )

    except Exception:
        raise