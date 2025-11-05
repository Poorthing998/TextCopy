# TextCopy Debugging Guide

If TextCopy isn't working as expected, follow this guide to diagnose and fix issues.

## Common Issue: Text Not Saving to Word Document

### Symptoms
- You see "Captured!" notification
- Text saves to `captures.txt` but NOT to `my_captures.docx`
- Word document is empty or not updating

### Quick Fix

**1. Run the test script first:**
```bash
python test_word.py
```

This will test if Word document creation is working and show detailed error messages.

**2. Check the log file:**
```bash
cat textcopy.log
```

Look for lines containing:
- `Error saving to Word:`
- `Failed to save to Word document`
- Stack traces with error details

**3. Common Causes:**

#### A. Missing python-docx library
**Error:** `ModuleNotFoundError: No module named 'docx'`

**Fix:**
```bash
pip install python-docx
```

#### B. Permission issues
**Error:** `PermissionError: [Errno 13] Permission denied`

**Fix:**
```bash
# Make sure captures directory is writable
chmod 777 captures/

# Or run with appropriate permissions
```

#### C. Word file is open in another program
**Error:** `PermissionError` when trying to save

**Fix:**
- Close the Word document in Microsoft Word, LibreOffice, etc.
- TextCopy can't write to a file that's open elsewhere

#### D. Corrupted Word file
**Fix:**
```bash
# Rename or delete the existing file
mv captures/my_captures.docx captures/my_captures.docx.backup

# TextCopy will create a new one
```

## Enable Detailed Logging

Edit `config.yaml`:

```yaml
log_level: "DEBUG"  # Change from "INFO" to "DEBUG"
```

Then check `textcopy.log` for detailed step-by-step logs.

## Test Word Document Functionality

Use the provided test script:

```bash
python test_word.py
```

This will:
1. Load configuration
2. Create a test capture
3. Save to Word document
4. Verify file exists and size
5. Test appending to existing document
6. Report any errors with full stack traces

## Manual Testing

### Test 1: Create a simple Word document

```python
from docx import Document

doc = Document()
doc.add_paragraph("Test")
doc.save("test.docx")
print("Success!")
```

If this fails, `python-docx` is not installed correctly.

### Test 2: Check if TextCopy can import modules

```python
import sys
sys.path.insert(0, 'src')

from config import Config
from capture import CapturedText
from storage import StorageManager

print("All imports successful!")
```

If this fails, there are import issues in the code.

## Check Configuration

### Verify output format
Check `config.yaml`:

```yaml
output_format: "both"  # Should be "both" or "word"
```

If set to `"txt"`, it will only save to text file!

### Verify file paths
Check `config.yaml`:

```yaml
output_directory: "captures"
word_file: "my_captures.docx"
```

Make sure the directory exists:
```bash
ls -la captures/
```

## View Full Error Details

When running TextCopy, errors are logged to both console and `textcopy.log`.

**Console output:**
```bash
python src/textcopy.py
# Watch for red error messages
```

**Log file:**
```bash
tail -f textcopy.log
# This shows real-time log updates
```

## Understanding Log Messages

### Success messages:
```
✓ Saved to Word document: captures/my_captures.docx
✓ Successfully captured and saved 42 characters
```

### Failure messages:
```
✗ Failed to save capture
Error saving to Word: [detailed error]
Failed to save to Word document
```

### Debug messages (when log_level="DEBUG"):
```
DEBUG - Word output path: captures/my_captures.docx
DEBUG - Loading existing Word document
DEBUG - Saving Word document to: captures/my_captures.docx
```

## Still Having Issues?

### 1. Clean installation

```bash
# Backup your captures
cp -r captures captures_backup

# Remove all generated files
rm -rf captures/*.docx captures/*.txt
rm textcopy.log

# Reinstall dependencies
pip uninstall -y python-docx pynput pyperclip PyYAML
pip install -r requirements.txt

# Test again
python test_word.py
```

### 2. Check Python version

```bash
python --version
```

Should be Python 3.7 or higher.

### 3. Check installed packages

```bash
pip list | grep -E "python-docx|pynput|pyperclip|PyYAML"
```

Should show:
- python-docx >= 1.1.0
- pynput >= 1.7.6
- pyperclip >= 1.8.2
- PyYAML >= 6.0.1

### 4. Platform-specific issues

**Windows:**
- Run Command Prompt as Administrator
- Check if antivirus is blocking file writes

**macOS:**
- Grant permissions in System Preferences → Security & Privacy
- Try running with `sudo` (for testing only)

**Linux:**
- Check file permissions: `ls -la captures/`
- Install missing dependencies: `sudo apt install python3-tk`

## Report a Bug

If none of these solutions work, please report the issue with:

1. **Operating System:** (Windows/macOS/Linux and version)
2. **Python Version:** `python --version`
3. **Error Message:** Copy from console or textcopy.log
4. **Test Script Output:** `python test_word.py`
5. **Configuration:** Your `config.yaml` file
6. **Steps to reproduce:** What you did when the error occurred

## Recent Fixes (v1.0.1)

- Fixed import error in storage.py (relative imports)
- Added detailed error logging with stack traces
- Improved error notifications
- Added test_word.py for diagnosing Word document issues
- Enhanced logging with DEBUG level support
- Better user feedback when saves fail

---

For general help, see [README.md](README.md) or [QUICKSTART.md](QUICKSTART.md)
