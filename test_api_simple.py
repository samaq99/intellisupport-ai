"""
Simple API test to check if OpenRouter is working.
"""
import os
from dotenv import load_dotenv

# Load environment
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
api_base = os.getenv("OPENAI_API_BASE", "https://openrouter.ai/api/v1")

print(f"API Key exists: {bool(api_key)}")
print(f"API Key length: {len(api_key) if api_key else 0}")
print(f"API Base: {api_base}")

# Check if key looks valid
if api_key:
    if api_key.startswith("sk-or-v1-"):
        print("✅ API key format looks correct (OpenRouter)")
    else:
        print("⚠️  API key format unexpected")
else:
    print("❌ No API key found in .env")

# Check .env file
print(f"\n.env file exists: {os.path.exists('.env')}")