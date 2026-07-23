import json

from agents.base_agent import run_agent

from config import FAST_MODEL

from utils.prompts import RISK_ANALYSIS_PROMPT


def risk_analysis_agent(
    idea_analysis,
    market_analysis,
    business_model,
    marketing_strategy
):

    combined_information = {
        "startup_analysis": idea_analysis,
        "market_analysis": market_analysis,
        "business_model": business_model,
        "marketing_strategy": marketing_strategy
    }

    return run_agent(
        system_prompt=RISK_ANALYSIS_PROMPT,
        user_input=json.dumps(combined_information, indent=2),
        model=FAST_MODEL,
        temperature=0.2,
        max_tokens=800
    )