#!/usr/bin/env python3
"""
Test script to verify TextCopy Word document functionality
"""
import sys
from pathlib import Path

# Add parent directory to path to import src as a package
sys.path.insert(0, str(Path(__file__).parent))

from datetime import datetime
from src.config import Config
from src.capture import CapturedText
from src.storage import StorageManager


def test_word_save():
    """Test Word document saving"""
    print("=" * 60)
    print("TextCopy Word Document Test")
    print("=" * 60)
    print()

    # Initialize config
    print("1. Loading configuration...")
    try:
        config = Config('config.yaml')
        print("   ✓ Configuration loaded")
    except Exception as e:
        print(f"   ✗ Error loading config: {e}")
        return False

    # Initialize storage
    print("2. Initializing storage manager...")
    try:
        storage = StorageManager(config)
        print("   ✓ Storage manager initialized")
    except Exception as e:
        print(f"   ✗ Error initializing storage: {e}")
        import traceback
        traceback.print_exc()
        return False

    # Create test capture
    print("3. Creating test capture...")
    test_capture = CapturedText(
        text="This is a test capture to verify Word document functionality is working correctly.",
        timestamp=datetime.now(),
        source="Test Script"
    )
    print(f"   ✓ Test capture created: {len(test_capture.text)} characters")

    # Save to Word
    print("4. Saving to Word document...")
    try:
        success = storage.save_to_word(test_capture)
        if success:
            print(f"   ✓ Saved successfully to: {storage.get_word_path()}")
        else:
            print(f"   ✗ Failed to save to Word")
            return False
    except Exception as e:
        print(f"   ✗ Error saving to Word: {e}")
        import traceback
        traceback.print_exc()
        return False

    # Verify file exists
    print("5. Verifying file exists...")
    word_path = storage.get_word_path()
    if word_path.exists():
        file_size = word_path.stat().st_size
        print(f"   ✓ File exists: {word_path}")
        print(f"   ✓ File size: {file_size} bytes")
    else:
        print(f"   ✗ File does not exist: {word_path}")
        return False

    # Test loading existing document
    print("6. Testing append to existing document...")
    test_capture2 = CapturedText(
        text="This is a SECOND test capture to verify appending works.",
        timestamp=datetime.now(),
        source="Test Script"
    )
    try:
        success = storage.save_to_word(test_capture2)
        if success:
            new_size = word_path.stat().st_size
            print(f"   ✓ Second capture saved successfully")
            print(f"   ✓ New file size: {new_size} bytes (was {file_size} bytes)")
            if new_size > file_size:
                print(f"   ✓ File size increased as expected")
            else:
                print(f"   ⚠ Warning: File size did not increase")
        else:
            print(f"   ✗ Failed to save second capture")
            return False
    except Exception as e:
        print(f"   ✗ Error on second save: {e}")
        import traceback
        traceback.print_exc()
        return False

    print()
    print("=" * 60)
    print("✓ All tests passed!")
    print("=" * 60)
    print()
    print(f"Word document location: {word_path}")
    print(f"You can open it to verify the contents.")
    print()

    return True


if __name__ == '__main__':
    try:
        success = test_word_save()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
