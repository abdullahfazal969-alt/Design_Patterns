# agents/research_agent.py
from agents.base_agent import BaseAgent
from patterns.agent_factory import AgentFactory
from patterns.event_manager import EventManager
from strategies.base_strategy import ResearchStrategy
from strategies.research_strategies import StandardResearch
from tools.mock_tools import MockWebSearchTool, MockDatabaseTool
from typing import Dict, Any, Optional

@AgentFactory.register("research")
class ResearchAgent(BaseAgent):
    """
    A concrete agent specialized in conducting research.
    It uses the Strategy pattern to vary its research approach
    and interacts with mock tools.
    """

    def __init__(
        self,
        agent_id: str,
        strategy: Optional[ResearchStrategy] = None,
        web_tool: Optional[MockWebSearchTool] = None,
        db_tool: Optional[MockDatabaseTool] = None,
        event_manager: Optional[EventManager] = None
    ):
        super().__init__(agent_id)
        self.strategy = strategy if strategy else StandardResearch()
        self.web_tool = web_tool if web_tool else MockWebSearchTool()
        self.db_tool = db_tool if db_tool else MockDatabaseTool()
        self.event_manager = event_manager if event_manager else EventManager() # Get the Singleton
        print(f"ResearchAgent {self.agent_id} initialized with strategy: {self.strategy.__class__.__name__}")
        
    def _select_strategy(self, topic: str) -> ResearchStrategy:
        """
        Internal logic to select a strategy based on the topic.
        This demonstrates the agent's 'smartness' in choosing.
        """
        if "deep dive" in topic.lower() or "comprehensive" in topic.lower():
            from strategies.research_strategies import DeepDiveResearch
            print(f"ResearchAgent {self.agent_id}: Topic suggests DeepDive strategy.")
            return DeepDiveResearch()
        elif "quick" in topic.lower() or "headlines" in topic.lower():
            from strategies.research_strategies import QuickScanResearch
            print(f"ResearchAgent {self.agent_id}: Topic suggests QuickScan strategy.")
            return QuickScanResearch()
        else:
            print(f"ResearchAgent {self.agent_id}: Defaulting to StandardResearch strategy.")
            return StandardResearch()

    def execute_task(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes the research task based on the provided topic and selected strategy.
        Notifies the EventManager about task progress.
        """
        topic = data.get("topic")
        if not topic:
            raise ValueError("ResearchAgent requires a 'topic' in the input data.")

        # Agent selects its own strategy (as per your suggestion)
        self.strategy = self._select_strategy(topic)
        
        # Notify task started
        self.event_manager.notify(
            "task_started", {"agent_id": self.agent_id, "task": "research", "topic": topic}
        )
        
        # Conduct research using the selected strategy
        raw_web_results = self.web_tool.search(topic)
        combined_results = self.db_tool.query(raw_web_results) # Use both tools as part of strategy

        research_findings = self.strategy.conduct_research(topic) # This is where strategy is actually used

        # Prepare results
        results = {
            "agent_id": self.agent_id,
            "task": "research",
            "topic": topic,
            "raw_web_results": raw_web_results,
            "combined_results": combined_results,
            "research_findings": research_findings
        }
        
        # Notify task completed
        self.event_manager.notify(
            "research_completed", results
        )
        print(f"ResearchAgent {self.agent_id}: Research on '{topic}' complete.")
        return results

    def set_strategy(self, new_strategy: ResearchStrategy):
        """Allows changing the research strategy at runtime."""
        self.strategy = new_strategy
        print(f"ResearchAgent {self.agent_id}: Strategy changed to {self.strategy.__class__.__name__}.")