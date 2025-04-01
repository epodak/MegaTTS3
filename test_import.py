import sys
print("Python path:", sys.path)
try:
    import tts
    print("tts module found!")
except ImportError as e:
    print("Import error:", e) 