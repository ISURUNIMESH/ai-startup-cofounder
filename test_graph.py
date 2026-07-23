from graph.workflow import build_graph

graph = build_graph()

result = graph.invoke(
    {
        "startup_idea": "AI-powered platform for university students to improve mental health."
    }
)

print(result)