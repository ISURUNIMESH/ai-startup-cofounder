from agents.idea_agent import idea_analyzer_agent
from agents.market_agent import market_research_agent

idea = "AI-powered platform for university students to improve mental health."

idea_result = idea_analyzer_agent(idea)

market_result = market_research_agent(idea_result)

print(market_result)