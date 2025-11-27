"""Agent Configuration"""
import os
from dataclasses import dataclass

@dataclass
class AgentConfig:
    api_key: str = os.getenv("GOOGLE_API_KEY", "your_key_here")
    model_name: str = "gemini-2.0-flash"
    max_memory_size: int = 100
    temperature: float = 0.7
    max_tokens: int = 2000
    log_level: str = "INFO"
