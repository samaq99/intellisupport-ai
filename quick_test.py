#!/usr/bin/env python3
"""
Quick test of BasicSupportChain with actual API call.
"""

import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from intellisupport.chains import BasicSupportChain

def main():
    print("Quick API Test")
    print("-" * 40)
    
    try:
        # Create chain
        chain = BasicSupportChain()
        print("[OK] Chain created")
        
        # Simple test query
        test_query = "I cannot login to my account"
        print(f"[OK] Test query: '{test_query}'")
        
        # Get response (this makes actual API call)
        print("[WAIT] Calling OpenRouter API...")
        response = chain.respond(test_query)
        
        print(f"\n[OK] Response received ({len(response)} characters)")
        print("-" * 40)
        print("RESPONSE:")
        print(response[:500] + "..." if len(response) > 500 else response)
        print("-" * 40)
        
        print("\n[SUCCESS] BasicSupportChain is working with OpenRouter!")
        
    except Exception as e:
        print(f"\n[ERROR] {e}")
        print("\nPossible issues:")
        print("1. OpenRouter API key invalid/expired")
        print("2. Rate limits reached (free tier)")
        print("3. Network issue")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)