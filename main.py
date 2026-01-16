# main.py
from patterns.event_manager import EventManager
from patterns.agent_factory import AgentFactory
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.reporting_agent import ReportingAgent # Import our new agent
from tools.mock_tools import MockWebSearchTool, MockDatabaseTool, MockAnalysisTool
from strategies.research_strategies import StandardResearch, DeepDiveResearch, QuickScanResearch

def main():
    print("--- Initializing Multi-Agent System ---")

    # 1. Get the EventManager Singleton
    event_manager = EventManager()

    # 2. Prepare Mock Tools
    web_tool = MockWebSearchTool()
    db_tool = MockDatabaseTool()
    analysis_tool = MockAnalysisTool()

    # 3. Create the listening agents that will react to events
    # The AnalysisAgent will be created and will automatically subscribe to 'research_completed'
    analysis_agent = AgentFactory.create_agent(
        "analysis", 
        "DataMiner", 
        analysis_tool=analysis_tool, 
        event_manager=event_manager
    )
    
    # The new ReportingAgent will be created and will automatically subscribe to 'analysis_completed'
    reporting_agent = AgentFactory.create_agent(
        "reporting",
        "SummarizerBot",
        event_manager=event_manager
    )

    print("\n--- System Ready. Initiating Workflow ---")

    # Define a sample research topic
    topic = "The future of AI in space exploration (deep dive)"

    # 4. Create the initial agent to kick off the workflow
    research_agent = AgentFactory.create_agent(
        "research",
        "ExplorerBot",
        web_tool=web_tool,
        db_tool=db_tool,
        event_manager=event_manager,
    )

    # 5. Kick off the entire task cascade with a single command
    print(f"\n--- Main System: Assigning task to {research_agent.agent_id} ---")
    research_agent.execute_task({"topic": topic})

    print("\n--- Workflow Simulation Completed ---")

if __name__ == "__main__":
    main()
