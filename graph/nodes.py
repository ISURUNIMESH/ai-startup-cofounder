from graph.state import StartupState

from agents.idea_agent import idea_analyzer_agent
from agents.market_agent import market_research_agent
from agents.business_agent import business_model_agent
from agents.marketing_agent import marketing_strategy_agent
from agents.risk_agent import risk_analysis_agent
from agents.reviewer_agent import reviewer_agent


def idea_node(state: StartupState):
    state["idea_analysis"] = idea_analyzer_agent(
        state["startup_idea"]
    )
    return state


def market_node(state: StartupState):
    state["market_analysis"] = market_research_agent(
        state["idea_analysis"]
    )
    return state


def business_node(state: StartupState):
    state["business_model"] = business_model_agent(
        state["idea_analysis"],
        state["market_analysis"]
    )
    return state


def marketing_node(state: StartupState):
    state["marketing_strategy"] = marketing_strategy_agent(
        state["idea_analysis"],
        state["market_analysis"],
        state["business_model"]
    )
    return state


def risk_node(state: StartupState):
    state["risk_analysis"] = risk_analysis_agent(
        state["idea_analysis"],
        state["market_analysis"],
        state["business_model"],
        state["marketing_strategy"]
    )
    return state


def review_node(state: StartupState):
    state["review"] = reviewer_agent(
        state["idea_analysis"],
        state["market_analysis"],
        state["business_model"],
        state["marketing_strategy"],
        state["risk_analysis"]
    )
    return state