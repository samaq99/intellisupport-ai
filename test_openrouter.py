"""
Test OpenRouter connection with LangChain.

This verifies that:
1. Our configuration loads correctly
2. LangChain can connect to OpenRouter
3. Basic API calls work
"""

import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from intellisupport.config import Config
from langchain_openai import ChatOpenAI

def test_openrouter_connection():
    """Test basic connection to OpenRouter"""
    print("Testing OpenRouter connection...")
    
    # Validate configuration
    Config.validate()
    
    # Create LangChain LLM with OpenRouter settings
    llm = ChatOpenAI(
        model=Config.OPENAI_MODEL,
        temperature=Config.OPENAI_TEMPERATURE,
        api_key=Config.OPENAI_API_KEY,
        base_url=Config.OPENAI_API_BASE,
        max_tokens=100
    )
    
    print(f"Created LLM with model: {Config.OPENAI_MODEL}")
    
    # Try a simple test query (free model might have limitations)
    try:
        response = llm.invoke("Hello, can you hear me? Just say 'Connection successful' if you can.")
        print(f"Response: {response.content}")
        print("\n[SUCCESS] OpenRouter connection working!")
        return True
    except Exception as e:
        print(f"\n[ERROR] Connection failed: {e}")
        print("\nPossible issues:")
        print("1. OpenRouter API key invalid/expired")
        print("2. Free model rate limits reached")
        print("3. Network connectivity issue")
        print(f"\nKey used: {Config.OPENAI_API_KEY[:20]}...")
        print(f"API Base: {Config.OPENAI_API_BASE}")
        return False

def test_config():
    """Test configuration loading"""
    print("\nTesting configuration...")
    print(f"API Key present: {'Yes' if Config.OPENAI_API_KEY else 'No'}")
    print(f"Key length: {len(Config.OPENAI_API_KEY) if Config.OPENAI_API_KEY else 0}")
    print(f"Model: {Config.OPENAI_MODEL}")
    print(f"API Base: {Config.OPENAI_API_BASE}")
    return Config.OPENAI_API_KEY is not None

if __name__ == "__main__":
    print("=" * 50)
    print("OpenRouter + LangChain Integration Test")
    print("=" * 50)
    
    config_ok = test_config()
    
    if config_ok:
        print("\n" + "-" * 50)
        connection_ok = test_openrouter_connection()
        
        if connection_ok:
            print("\n" + "=" * 50)
            print("✅ ALL TESTS PASSED - Ready for LangChain!")
            print("=" * 50)
        else:
            print("\n" + "=" * 50)
            print("⚠️  Connection test failed")
            print("We can still proceed with mock data for learning")
            print("=" * 50)
    else:
        print("\n" + "=" * 50)
        print("❌ Configuration test failed")
        print("Check your .env file")
        print("=" * 50)