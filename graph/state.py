from typing import TypedDict


class StartupState(TypedDict):
    # User Input
    startup_idea: str

    # Agent Outputs
    idea_analysis: dict
    market_analysis: dict
    business_model: dict
    marketing_strategy: dict
    risk_analysis: dict
    review: dict