#!/usr/bin/env python3
"""
Simple launcher script for TextCopy
"""
import sys
from pathlib import Path

# Add parent directory to path so we can import src as a package
sys.path.insert(0, str(Path(__file__).parent))

from src.textcopy import main

if __name__ == '__main__':
    main()
