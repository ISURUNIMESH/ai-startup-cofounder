import requests

from config import (
    GROQ_API_KEY,
    GROQ_URL,
    GROQ_MODEL,
    REQUEST_TIMEOUT
)


def call_groq(
    messages,
    model=None,
    temperature=0.3,
    max_tokens=900,
    show_debug=False
):
    """
    Send a request to Groq.
    """

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model or GROQ_MODEL,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }

    try:
        response = requests.post(
            GROQ_URL,
            headers=headers,
            json=payload,
            timeout=REQUEST_TIMEOUT
        )

        if show_debug:
            print("=" * 70)
            print("STATUS :", response.status_code)
            print("=" * 70)
            print(response.text)

        response.raise_for_status()

        result = response.json()

        return result["choices"][0]["message"]["content"]

    except requests.exceptions.Timeout:
        raise Exception("Groq request timed out.")

    except requests.exceptions.ConnectionError:
        raise Exception("Unable to connect to Groq.")

    except requests.exceptions.HTTPError:
        raise Exception(
            f"Groq HTTP Error {response.status_code}: {response.text}"
        )

    except requests.exceptions.RequestException as e:
        raise Exception(f"Groq Request Error: {e}")

    except KeyError:
        raise Exception("Invalid response received from Groq.")

    except Exception as e:
        raise Exception(f"Unexpected Groq Error: {e}")