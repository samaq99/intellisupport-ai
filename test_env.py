try:
    with open('.env', 'r', encoding='utf-8') as f:
        content = f.read()
        print("✅ .env file read successfully")
        print(f"First 50 chars: {content[:50]}")
except Exception as e:
    print(f"❌ Error reading .env: {e}")