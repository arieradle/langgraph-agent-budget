from shekel import budget
from langgraph.graph import StateGraph

# Enforce budget on LangGraph agent
with budget(max_usd=10.0):
    # Your LangGraph agent runs here
    # All LLM calls will be tracked and limited
    agent.run(input)