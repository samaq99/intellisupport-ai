"""
Simple API test without unicode.
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
        print("OK: API key format looks correct (OpenRouter)")
    else:
        print("WARNING: API key format unexpected")
else:
    print("ERROR: No API key found in .env")

# Check .env file
print(f"\n.env file exists: {os.path.exists('.env')}")

# Show first few chars of key (for debugging)
if api_key:
    print(f"Key preview: {api_key[:20]}...")