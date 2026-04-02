"""
Test the chain YOU just built.
"""
import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# Test 1: Can we import?
print("Test 1: Importing your chain...")
try:
    from intellisupport.chains.basic_support import BasicSupportChain
    print("Import successful!")
except ImportError as e:
    print(f"Import failed: {e}")
    sys.exit(1)

# Test 2: Can we initialize?
print("\nTest 2: Initializing chain...")
try:
    chain = BasicSupportChain()
    print("Chain initialized!")
except Exception as e:
    print(f"Initialization failed: {e}")
    sys.exit(1)

# Test 3: Test with simple input
print("\nTest 3: Testing with simple input...")
test_email = "Hello, I need help with my account."
try:
    response = chain.respond(test_email)
    print(f"Response generated!")
    print(f"\nInput: {test_email}")
    print(f"\nResponse preview: {response[:200]}...")
except Exception as e:
    print(f"Chain execution failed: {e}")

print("\n" + "="*50)
print("TEST COMPLETE!")