# test_encoding.py
import sys
sys.path.insert(0, 'src')
try:
    from intellisupport.chains import __init__
    print("Import successful!")
except SyntaxError as e:
    print(f"Syntax error: {e}")
    print("File still has null bytes")
except Exception as e:
    print(f"Other error: {e}")