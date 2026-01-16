# agents/reporting_agent.py
from agents.base_agent import BaseAgent
from patterns.agent_factory import AgentFactory
from patterns.event_manager import EventManager, Observer
from typing import Dict, Any, Optional

@AgentFactory.register("reporting")
class ReportingAgent(BaseAgent, Observer):
    """
    A concrete agent specialized in generating a final report.
    It acts as an Observer, listening for 'analysis_completed' events
    to produce the final output of the system.
    """

    def __init__(
        self,
        agent_id: str,
        event_manager: Optional[EventManager] = None
    ):
        # Initialize both parent classes
        super().__init__(agent_id) 
        Observer.__init__(self)

        self.event_manager = event_manager if event_manager else EventManager()

        # Subscribe to the 'analysis_completed' event upon creation
        self.event_manager.attach("analysis_completed", self)
        print(f"ReportingAgent {self.agent_id} initialized and observing 'analysis_completed' events.")

    def execute_task(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes the reporting task on the provided analysis summary.
        This is the final step in the workflow.
        """
        topic = data.get("topic", "N/A")
        analysis_summary = data.get("analysis_summary", "No summary provided.")

        print("\n" + "="*50)
        print(f"FINAL REPORT by {self.agent_id}")
        print("="*50)
        print(f"Topic: {topic}")
        print("\n--- Analysis Summary ---")
        print(analysis_summary)
        print("\n" + "="*50)
        print("--- END OF REPORT ---")
        
        final_report = {"topic": topic, "summary": analysis_summary}
        
        # Notify that the entire workflow is complete
        self.event_manager.notify("workflow_completed", final_report)
        
        return final_report

    def update(self, subject: EventManager, event_type: str, event_data: Dict[str, Any]):
        """
        Receives updates from the EventManager.
        If 'analysis_completed', it triggers its own reporting task.
        """
        if event_type == "analysis_completed":
            print(f"\nReportingAgent {self.agent_id}: Received 'analysis_completed' event. Generating final report...")
            self.execute_task(event_data)
