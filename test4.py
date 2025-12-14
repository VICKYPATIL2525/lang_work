# Simple conditional workflow for customer feedback
from langgraph.graph import StateGraph, START, END
from langchain_openai import AzureChatOpenAI
from typing import TypedDict
import os

from dotenv import load_dotenv
load_dotenv()

# Setup Azure OpenAI
llm = AzureChatOpenAI(
    deployment_name="gpt-4.1-mini",
    temperature=0.1,
    max_tokens=1000,
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_VERSION"),
    api_key=os.getenv("OPENAI_API_KEY"),
)



# Define state
class State(TypedDict):
    feedback: str      # Customer feedback
    sentiment: str     # positive or negative
    response: str      # Final response

# Node 1: Check if feedback is positive
def check_feedback(state: State):
    # Simple prompt
    prompt = f"Is this feedback positive or negative? Answer only 'positive' or 'negative': {state['feedback']}"
    
    # Get LLM response
    result = llm.invoke(prompt).content
    

    return {'sentiment':result}

# Node 2: Generate thank you for positive feedback
def thank_you(state: State):
    # Simple prompt
    prompt = f"Say thank you for positive feedback: {state['feedback']}"
    
    # Get LLM response
    result = llm.invoke(prompt).content
    
    return {'response': result}

# Node 3: Generate apology for negative feedback
def apology(state: State):
    # Simple prompt
    prompt = f"Apologize and say we'll contact support about: {state['feedback']}"
    
    # Get LLM response
    result = llm.invoke(prompt).content
    
    return {'response': result}

# Build graph
graph = StateGraph(State)

# Add nodes
graph.add_node("check", check_feedback)
graph.add_node("thank", thank_you)
graph.add_node("sorry", apology)

# Add edges
graph.add_edge(START, "check")

# Conditional routing function
def decide_next(state: State):
    if state['sentiment'] == "positive":
        return "thank"
    else:
        return "sorry"

graph.add_conditional_edges(
    "check",
    decide_next,
    {
        "thank": "thank",
        "sorry": "sorry"
    }
)

graph.add_edge("thank", END)
graph.add_edge("sorry", END)

# Compile
workflow = graph.compile()

# Test it
good_feedback = "I love this product! Very good."
bad_feedback = "This product is terrible. Worst ever."

print("Testing GOOD feedback:")
result1 = workflow.invoke({"feedback": good_feedback})
print(f"Sentiment: {result1['sentiment']}")
print(f"Response: {result1['response']}")

print("\nTesting BAD feedback:")
result2 = workflow.invoke({"feedback": bad_feedback})
print(f"Sentiment: {result2['sentiment']}")
print(f"Response: {result2['response']}")