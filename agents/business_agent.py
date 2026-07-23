import json

from agents.base_agent import run_agent

from config import REASONING_MODEL

from utils.prompts import BUSINESS_MODEL_PROMPT


def business_model_agent(
    idea_analysis,
    market_analysis
):

    combined_information = {

        "startup_analysis": idea_analysis,

        "market_analysis": market_analysis

    }

    return run_agent(

        system_prompt=BUSINESS_MODEL_PROMPT,

        user_input=json.dumps(
            combined_information,
            indent=2
        ),

        model=REASONING_MODEL,

        temperature=0.2,

        max_tokens=800

    )