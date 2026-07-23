import json

from agents.base_agent import run_agent

from config import FAST_MODEL

from utils.prompts import REVIEWER_AGENT_PROMPT


def reviewer_agent(
    idea_analysis,
    market_analysis,
    business_model,
    marketing_strategy,
    risk_analysis
):

    project_data = {
        "startup_analysis": idea_analysis,
        "market_analysis": market_analysis,
        "business_model": business_model,
        "marketing_strategy": marketing_strategy,
        "risk_analysis": risk_analysis
    }

    return run_agent(
        system_prompt=REVIEWER_AGENT_PROMPT,
        user_input=json.dumps(
            project_data,
            indent=2
        ),
        model=FAST_MODEL,
        temperature=0.1,
        max_tokens=800
    )