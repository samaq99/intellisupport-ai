 # src/intellisupport/config.py
"""
Central configuration management for IntelliSupport AI.

Why this matters:
1. Single source of truth for all settings
2. Environment-based configuration (dev/test/prod)
3. Type safety and validation
4. Easy testing with different configurations
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
# Try multiple possible locations for .env
possible_paths = [
    Path(__file__).parent.parent.parent.parent / '.env',  # project root
    Path(__file__).parent.parent.parent / '.env',         # src parent
    Path.cwd() / '.env',                                  # current directory
]

for env_path in possible_paths:
    if env_path.exists():
        load_dotenv(env_path)
        print(f"Loaded .env from: {env_path}")
        break
else:
    print("⚠️  No .env file found, using system environment variables")


class Config:
    """Central configuration management"""
    
    # OpenRouter API settings
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://openrouter.ai/api/v1")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "openrouter/free")
    
    # Model settings (adjust based on your OpenRouter plan)
    OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.1"))
    MAX_RESPONSE_TOKENS = int(os.getenv("MAX_RESPONSE_TOKENS", "500"))
    
    # Application settings
    SUPPORT_EMAIL_DOMAIN = "techsolutions-gmbh.de"
    DEFAULT_LANGUAGE = "en"
    SUPPORT_SLA_HOURS = 4
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "logs/intellisupport.log")
    
    @classmethod
    def validate(cls) -> None:
        """Validate all required configurations are set"""
        errors = []
        
        # Validate API key exists
        if not cls.OPENAI_API_KEY:
            errors.append("OPENAI_API_KEY not set in .env file")
        elif len(cls.OPENAI_API_KEY) < 20:
            errors.append("OPENAI_API_KEY appears too short (should be 20+ characters)")
        
        if errors:
            raise ValueError(f"Configuration errors: {', '.join(errors)}")
        
        print(f"[OK] Configuration validated successfully")
        print(f"     Model: {cls.OPENAI_MODEL}")
        print(f"     API Base: {cls.OPENAI_API_BASE}")
        
    @classmethod
    def get_model_settings(cls) -> dict:
        """Get model settings as dictionary for LangChain"""
        return {
            "model": cls.OPENAI_MODEL,
            "temperature": cls.OPENAI_TEMPERATURE,
            "max_tokens": cls.MAX_RESPONSE_TOKENS,
            "api_key": cls.OPENAI_API_KEY,
            "base_url": cls.OPENAI_API_BASE,
        }


# Quick test if run directly
if __name__ == "__main__":
    try:
        Config.validate()
        print("🎉 Config test passed!")
    except ValueError as e:
        print(f"❌ Config test failed: {e}")