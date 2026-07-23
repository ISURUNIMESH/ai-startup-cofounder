from agents.idea_agent import idea_analyzer_agent
from agents.market_agent import market_research_agent
from agents.business_agent import business_model_agent
from agents.marketing_agent import marketing_strategy_agent

idea = "AI-powered platform for university students to improve mental health."

idea_result = idea_analyzer_agent(idea)

market_result = market_research_agent(idea_result)

business_result = business_model_agent(
    idea_result,
    market_result
)

marketing_result = marketing_strategy_agent(
    idea_result,
    market_result,
    business_result
)

print(marketing_result)