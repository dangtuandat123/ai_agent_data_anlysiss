from typing_extensions import Dict, Any
from langgraph.graph import StateGraph, END, START
from langgraph.checkpoint.memory import MemorySaver
from core.state import State
from agent.hypothesis_agent import create_hypothesis_agent
from agent.process_agent import create_process_agent, create_handoff_tool
from agent.code_agent import create_code_agent
from agent.aboutdata_agent import create_aboutdata_agent

class WorkflowManager:
    def __init__(self, language_models):
        """
        Initialize the workflow manager with language models and working directory.
        
        Args:
            language_models (dict): Dictionary containing language model instances
            working_directory (str): Path to the working directory
        """
        self.language_models = language_models
        self.workflow = None
        self.memory = None
        self.graph = None
        self.setup_workflow()


    def setup_workflow(self):
        """Set up the workflow graph"""

        llm = self.language_models["llm"]


                # Create each agent using their respective creation functions
        hypothesis_agent= create_hypothesis_agent(llm)


        code_agent = create_code_agent(llm)

        aboutdata_agent = create_aboutdata_agent(llm)

        # Handoffs
        assign_to_aboutdata_agent = create_handoff_tool(
            agent_name="AboutData",
            description="Assign task to a aboutata agent.",
        )

        assign_to_code_agent = create_handoff_tool(
            agent_name="Coder",
            description="Assign task to a code agent.",
        )

        assign_to_hypothesis_agent = create_handoff_tool(
            agent_name="Hypothesis",
            description="Assign task to a hypothesis agent.",
        )

        tools = [assign_to_aboutdata_agent, assign_to_code_agent,assign_to_hypothesis_agent]
        process_agent = create_process_agent(llm, tools)
        self.workflow = StateGraph(State)
        
        # Add nodes
        self.workflow.add_node("Hypothesis", hypothesis_agent)
        self.workflow.add_node("Process", process_agent, destinations=("AboutData","Hypothesis", "Coder", END ))
        self.workflow.add_node("AboutData", aboutdata_agent)
        self.workflow.add_node("Coder", code_agent)

        # Add edges
        self.workflow.add_edge(START, "Process")
        self.workflow.add_edge("AboutData", "Process")
        self.workflow.add_edge("Coder", "Process")
        self.workflow.add_edge("Hypothesis", "Process")



        # Compile workflow
        self.memory = MemorySaver()
        self.graph = self.workflow.compile(checkpointer=self.memory)

    def get_graph(self):
        """Return the compiled workflow graph"""
        return self.graph
