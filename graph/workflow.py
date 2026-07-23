from langgraph.graph import StateGraph, END

from graph.state import StartupState

from graph.nodes import (
    idea_node,
    market_node,
    business_node,
    marketing_node,
    risk_node,
    review_node
)


def build_graph():

    workflow = StateGraph(StartupState)

    # Add Nodes
    workflow.add_node("idea", idea_node)
    workflow.add_node("market", market_node)
    workflow.add_node("business", business_node)
    workflow.add_node("marketing", marketing_node)
    workflow.add_node("risk", risk_node)
    workflow.add_node("review", review_node)

    # Entry Point
    workflow.set_entry_point("idea")

    # Edges
    workflow.add_edge("idea", "market")
    workflow.add_edge("market", "business")
    workflow.add_edge("business", "marketing")
    workflow.add_edge("marketing", "risk")
    workflow.add_edge("risk", "review")
    workflow.add_edge("review", END)

    return workflow.compile()