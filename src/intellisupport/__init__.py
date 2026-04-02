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
- chains: LangChain processing chains
- config: Central configuration management
"""

__version__ = "0.1.0"
__author__ = "Saad Maqsood"
__email__ = "samaq99@gmail.com"

# Package-level exports (will be populated as we build components)
from .config import Config

# Import error types for easy access
try:
    from .utils.exceptions import (
        IntelliSupportError,
        AgentError,
        ToolError,
        MemoryError
    )
except ImportError:
    # Define placeholder exceptions if not yet created
    class IntelliSupportError(Exception):
        """Base exception for IntelliSupport AI"""
        pass
    
    class AgentError(IntelliSupportError):
        """Agent-related errors"""
        pass
    
    class ToolError(IntelliSupportError):
        """Tool-related errors"""
        pass
    
    class MemoryError(IntelliSupportError):
        """Memory-related errors"""
        pass

# Logging setup
import logging
logger = logging.getLogger(__name__)

# Package initialization
def initialize():
    """Initialize the IntelliSupport AI system."""
    logger.info("IntelliSupport AI v%s initialized", __version__)
    return True