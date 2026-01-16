from typing import Type, Dict, Callable
from agents.base_agent import BaseAgent
# We anticipate a ToolManager for the factory to provide tools, but won't implement here yet.
# from tools.tool_manager import ToolManager 

class AgentFactory:
    """
    Factory pattern - creates agents without specifying concrete classes.
    Uses a registry pattern for agents to self-register their types.
    """

    # The registry maps agent type strings to their respective Agent classes.
    _registry: Dict[str, Type[BaseAgent]] = {}

    @classmethod
    def register(cls, agent_type: str) -> Callable[[Type[BaseAgent]], Type[BaseAgent]]:
        """
        A class decorator used to register agent classes with the factory.
        When a class is decorated with @AgentFactory.register("type_name"),
        it automatically adds itself to the factory's registry.

        Args:
            agent_type (str): The unique string identifier for this agent type.

        Returns:
            Callable: A decorator that registers the class.
        """
        def decorator(agent_class: Type[BaseAgent]) -> Type[BaseAgent]:
            if agent_type in cls._registry:
                raise ValueError(f"Agent type '{agent_type}' already registered.")
            cls._registry[agent_type] = agent_class
            # print(f"AgentFactory: Registered '{agent_type}' with class {agent_class.__name__}.")
            return agent_class
        return decorator

    @classmethod
    def create_agent(cls, agent_type: str, agent_id: str, **kwargs) -> BaseAgent:
        """
        Creates an agent instance based on its registered type.

        Args:
            agent_type (str): The string identifier of the agent type to create.
            agent_id (str): The unique ID for the new agent instance.
            **kwargs: Additional keyword arguments to pass to the agent's constructor.

        Returns:
            BaseAgent: An instance of the requested agent type.

        Raises:
            ValueError: If the agent_type is not registered.
        """
        agent_class = cls._registry.get(agent_type)
        if agent_class is None:
            raise ValueError(
                f"Unknown agent type: '{agent_type}'. "
                f"Available types: {list(cls._registry.keys())}"
            )
        # The factory is now responsible for providing dependencies.
        # For simplicity, we pass kwargs directly. A more advanced factory would get these from ToolManager.
        # This will be refined when we integrate ToolManager.
        return agent_class(agent_id=agent_id, **kwargs)

    @classmethod
    def available_types(cls) -> list[str]:
        """
        Lists all agent types currently registered with the factory.

        Returns:
            list[str]: A list of available agent type strings.
        """
        return list(cls._registry.keys())
