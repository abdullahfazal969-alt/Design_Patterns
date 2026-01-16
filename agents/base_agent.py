from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """
    The Abstract Base Class (ABC) for all agents in the multi-agent system.

    This class defines the essential contract that all concrete agents must follow,
    ensuring they can be treated polymorphically by the system.
    """

    def __init__(self, agent_id: str):
        """
        Initializes the agent with a unique ID.
        
        Args:
            agent_id (str): A unique identifier for the agent.
        """
        self.agent_id = agent_id
        # print(f"Agent {self.agent_id} initialized.") # Keep prints minimal in core classes

    @abstractmethod
    def execute_task(self, data: dict) -> dict:
        """
        The core method for an agent to perform its primary function.
        All concrete agent subclasses MUST implement this method.

        Args:
            data (dict): The input data or task description for the agent.
                         Expected to contain 'topic' among other things.

        Returns:
            dict: The result of the agent's task, typically including processed data.
        """
        pass
