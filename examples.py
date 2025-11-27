"""Usage Examples of Productivity AI Agent"""

from src.agent import ProductivityAgent, ToolKit, LongTermMemory
import json

print("=" * 70)
print("PRODUCTIVITY AI AGENT - EXAMPLES")
print("=" * 70)

# Example 1: Tool Usage
print("\n[EXAMPLE 1] Tool Integration")
print("-" * 70)

toolkit = ToolKit()

print("\n1. Parse Task Tool:")
result = toolkit.parse_task("Complete quarterly report by Friday")
print(json.dumps(result, indent=2))

print("\n2. Generate Schedule Tool:")
tasks = ["Code Review", "Write Report", "Team Meeting"]
result = toolkit.generate_schedule(tasks)
print(f"Generated schedule for {result['total_tasks']} tasks")

print("\n3. Evaluate Progress Tool:")
result = toolkit.evaluate_progress(7, 10)
print(f"Progress: {result['completion_percent']}%")

# Example 2: Memory System
print("\n\n[EXAMPLE 2] Memory Management")
print("-" * 70)

memory = LongTermMemory(max_memory_size=10)

print("\nStoring memories...")
memory.store("task", "Complete AI agent capstone project")
memory.store("preference", "User prefers morning work sessions")
memory.store("decision", "Prioritize high-impact tasks first")

print("\nRetrieving context...")
context = memory.retrieve_context("What should I work on?")
print(f"Context:\n{context}")

print("\nMemory Summary:")
summary = memory.get_memory_summary()
print(f"Total entries: {summary['total_entries']}")
print(f"Memory types: {summary['types']}")

# Example 3: Agent Processing
print("\n\n[EXAMPLE 3] Agent Query Processing")
print("-" * 70)

agent = ProductivityAgent("test_api_key")

print("\nProcessing user query...")
query = "Help me organize my 3 project tasks for this week"
response = agent.process_user_input(query)
print(f"\nUser: {query}")
print(f"Agent: {response[:100]}...")

# Example 4: Agent Status
print("\n\n[EXAMPLE 4] Agent Metrics & Status")
print("-" * 70)

status = agent.get_agent_status()
print("\nAgent Status:")
print(json.dumps(status, indent=2, default=str))

# Example 5: Session Export
print("\n\n[EXAMPLE 5] Session Export")
print("-" * 70)

session = agent.export_session()
print(f"\nSession Summary:")
print(f"Total interactions: {len(session['interactions'])}")
print(f"Successful tasks: {session['metrics']['successful_tasks']}")

print("\n" + "=" * 70)
print("✅ Examples completed! Try the API with:")
print("   python src/api.py")
print("   curl http://localhost:5000/health")
print("=" * 70)
