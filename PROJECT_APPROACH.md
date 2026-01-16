# Project Approach: Multi-Agent System using Design Patterns

## 1. Project Goal

The primary goal of this project is to build a well-architected, modular multi-agent system from the ground up using pure Python. The focus is not on creating a production-level AI, but on demonstrating a deep understanding of core OOP software design patterns by implementing them to solve specific architectural problems.

The system will simulate an automated research and reporting workflow. A user will provide a topic, and a team of specialized agents will work together to produce a final report.

## 2. Core Principles

- **Mock Objects:** To keep the focus on architecture, the system will use "mock" tools instead of real APIs. For example, a `MockWebSearchTool` will simulate web searches without making actual network calls.
- **First Principles:** The system will be built from scratch, without relying on external agentic frameworks, to clearly showcase the implementation of each design pattern.

## 3. Technology Stack

- **Version Control:** Git & GitHub
- **Project/Environment Management:** `uv`
- **Language:** Python

## 4. Proposed Directory Structure

The project will be organized into the following modular structure:

```
multi_agent_system/
├── .gitignore
├── uv.lock
├── pyproject.toml
├── PROJECT_APPROACH.md  <-- This file
├── main.py                # Main script to run the simulation
│
├── agents/                # Module for all agent-related code
│   ├── __init__.py
│   ├── base_agent.py      # The BaseAgent ABC
│   └── (other agent files will be created here)
│
├── patterns/              # Module for our core design patterns
│   ├── __init__.py
│   ├── event_manager.py   # The EventManager Singleton
│   └── agent_factory.py   # The AgentFactory
│
├── strategies/            # Module for different agent strategies
│   ├── __init__.py
│   ├── base_strategy.py   # The ResearchStrategy ABC
│   └── (other strategy files will be created here)
│
└── tools/                 # Module for all tools
    ├── __init__.py
    └── mock_tools.py      # Our MockWebSearchTool, etc.
```

## 5. System Workflow & Design Patterns

The system operates on a decoupled, event-driven workflow that utilizes four key design patterns.

### a. The Singleton Pattern
- **Problem:** How do all independent agents communicate without being tightly coupled?
- **Our Implementation:** We will create an `EventManager` as a **Singleton**. This class will provide a single, global "message board" for the entire application. Agents will post events to this single instance, and other agents can listen to it.
- **File:** `patterns/event_manager.py`

### b. The Factory Pattern
- **Problem:** How does the main system create different types of agents (e.g., `ResearchAgent`, `AnalysisAgent`) without knowing their specific class names or how to construct them?
- **Our Implementation:** We will build an `AgentFactory` with a self-registering decorator. This **Factory** will be the central authority for creating all agents. The main loop will ask the factory for an agent by a "type" string (e.g., "research"), and the factory will handle the details of instantiation.
- **File:** `patterns/agent_factory.py`

### c. The Observer Pattern
- **Problem:** How does an agent (e.g., `AnalysisAgent`) know when an event it cares about (e.g., `"research_complete"`) has occurred?
- **Our Implementation:** The `EventManager` (our Singleton Subject) will work with the **Observer** pattern. Agents will act as Observers, subscribing to specific event types (e.g., `event_manager.attach("research_complete", analysis_agent)`). When an event is posted, the `EventManager` will notify only the subscribed observers.
- **File:** `patterns/event_manager.py` (Subject logic) and the concrete agent files (Observer logic).

### d. The Strategy Pattern
- **Problem:** How can an agent, like a `ResearchAgent`, perform its task in different ways (e.g., a quick scan vs. a deep dive) without using messy `if/else` logic?
- **Our Implementation:** We will use the **Strategy** pattern. The `ResearchAgent` will be composed of a `ResearchStrategy` object. We will define concrete strategies like `QuickScanResearch` and `DeepDiveResearch`. The agent will delegate the "how-to" of its task to its current strategy object and can even switch strategies at runtime.
- **File:** `strategies/base_strategy.py` and `strategies/research_strategies.py`.

## 6. Step-by-Step Coding Plan

We will build the project in the following sequence:

1.  **Define Interfaces (ABCs):** Create the abstract base classes `BaseAgent` in `agents/base_agent.py` and `ResearchStrategy` in `strategies/base_strategy.py`.
2.  **Implement Core Patterns:** Implement the `EventManager` Singleton and the `AgentFactory`.
3.  **Create Concrete Components:** Implement the `Mock Tools`, concrete `Strategies`, and concrete `Agent` classes.
4.  **Orchestrate in `main.py`:** Write the main script to tie everything together and run a full simulation of the workflow.
