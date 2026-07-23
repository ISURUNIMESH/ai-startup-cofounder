import json

from agents.base_agent import run_agent

from config import FAST_MODEL

from utils.prompts import MARKET_RESEARCH_PROMPT


def market_research_agent(idea_analysis):

    return run_agent(

        system_prompt=MARKET_RESEARCH_PROMPT,

        user_input=json.dumps(
            idea_analysis,
            indent=2
        ),

        model=FAST_MODEL,

        temperature=0.2,

        max_tokens=800

    )