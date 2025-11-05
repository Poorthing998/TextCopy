#!/bin/bash
# TextCopy Installation Script for Linux/macOS

echo "=================================="
echo "TextCopy Installation Script"
echo "=================================="
echo ""

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed."
    echo "Please install Python 3.7 or higher and try again."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✓ Found Python $PYTHON_VERSION"

# Check for pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip is not installed."
    echo "Please install pip and try again."
    exit 1
fi

echo "✓ Found pip"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""

# Platform-specific setup
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Detected macOS"
    echo ""
    echo "⚠️  IMPORTANT: You need to grant permissions for TextCopy to work:"
    echo "1. Go to System Preferences → Security & Privacy → Privacy"
    echo "2. Add Terminal (or your Python) to 'Accessibility' and 'Input Monitoring'"
    echo ""
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Detected Linux"
    echo ""
    echo "Installing additional dependencies for Linux..."

    # Check for xdotool
    if ! command -v xdotool &> /dev/null; then
        echo "⚠️  xdotool is recommended for better source detection"
        echo "Install with: sudo apt-get install xdotool"
    else
        echo "✓ xdotool found"
    fi
fi

echo ""
echo "=================================="
echo "✓ Installation Complete!"
echo "=================================="
echo ""
echo "To start TextCopy, run:"
echo "  python3 src/textcopy.py"
echo ""
echo "Or use the launcher:"
echo "  python3 run.py"
echo ""
echo "For quick start guide, see QUICKSTART.md"
echo ""
