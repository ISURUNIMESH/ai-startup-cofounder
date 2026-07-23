import json

from agents.base_agent import run_agent

from config import FAST_MODEL

from utils.prompts import MARKETING_STRATEGY_PROMPT


def marketing_strategy_agent(
    idea_analysis,
    market_analysis,
    business_model
):

    combined_information = {

        "startup_analysis": idea_analysis,

        "market_analysis": market_analysis,

        "business_model": business_model

    }

    return run_agent(

        system_prompt=MARKETING_STRATEGY_PROMPT,

        user_input=json.dumps(
            combined_information,
            indent=2
        ),

        model=FAST_MODEL,

        temperature=0.2,

        max_tokens=800

    )