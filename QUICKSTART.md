# TextCopy Quick Start Guide

Get started with TextCopy in 5 minutes!

## Installation

### 1. Install Python (if not already installed)

- **Windows**: Download from [python.org](https://python.org)
- **macOS**: `brew install python3` or download from python.org
- **Linux**: Usually pre-installed, or `sudo apt install python3 python3-pip`

### 2. Install TextCopy

```bash
# Clone or download the repository
git clone https://github.com/Poorthing998/TextCopy.git
cd TextCopy

# Install dependencies
pip install -r requirements.txt
```

### 3. Run TextCopy

```bash
python src/textcopy.py
```

That's it! TextCopy is now running in the background.

## First Capture

1. **Open any application** (browser, PDF reader, eBook app, etc.)

2. **Select some text** (drag to highlight)

3. **Press `Ctrl+Shift+C`** (or `Cmd+Shift+C` on macOS)

4. **Done!** Your text is saved to `captures/my_captures.docx`

## Viewing Your Captures

### Option 1: Use the View Hotkey
Press `Ctrl+Shift+V` to automatically open your captures document

### Option 2: Open Manually
Navigate to the `captures` folder and open:
- `my_captures.docx` (Word document with formatting)
- `captures.txt` (plain text backup)

## Common Use Cases

### Reading a Research Paper
```
1. Open PDF in your reader
2. Highlight important quotes
3. Press Ctrl+Shift+C for each quote
4. Open captures document to see all quotes with timestamps
```

### Web Research
```
1. Browse multiple articles/websites
2. Select key information from each
3. Press Ctrl+Shift+C to save
4. All captures saved in one document with source tracking
```

### Reading eBooks
```
1. Read in Kindle, Apple Books, or any eBook reader
2. Highlight passages you want to remember
3. Press Ctrl+Shift+C to save
4. Build your personal quote collection
```

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+C` | Capture selected text |
| `Ctrl+Shift+P` | Pause/Resume capturing |
| `Ctrl+Shift+V` | View captures document |
| `Ctrl+Shift+Q` | Exit TextCopy |

*On macOS, use `Cmd` instead of `Ctrl`*

## Customization

Edit `config.yaml` to customize:

```yaml
# Change the hotkey
hotkey: "ctrl+alt+c"

# Change output format
output_format: "word"  # or "txt" or "both"

# Change file names
word_file: "my_notes.docx"

# Disable timestamps
include_timestamp: false
```

## Platform-Specific Notes

### macOS
On first run, you'll need to grant permissions:
1. Go to **System Preferences** → **Security & Privacy** → **Privacy**
2. Add Terminal (or your Python) to **Accessibility** and **Input Monitoring**

### Linux
If hotkeys don't work, install `xdotool`:
```bash
sudo apt-get install xdotool
```

### Windows
No special setup required! Should work out of the box.

## Tips for Best Results

1. **Always select text first** before pressing the hotkey
2. **Use pause mode** (`Ctrl+Shift+P`) when you want to copy without saving
3. **Check your config.yaml** if something isn't working as expected
4. **Review captures regularly** to organize your collected information

## Troubleshooting

### "No text in clipboard" warning
- Make sure you **select** the text before pressing the hotkey
- Try enabling `auto_copy: true` in config.yaml

### Hotkey not responding
- Check if another app is using the same hotkey
- Try a different hotkey combination in config.yaml
- Run with admin/sudo privileges

### Import errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

## Next Steps

- Explore advanced configuration options in `config.yaml`
- Read the full README.md for detailed documentation
- Customize Word formatting options
- Set up auto-categorization for large projects

## Need Help?

- Check the full [README.md](README.md)
- Review [config.yaml](config.yaml) for all options
- Check the logs: `textcopy.log`

Happy capturing! 📝
