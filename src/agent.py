"""Productivity AI Agent"""
import logging
from datetime import datetime, timedelta
from typing import Dict, List
from dataclasses import dataclass, asdict
import uuid
import os
from dotenv import load_dotenv

try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class MemoryEntry:
    id: str
    timestamp: str
    entry_type: str
    content: str
    metadata: Dict

@dataclass
class AgentMetrics:
    total_requests: int = 0
    successful_tasks: int = 0
    failed_tasks: int = 0

class LongTermMemory:
    def __init__(self, max_memory_size: int = 100):
        self.memory: List[MemoryEntry] = []
        self.max_memory_size = max_memory_size
    
    def store(self, entry_type: str, content: str, metadata: Dict = None):
        entry = MemoryEntry(str(uuid.uuid4()), datetime.now().isoformat(), entry_type, content, metadata or {})
        self.memory.append(entry)
        if len(self.memory) > self.max_memory_size:
            self.memory.pop(0)
        return entry.id
    
    def retrieve_context(self, query: str, limit: int = 5) -> str:
        if not self.memory:
            return "No context"
        context = "Recent Context:\n"
        for entry in self.memory[-limit:]:
            context += f"- [{entry.entry_type}] {entry.content}\n"
        return context
    
    def get_memory_summary(self) -> Dict:
        return {"total_entries": len(self.memory), "types": list(set(e.entry_type for e in self.memory))}

class ToolKit:
    @staticmethod
    def parse_task(task: str) -> Dict:
        logger.info("parse_task")
        return {"status": "parsed", "task": task, "priority": "medium"}
    
    @staticmethod
    def check_dependencies(task_id: str) -> List[str]:
        logger.info("check_dependencies")
        return []
    
    @staticmethod
    def generate_schedule(tasks: List[str]) -> Dict:
        logger.info("generate_schedule")
        return {"schedule": {}, "total_tasks": len(tasks)}
    
    @staticmethod
    def evaluate_progress(completed: int, total: int) -> Dict:
        logger.info("evaluate_progress")
        pct = (completed/total*100) if total > 0 else 0
        return {"completion_percent": pct, "remaining_tasks": total - completed}
    
    @staticmethod
    def calculate_metrics(data: Dict) -> Dict:
        logger.info("calculate_metrics")
        return {"efficiency_score": 0.85, "productivity_index": 0.78}

class ProductivityAgent:
    def __init__(self, api_key: str):
        self.memory = LongTermMemory()
        self.toolkit = ToolKit()
        self.metrics = AgentMetrics()
        self.session_history = []
        self.model = None
        
        # Initialize Gemini model
        try:
            if not api_key:
                load_dotenv()
                api_key = os.getenv("GOOGLE_API_KEY")
            
            if api_key and GENAI_AVAILABLE:
                genai.configure(api_key=api_key)
                self.model = genai.GenerativeModel('gemini-2.0-flash')
                logger.info("✅ Gemini model initialized")
            else:
                logger.warning("⚠️ No API key or genai not available")
                self.model = None
        except Exception as e:
            logger.error(f"❌ Model init failed: {e}")
            self.model = None
        
        logger.info("Agent initialized")
    
    def process_user_input(self, user_input: str) -> str:
        try:
            self.metrics.total_requests += 1
            context = self.memory.retrieve_context(user_input, limit=3)
            
            # Try to use Gemini if available
            if self.model:
                try:
                    prompt = f"""You are a Productivity AI Agent helping with task management.

Previous Context:
{context}

User Request: {user_input}

Provide a helpful, concise response."""
                    response = self.model.generate_content(prompt, stream=False)
                    agent_response = response.text if response else f"Processed: {user_input}"
                except Exception as api_error:
                    logger.error(f"API call failed: {api_error}")
                    agent_response = f"Error calling AI: {str(api_error)}"
            else:
                agent_response = f"AI model not available. Received: {user_input}"
            
            # Store and track
            self.memory.store("interaction", user_input)
            self.metrics.successful_tasks += 1
            self.session_history.append({
                "timestamp": datetime.now().isoformat(), 
                "user_input": user_input,
                "response": agent_response[:100]
            })
            
            return agent_response
        except Exception as e:
            logger.error(f"Process error: {e}")
            self.metrics.failed_tasks += 1
            return f"Error: {str(e)}"
    
    def get_agent_status(self) -> Dict:
        return {
            "metrics": asdict(self.metrics), 
            "memory": self.memory.get_memory_summary(), 
            "status": "operational",
            "model_available": self.model is not None
        }
    
    def export_session(self) -> Dict:
        return {
            "interactions": self.session_history, 
            "metrics": asdict(self.metrics)
        }
