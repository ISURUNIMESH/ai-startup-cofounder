from agents.idea_agent import idea_analyzer_agent
from agents.market_agent import market_research_agent
from agents.business_agent import business_model_agent
from agents.marketing_agent import marketing_strategy_agent
from agents.risk_agent import risk_analysis_agent
from agents.reviewer_agent import reviewer_agent

idea = "AI-powered platform for university students to improve mental health."

# Step 1
idea_result = idea_analyzer_agent(idea)

# Step 2
market_result = market_research_agent(idea_result)

# Step 3
business_result = business_model_agent(
    idea_result,
    market_result
)

# Step 4
marketing_result = marketing_strategy_agent(
    idea_result,
    market_result,
    business_result
)

# Step 5
risk_result = risk_analysis_agent(
    idea_result,
    market_result,
    business_result,
    marketing_result
)

# Step 6
review_result = reviewer_agent(
    idea_result,
    market_result,
    business_result,
    marketing_result,
    risk_result
)

print(review_result)