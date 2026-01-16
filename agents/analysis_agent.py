# agents/analysis_agent.py
from agents.base_agent import BaseAgent
from patterns.agent_factory import AgentFactory
from patterns.event_manager import EventManager, Observer
from tools.mock_tools import MockAnalysisTool
from typing import Dict, Any, Optional

@AgentFactory.register("analysis")
class AnalysisAgent(BaseAgent, Observer): # AnalysisAgent is both an Agent and an Observer
    """
    A concrete agent specialized in analyzing research findings.
    It acts as an Observer, listening for 'research_completed' events
    and uses a mock analysis tool.
    """

    def __init__(
        self,
        agent_id: str,
        analysis_tool: Optional[MockAnalysisTool] = None,
        event_manager: Optional[EventManager] = None
    ):
        super().__init__(agent_id)
        # Initialize the Observer part of the class
        Observer.__init__(self) 
        
        self.analysis_tool = analysis_tool if analysis_tool else MockAnalysisTool()
        self.event_manager = event_manager if event_manager else EventManager() # Get the Singleton

        # AnalysisAgent immediately subscribes to research_completed events
        self.event_manager.attach("research_completed", self)
        print(f"AnalysisAgent {self.agent_id} initialized and observing 'research_completed' events.")

    def execute_task(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes the analysis task on the provided research findings.
        Notifies the EventManager about task progress.
        """
        raw_research_findings = data.get("research_findings")
        topic = data.get("topic", "N/A")

        if not raw_research_findings:
            print(f"AnalysisAgent {self.agent_id}: No findings to analyze for topic '{topic}'.")
            return {"agent_id": self.agent_id, "task": "analysis", "status": "no_data"}

        # Notify task started
        self.event_manager.notify(
            "task_started", {"agent_id": self.agent_id, "task": "analysis", "topic": topic}
        )
        
        # Perform analysis using the mock tool
        analysis_results = self.analysis_tool.analyze(raw_research_findings)

        results = {
            "agent_id": self.agent_id,
            "task": "analysis",
            "topic": topic,
            "analysis_summary": analysis_results
        }
        
        # Notify task completed
        self.event_manager.notify(
            "analysis_completed", results
        )
        print(f"AnalysisAgent {self.agent_id}: Analysis for '{topic}' complete.")
        return results

    def update(self, subject: EventManager, event_type: str, event_data: Dict[str, Any]):
        """
        Receives updates from the EventManager.
        If 'research_completed', it triggers its own analysis task.
        """
        if event_type == "research_completed":
            print(f"\nAnalysisAgent {self.agent_id}: Received 'research_completed' event for topic '{event_data.get('topic')}'. Starting analysis...")
            # Trigger its own execute_task with the received data
            self.execute_task(event_data)