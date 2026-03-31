"""
IntelliSupport AI - Customer Support Automation System

This package provides AI-powered customer support automation
for TechSolutions GmbH, reducing response times from 48+ hours
to under 1 hour for 70% of Tier-1 queries.

Main Components:
- agents: AI agent implementations
- tools: Custom tools for agent interaction
- memory: Conversation history and context
- utils: Utility functions and helpers
"""
__version__ = "0.1.0"
__author__ = "Saad Maqsood"
__email__ = "samaq99@gmail.com"

# Package-level exports
from .agents.support_agent import SupportAgent
from .utils.logger import setup_logger

# Import error types for easy access
from .utils.exceptions import (
    IntelliSupportError,
    AgentError,
    ToolError,
    MemoryError
)

# Logging setup
import logging
logger = logging.getLogger(__name__)

# Package initialization
def initialize():
    """Initialize the IntelliSupport AI system."""
    logger.info("IntelliSupport AI v%s initialized", __version__)
    return True