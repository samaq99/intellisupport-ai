"""
Custom exceptions for the IntelliSupport AI system.

Why custom exceptions:
1. Better error categorization
2. More informative error messages
3. Easier debugging
4. Cleaner error handling
"""


class IntelliSupportError(Exception):
    """Base exception for all IntelliSupport errors."""
    
    def __init__(self, message: str, original_error: Exception = None):
        self.message = message
        self.original_error = original_error
        super().__init__(self.message)
    
    def __str__(self):
        if self.original_error:
            return f"{self.message} (Original: {self.original_error})"
        return self.message


class AgentError(IntelliSupportError):
    """Errors related to AI agent operations."""
    pass


class ToolError(IntelliSupportError):
    """Errors related to agent tools."""
    pass


class MemoryError(IntelliSupportError):
    """Errors related to conversation memory."""
    pass


class ConfigurationError(IntelliSupportError):
    """Errors related to system configuration."""
    pass