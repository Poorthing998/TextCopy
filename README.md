# TextCopy

A system-wide text capture tool that saves selected text to a document with a single hotkey press.

## Features

- 🔥 **One-Click Capture**: Press a hotkey to instantly save selected text
- 📄 **Multiple Formats**: Save to Word (.docx), plain text, or both
- ⏰ **Timestamped**: Each capture includes date and time
- 🎯 **Smart Organization**: Automatic categorization with source tracking
- ⚙️ **Customizable**: Configure hotkeys, output formats, and file locations
- 🖥️ **System-Wide**: Works with PDFs, browsers, eBooks, and any application

## How It Works

1. Select any text in any application
2. Press your configured hotkey (default: `Ctrl+Shift+C`)
3. Text is automatically copied and saved to your document
4. Continue reading/working without interruption

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone or download this repository:
```bash
git clone https://github.com/Poorthing998/TextCopy.git
cd TextCopy
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python src/textcopy.py
```

## Usage

### Basic Usage

1. Start TextCopy (choose one method):

   **Method 1 - Recommended (works on all platforms):**
   ```bash
   python -m src
   ```

   **Method 2 - Using launcher:**
   ```bash
   python run.py
   ```

   **Method 3 - Windows batch file:**
   ```cmd
   run.bat
   ```

   **Method 4 - Direct execution:**
   ```bash
   python src/textcopy.py
   ```

2. The application runs in the background (you'll see console messages)

3. Select text anywhere on your system and press `Ctrl+Shift+C`

4. Your text is saved to `captures/my_captures.docx` (default location)

### Configuration

Edit `config.yaml` to customize:

```yaml
hotkey: "ctrl+shift+c"           # Change the capture hotkey
output_format: "both"             # Options: "word", "txt", "both"
output_directory: "captures"      # Where to save files
word_file: "my_captures.docx"    # Word document name
text_file: "captures.txt"        # Text file name
include_timestamp: true           # Add timestamps to captures
include_source: true              # Try to detect source application
auto_categorize: false            # Group by date/source
```

### Advanced Features

#### Pause/Resume Capturing
Press `Ctrl+Shift+P` to pause/resume capturing (useful when you want to copy without saving)

#### View Recent Captures
Press `Ctrl+Shift+V` to open your captures document

#### Exit
Press `Ctrl+Shift+Q` or close the console/tray icon

## Output Format

### Word Document
Captures are formatted with:
- Heading with timestamp
- Source application (when detectable)
- Captured text with original formatting preserved
- Separator between captures

Example:
```
═══════════════════════════════════════
📅 Captured: 2025-11-05 14:32:15
📱 Source: Firefox Browser
───────────────────────────────────────
"Machine learning is a subset of artificial intelligence
that focuses on the development of algorithms..."
═══════════════════════════════════════
```

### Text File
Simple plain text format with timestamps:
```
[2025-11-05 14:32:15]
Machine learning is a subset of artificial intelligence...

[2025-11-05 14:35:42]
Another captured text...
```

## Platform Support

- ✅ **Windows**: Full support
- ✅ **macOS**: Full support (requires accessibility permissions)
- ✅ **Linux**: Full support (X11 and Wayland)

## Requirements

- `pynput`: For global hotkey detection
- `pyperclip`: For clipboard access
- `python-docx`: For Word document creation
- `pyyaml`: For configuration management
- `pygetwindow`: For source window detection (Windows)

## Troubleshooting

### Hotkey not working
- Check if another application is using the same hotkey
- Try changing the hotkey in `config.yaml`
- Run with administrator/sudo privileges if needed

### macOS: Permission denied
- Go to System Preferences → Security & Privacy → Privacy
- Add Terminal (or your Python) to "Accessibility" and "Input Monitoring"

### Linux: Missing dependencies
```bash
sudo apt-get install python3-tk python3-dev
```

## Tips

1. **Reading Research Papers**: Capture key quotes with `Ctrl+Shift+C` as you read
2. **Web Research**: Save important snippets from multiple tabs instantly
3. **eBook Reading**: Build your personal quote collection
4. **Code Snippets**: Quickly save code examples while learning

## License

MIT License - feel free to modify and distribute

## Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## Author

Created for efficient text collection and note-taking
