# tools/mock_tools.py

class MockWebSearchTool:
    """
    A mock tool that simulates searching the web.
    It prints a message and returns a predefined fake result.
    """
    def search(self, query: str) -> str:
        """Simulates performing a web search."""
        print(f"    [MockWebSearchTool] Searching the web for: '{query}'...")
        return f"FAKE_WEB_RESULT: Comprehensive findings on '{query}' from various online sources."

class MockDatabaseTool:
    """
    A mock tool that simulates querying a database.
    It prints a message and returns a predefined fake result.
    """
    def query(self, data: str) -> str:
        """Simulates querying a database with given data."""
        print(f"    [MockDatabaseTool] Querying database with data derived from: '{data}'...")
        return f"FAKE_DB_RESULT: Relevant entries and cross-references for '{data}' from database."

class MockAnalysisTool:
    """
    A mock tool that simulates analyzing data.
    """
    def analyze(self, raw_data: str) -> str:
        """Simulates performing data analysis."""
        print(f"    [MockAnalysisTool] Analyzing raw data: '{raw_data[:50]}...'")
        return f"FAKE_ANALYSIS_RESULT: Key insights and summary from '{raw_data[:30]}...'"
