# strategies/research_strategies.py
from strategies.base_strategy import ResearchStrategy

class StandardResearch(ResearchStrategy):
    """
    A concrete strategy for performing standard, broad-based research.
    """
    def conduct_research(self, topic: str) -> str:
        print(f"    [StandardResearch Strategy] Conducting broad search for '{topic}'...")
        return f"Standard research findings on {topic}."

class DeepDiveResearch(ResearchStrategy):
    """
    A concrete strategy for performing in-depth, detailed research.
    """
    def conduct_research(self, topic: str) -> str:
        print(f"    [DeepDiveResearch Strategy] Performing in-depth analysis and synthesis for '{topic}'...")
        return f"Deep-dive research findings on {topic}."

class QuickScanResearch(ResearchStrategy):
    """
    A concrete strategy for performing a quick, superficial scan.
    """
    def conduct_research(self, topic: str) -> str:
        print(f"    [QuickScanResearch Strategy] Quickly scanning top sources for '{topic}'...")
        return f"Quick scan findings on {topic}."
