from abc import ABC, abstractmethod
from collections import defaultdict

# --- Observer ABC (Interface) ---
class Observer(ABC):
    """
    Abstract Base Class for all Observer participants in the Observer pattern.
    Defines the interface for objects that wish to be notified of events.
    """
    @abstractmethod
    def update(self, subject: 'EventManager', event_type: str, event_data: dict):
        """
        Receives updates from a Subject. Concrete observers must implement this method.

        Args:
            subject (EventManager): The subject that is notifying the observer.
            event_type (str): A string identifying the type of event.
            event_data (dict): A dictionary containing data relevant to the event.
        """
        pass

# --- EventManager (Singleton Subject) ---
class EventManager:
    """
    The EventManager is implemented as a Singleton pattern, ensuring
    there is only one instance globally to manage all events.
    It also acts as the Subject in the Observer pattern, allowing other
    objects (Observers) to subscribe to specific event types.
    """
    
    _instance: 'EventManager' | None = None
    _initialized: bool = False

    def __new__(cls) -> 'EventManager':
        """
        Controls the instance creation process, ensuring only one instance is ever created.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """
        Initializes the EventManager. Ensures that initialization occurs only once.
        Initializes the dictionary to store observers for different event types.
        """
        if self._initialized:
            return
        self._initialized = True
        
        # Dictionary to store observers, mapping event types to a list of Observers
        self._observers: dict[str, list[Observer]] = defaultdict(list)
        print("EventManager: Initialized (Singleton instance created).")

    def attach(self, event_type: str, observer: Observer):
        """
        Attaches an observer to a specific event type.

        Args:
            event_type (str): The type of event the observer wants to subscribe to.
            observer (Observer): The observer instance to attach.
        """
        if observer not in self._observers[event_type]:
            self._observers[event_type].append(observer)
            print(f"EventManager: {observer.__class__.__name__} attached to '{event_type}' events.")

    def detach(self, event_type: str, observer: Observer):
        """
        Detaches an observer from a specific event type.

        Args:
            event_type (str): The type of event the observer wants to unsubscribe from.
            observer (Observer): The observer instance to detach.
        """
        if observer in self._observers[event_type]:
            self._observers[event_type].remove(observer)
            print(f"EventManager: {observer.__class__.__name__} detached from '{event_type}' events.")

    def notify(self, event_type: str, event_data: dict):
        """
        Notifies all attached observers for a specific event type.

        Args:
            event_type (str): The type of event that occurred.
            event_data (dict): A dictionary containing data relevant to the event.
        """
        # print(f"EventManager: Notifying observers for event '{event_type}'...")
        for observer in self._observers[event_type]:
            observer.update(self, event_type, event_data)
        # if not self._observers[event_type]:
            # print(f"EventManager: No observers for '{event_type}'.")
