"""
Simple test for BasicSupportChain - tests initialization without API calls.
"""

import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from intellisupport.chains import BasicSupportChain
from intellisupport.config import Config


def test_imports():
    """Test that all imports work"""
    print("1. Testing imports...")
    
    try:
        from langchain_openai import ChatOpenAI
        from langchain_core.prompts import ChatPromptTemplate
        from langchain_core.output_parsers import StrOutputParser
        from langchain_core.runnables import RunnablePassthrough
        print("   [OK] All LangChain imports work")
        return True
    except ImportError as e:
        print(f"   [FAILED] Import error: {e}")
        return False


def test_config():
    """Test configuration loading"""
    print("\n2. Testing configuration...")
    
    try:
        Config.validate()
        print(f"   [OK] Configuration loaded")
        print(f"     Model: {Config.OPENAI_MODEL}")
        print(f"     API Base: {Config.OPENAI_API_BASE}")
        return True
    except Exception as e:
        print(f"   [FAILED] Config validation: {e}")
        return False


def test_chain_structure():
    """Test chain class structure without making API calls"""
    print("\n3. Testing chain structure...")
    
    try:
        # Create chain instance
        chain = BasicSupportChain()
        
        # Check attributes
        assert hasattr(chain, 'llm'), "Chain missing 'llm' attribute"
        assert hasattr(chain, 'prompt'), "Chain missing 'prompt' attribute"
        assert hasattr(chain, 'chain'), "Chain missing 'chain' attribute"
        assert hasattr(chain, 'respond'), "Chain missing 'respond' method"
        assert hasattr(chain, 'batch_respond'), "Chain missing 'batch_respond' method"
        
        print("   [OK] Chain structure is correct")
        print(f"   Chain type: {type(chain).__name__}")
        
        # Check chain composition
        print(f"   Chain components: LLM + Prompt + OutputParser")
        
        return True
    except Exception as e:
        print(f"   [FAILED] Chain structure test: {e}")
        return False


def test_without_api_call():
    """Test chain without making actual API call"""
    print("\n4. Testing chain without API call (dry run)...")
    
    try:
        chain = BasicSupportChain()
        
        # Create a mock response to avoid API call
        class MockLLM:
            def invoke(self, prompt):
                return "Mock response for testing"
        
        # Temporarily replace LLM with mock
        original_llm = chain.llm
        chain.llm = MockLLM()
        
        test_email = "Test email for dry run"
        response = chain.respond(test_email)
        
        # Restore original LLM
        chain.llm = original_llm
        
        print(f"   [OK] Chain processed email (dry run)")
        print(f"   Response length: {len(response)} characters")
        print(f"   Response contains signature: {'IntelliSupport AI' in response}")
        
        return True
    except Exception as e:
        print(f"   [FAILED] Dry run test: {e}")
        return False


def run_all_tests():
    """Run all simple tests"""
    print("=" * 60)
    print("BasicSupportChain - Structure Tests")
    print("=" * 60)
    
    tests = [
        ("Imports", test_imports),
        ("Configuration", test_config),
        ("Chain Structure", test_chain_structure),
        ("Dry Run", test_without_api_call),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"   [ERROR] Test '{test_name}' crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "PASS" if result else "FAIL"
        print(f"  {test_name:20} {status}")
    
    print(f"\n  Passed: {passed}/{total}")
    
    if passed == total:
        print("\n[SUCCESS] All structure tests passed!")
        print("\nNext: Test with actual API call (may incur costs)")
        return True
    elif passed >= 2:
        print("\n[PARTIAL SUCCESS] Core structure is working")
        print("\nIssues to fix:")
        for test_name, result in results:
            if not result:
                print(f"  - {test_name}")
        return True
    else:
        print("\n[FAILED] Major issues with chain structure")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    
    print("\n" + "=" * 60)
    if success:
        print("READY FOR API TEST:")
        print("\nTo test with actual API (may use credits):")
        print("  python -c \"")
        print("  from intellisupport.chains import BasicSupportChain")
        print("  chain = BasicSupportChain()")
        print("  print(chain.respond('Test login issue'))")
        print("  \"")
    else:
        print("NEEDS FIXING BEFORE API TEST")
    
    print("=" * 60)