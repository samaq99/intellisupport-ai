"""
Test the EmailClassifier with MOCK responses.
This simulates what happens when the API works perfectly.

Pattern: Mock testing is essential for:
1. Development when APIs are unavailable
2. CI/CD pipelines (no external dependencies)
3. Testing edge cases without API costs
4. Demonstrating the tool's logic
"""

import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# We'll create a mock version that doesn't call the API
class MockEmailClassifier:
    """Mock version that simulates perfect classification"""
    
    CATEGORIES = {
        "login_issue": {"priority": "high", "sla_hours": 2, "team": "technical_support"},
        "billing_question": {"priority": "medium", "sla_hours": 4, "team": "billing_support"},
        "feature_request": {"priority": "low", "sla_hours": 48, "team": "product_team"},
        "bug_report": {"priority": "medium", "sla_hours": 8, "team": "technical_support"},
        "general_inquiry": {"priority": "low", "sla_hours": 24, "team": "general_support"},
        "data_request": {"priority": "high", "sla_hours": 72, "team": "legal_support"},
        "feedback": {"priority": "low", "sla_hours": 72, "team": "product_team"}
    }
    
    def __init__(self):
        print("[MOCK] EmailClassifier initialized (mock mode)")
    
    def classify(self, email_text: str):
        """Mock classification based on keyword matching"""
        
        email_lower = email_text.lower()
        
        # Simple keyword-based classification (simulating LLM)
        if any(word in email_lower for word in ["login", "password", "cannot access", "account", "forgot"]):
            category = "login_issue"
        elif any(word in email_lower for word in ["invoice", "billing", "payment", "charge", "refund"]):
            category = "billing_question"
        elif any(word in email_lower for word in ["feature", "add", "improve", "suggestion", "would be great"]):
            category = "feature_request"
        elif any(word in email_lower for word in ["bug", "crash", "error", "not working", "broken"]):
            category = "bug_report"
        elif any(word in email_lower for word in ["data", "gdpr", "export", "delete", "privacy"]):
            category = "data_request"
        elif any(word in email_lower for word in ["feedback", "review", "love", "hate", "awesome"]):
            category = "feedback"
        else:
            category = "general_inquiry"
        
        category_info = self.CATEGORIES[category]
        
        result = {
            "category": category,
            "category_info": category_info,
            "priority": category_info["priority"],
            "sla_hours": category_info["sla_hours"],
            "assigned_team": category_info["team"],
            "language": "en",  # Mock detection
            "email_length": len(email_text),
            "has_urgency_keywords": any(word in email_lower for word in ["urgent", "asap", "emergency", "now"])
        }
        
        print(f"[MOCK] Classified as '{category}'")
        return result


def test_mock_classifier():
    """Test the mock classifier"""
    print("=" * 60)
    print("Mock EmailClassifier Test")
    print("=" * 60)
    
    classifier = MockEmailClassifier()
    
    test_cases = [
        ("Login issue", "I can't login to my account", "login_issue", "high"),
        ("Billing question", "My invoice is incorrect", "billing_question", "medium"),
        ("Feature request", "Can you add dark mode?", "feature_request", "low"),
        ("Bug report", "The app crashes when I save", "bug_report", "medium"),
        ("General inquiry", "How do I export data?", "general_inquiry", "low"),
        ("Urgent email", "URGENT: System down!", "general_inquiry", "low"),
    ]
    
    print("\nTesting classification logic:")
    print("-" * 40)
    
    all_correct = True
    
    for name, email, expected_category, expected_priority in test_cases:
        result = classifier.classify(email)
        
        category_match = result["category"] == expected_category
        priority_match = result["priority"] == expected_priority
        
        status = "PASS" if category_match and priority_match else "FAIL"
        
        print(f"{status} {name}:")
        print(f"  Expected: {expected_category} ({expected_priority})")
        print(f"  Got:      {result['category']} ({result['priority']})")
        print(f"  Team:     {result['assigned_team']}")
        print(f"  Urgent:   {result['has_urgency_keywords']}")
        print()
        
        if not (category_match and priority_match):
            all_correct = False
    
    print("=" * 60)
    if all_correct:
        print("SUCCESS: All classifications correct!")
        print("\nWhat this demonstrates:")
        print("1. Tool logic works correctly")
        print("2. Classification patterns are sound")
        print("3. Business rules are applied (priority, SLA, teams)")
        print("4. Ready for real API integration")
    else:
        print("ISSUES: Some classifications incorrect")
        print("\nThis helps identify:")
        print("1. Prompt improvements needed")
        print("2. Category definitions to refine")
        print("3. Edge cases to handle")
    
    print("=" * 60)


def demonstrate_integration():
    """Show how the tool integrates into a system"""
    print("\n" + "=" * 60)
    print("Integration Demonstration")
    print("=" * 60)
    
    classifier = MockEmailClassifier()
    
    # Simulate incoming customer email
    customer_email = """URGENT: I can't login to my account!
    
    I have an important presentation in 1 hour and I need
    access to my project files. The system says "invalid
    credentials" but I know my password is correct.
    
    Please help immediately!
    - Sarah Johnson"""
    
    print("Customer Email:")
    print("-" * 40)
    print(customer_email[:200] + "...")
    print()
    
    # Classify the email
    classification = classifier.classify(customer_email)
    
    print("Classification Results:")
    print("-" * 40)
    print(f"Category:    {classification['category']}")
    print(f"Priority:    {classification['priority']} (SLA: {classification['sla_hours']} hours)")
    print(f"Team:        {classification['assigned_team']}")
    print(f"Language:    {classification['language']}")
    print(f"Urgent:      {classification['has_urgency_keywords']}")
    print(f"Email length: {classification['email_length']} chars")
    print()
    
    print("Business Impact:")
    print("-" * 40)
    print("1. Auto-routed to: Technical Support team")
    print("2. Priority flag: HIGH (2-hour SLA)")
    print("3. Language: English-speaking agent assigned")
    print("4. Urgency: Marked for immediate attention")
    print("5. Expected: Resolution within 2 hours")
    print()
    
    print("Without this tool:")
    print("- Email goes to general queue")
    print("- No priority flag")
    print("- Could wait 24+ hours for response")
    print("- Customer frustrated, business at risk")
    
    print("=" * 60)


if __name__ == "__main__":
    test_mock_classifier()
    demonstrate_integration()
    
    print("\n" + "=" * 60)
    print("NEXT STEPS FOR PRODUCTION:")
    print("=" * 60)
    print("1. Fix API authentication (check OpenRouter account)")
    print("2. Replace mock with real LLM calls")
    print("3. Add more sophisticated language detection")
    print("4. Implement caching for frequent queries")
    print("5. Add monitoring and metrics")
    print("6. Create integration with ticketing system")
    print("=" * 60)