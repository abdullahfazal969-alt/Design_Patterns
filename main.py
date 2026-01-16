# main.py
from patterns.event_manager import EventManager
from patterns.agent_factory import AgentFactory
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
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

    # 3. Create the AgentFactory
    # AgentFactory is configured to work with agent classes that self-register.
    # No need to explicitly pass tools to the factory here, as agents will get them
    # directly or through a ToolManager if we were to implement one.

    # 4. Create the AnalysisAgent (which will immediately subscribe to 'research_completed' events)
    analysis_agent = AgentFactory.create_agent(
        "analysis", 
        "DataMiner", 
        analysis_tool=analysis_tool, 
        event_manager=event_manager
    )
    # The AnalysisAgent automatically attaches itself during its __init__
    # analysis_agent.event_manager.attach("research_completed", analysis_agent) # Not needed as agent does this itself

    print("\n--- System Ready. Initiating Workflow ---")

    # Define a sample research topic
    topic_1 = "The future of AI in space exploration (deep dive)"
    topic_2 = "Quick scan of current renewable energy headlines"

    # 5. Create the ResearchAgent for Topic 1 (with specific tools)
    research_agent_1 = AgentFactory.create_agent(
        "research",
        "ExplorerBot",
        web_tool=web_tool,
        db_tool=db_tool,
        event_manager=event_manager,
        # We can explicitly set a strategy, or let the agent decide
        # strategy=DeepDiveResearch()
    )

    # 6. Kick off the research task for Topic 1
    print(f"\n--- Main System: Assigning task to {research_agent_1.agent_id} ---")
    research_agent_1.execute_task({"topic": topic_1})
    
    # 7. Create another ResearchAgent for Topic 2
    research_agent_2 = AgentFactory.create_agent(
        "research",
        "ScannerBot",
        web_tool=web_tool,
        db_tool=db_tool,
        event_manager=event_manager,
    )
    
    print(f"\n--- Main System: Assigning task to {research_agent_2.agent_id} ---")
    research_agent_2.execute_task({"topic": topic_2})

    print("\n--- Workflow Completed ---")

if __name__ == "__main__":
    main()