# ==============================================================================
# PROJECT CONFIGURATION
# ==============================================================================

import os
from dotenv import load_dotenv

load_dotenv()

# ==============================================================================
# PROJECT INFORMATION
# ==============================================================================

PROJECT_NAME = "Startup Co-Founder"

VERSION = "1.0"

AUTHOR = "Isuru"

DESCRIPTION = "AI-powered Startup Advisor using Multi-Agent AI"

# ==============================================================================
# LLM PROVIDER
# ==============================================================================

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openrouter")
# Options:
# openrouter
# groq

# ==============================================================================
# OPENROUTER
# ==============================================================================

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# ==============================================================================
# GROQ
# ==============================================================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

# ==============================================================================
# OPTIONAL API KEYS
# ==============================================================================

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# ==============================================================================
# AI MODELS
# ==============================================================================

FAST_MODEL = "google/gemini-2.5-flash-lite"

REASONING_MODEL = "deepseek/deepseek-r1"

GROQ_MODEL = "llama-3.3-70b-versatile"

# ==============================================================================
# REQUEST SETTINGS
# ==============================================================================

REQUEST_TIMEOUT = 60      # API request timeout (seconds)

MAX_RETRIES = 3           # Retry attempts for failed requests

DEBUG = False             # Enable/Disable debug logs