from abc import ABC, abstractmethod

class ResearchStrategy(ABC):
    """
    The Abstract Base Class (ABC) for all research strategies.

    This class defines the contract for how a research task should be conducted,
    allowing different concrete strategies to be interchanged.
    """

    @abstractmethod
    def conduct_research(self, topic: str) -> str:
        """
        Conducts research on a given topic.
        All concrete strategy subclasses MUST implement this method.

        Args:
            topic (str): The research topic.

        Returns:
            str: The raw research findings.
        """
        pass
