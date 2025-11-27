"""Unit Tests"""
from src.agent import LongTermMemory, ToolKit, ProductivityAgent, AgentMetrics

def test_memory_store():
    mem = LongTermMemory()
    id = mem.store("task", "Test task")
    assert id is not None
    assert len(mem.memory) == 1

def test_memory_retrieve():
    mem = LongTermMemory()
    mem.store("task", "Task 1")
    mem.store("task", "Task 2")
    context = mem.retrieve_context("test")
    assert "Task 1" in context

def test_parse_task():
    result = ToolKit.parse_task("Complete report")
    assert result["status"] == "parsed"
    assert result["task"] == "Complete report"

def test_schedule():
    result = ToolKit.generate_schedule(["Task A", "Task B", "Task C"])
    assert result["total_tasks"] == 3

def test_progress():
    result = ToolKit.evaluate_progress(5, 10)
    assert result["completion_percent"] == 50.0
    assert result["remaining_tasks"] == 5

def test_metrics():
    result = ToolKit.calculate_metrics({})
    assert "efficiency_score" in result

def test_agent_init():
    agent = ProductivityAgent("test_key")
    assert agent.metrics.total_requests == 0

def test_agent_query():
    agent = ProductivityAgent("test_key")
    response = agent.process_user_input("Help me organize tasks")
    assert response is not None
    assert agent.metrics.total_requests == 1

if __name__ == "__main__":
    test_memory_store()
    test_memory_retrieve()
    test_parse_task()
    test_schedule()
    test_progress()
    test_metrics()
    test_agent_init()
    test_agent_query()
    print("All tests passed!")
