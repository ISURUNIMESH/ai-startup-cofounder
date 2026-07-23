from utils.api import call_openrouter
from config import FAST_MODEL

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    },
    {
        "role": "user",
        "content": "Say hello in one sentence."
    }
]

response = call_openrouter(
    messages=messages,
    model=FAST_MODEL,
    show_debug=True
)

print("\nAI Response:\n")
print(response)