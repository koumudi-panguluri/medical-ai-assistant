"""LangGraph multi-agent orchestrator for the medical pipeline.

The graph flows linearly through three stages:
  Intake → Diagnosis → Care Plan

Each node is a specialized agent that reads from and writes to the shared
PatientState, passing structured data downstream.
"""

from langgraph.graph import END, StateGraph

from src.agents.care_plan import run_care_plan
from src.agents.diagnosis import run_diagnosis
from src.agents.intake import run_intake
from src.state import PatientState


def build_medical_graph() -> StateGraph:
    """Construct and compile the multi-agent medical graph."""
    graph = StateGraph(PatientState)

    # Add agent nodes
    graph.add_node("intake", run_intake)
    graph.add_node("diagnosis", run_diagnosis)
    graph.add_node("care_plan", run_care_plan)

    # Define the pipeline flow
    graph.set_entry_point("intake")
    graph.add_edge("intake", "diagnosis")
    graph.add_edge("diagnosis", "care_plan")
    graph.add_edge("care_plan", END)

    return graph.compile()
