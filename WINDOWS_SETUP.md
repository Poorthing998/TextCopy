# TextCopy Setup Guide for Windows

Step-by-step instructions for setting up TextCopy on Windows.

## Prerequisites

### 1. Install Python

1. Download Python from [python.org](https://www.python.org/downloads/)
2. **IMPORTANT:** Check "Add Python to PATH" during installation
3. Click "Install Now"

### 2. Verify Python Installation

Open Command Prompt (cmd) or PowerShell and run:

```cmd
python --version
```

Should show: `Python 3.7` or higher

```cmd
pip --version
```

Should show pip version information

## Installation Steps

### Step 1: Download TextCopy

**Option A: Using Git**
```cmd
git clone <YOUR_REPO_URL> TextCopy
cd TextCopy
git checkout claude/refactor-textcopy-codebase-011CUq4VGC4y3eVJQDmQeRFm
```

**Option B: Download ZIP**
1. Download the repository as ZIP
2. Extract to a folder (e.g., `D:\Work\TextCopy`)
3. Open Command Prompt in that folder

### Step 2: Install Dependencies

```cmd
pip install -r requirements.txt
```

**Expected output:**
```
Collecting pynput>=1.7.6
Collecting pyperclip>=1.8.2
Collecting python-docx>=1.1.0
Collecting PyYAML>=6.0.1
...
Successfully installed ...
```

### Step 3: Test Installation

**Test 1: Simple Word Document Test**
```cmd
python test_simple.py
```

This tests if `python-docx` is working. Should show:
```
══════════════════════════════════════════════════════════
Simple Word Document Test
══════════════════════════════════════════════════════════

1. Testing python-docx import...
   ✓ python-docx imported successfully
2. Creating a test Word document...
   ✓ Document object created
...
✓ All tests passed!
```

**Test 2: Full TextCopy Test**
```cmd
python test_word.py
```

This tests the full TextCopy Word functionality.

## Running TextCopy

### Method 1: Using the launcher
```cmd
python run.py
```

### Method 2: Direct execution
```cmd
python src\textcopy.py
```

### Method 3: Using the install script
```cmd
install.bat
```

## Usage

1. **Start TextCopy:**
   ```cmd
   python run.py
   ```

2. You'll see:
   ```
   ══════════════════════════════════════════════════════════
   TextCopy - System-wide Text Capture Tool
   ══════════════════════════════════════════════════════════
   Capture hotkey: ctrl+shift+c
   ...
   TextCopy is running. Press configured hotkeys to capture text.
   ```

3. **Capture text:**
   - Select any text in any application
   - Press `Ctrl+Shift+C`
   - Text is saved to `captures\my_captures.docx`

4. **View captures:**
   - Press `Ctrl+Shift+V` to open the document
   - Or manually open: `captures\my_captures.docx`

5. **Exit:**
   - Press `Ctrl+Shift+Q`
   - Or press `Ctrl+C` in the command prompt

## Troubleshooting

### "python is not recognized"

**Problem:** Python not in PATH

**Fix:**
1. Reinstall Python and check "Add Python to PATH"
2. Or manually add Python to PATH:
   - Search for "Environment Variables" in Windows
   - Edit PATH variable
   - Add Python installation folder (e.g., `C:\Python39`)

### "No module named 'docx'"

**Problem:** python-docx not installed

**Fix:**
```cmd
pip install python-docx
```

### "Permission denied" errors

**Problem:** Running without administrator rights

**Fix:**
1. Right-click Command Prompt
2. Select "Run as administrator"
3. Navigate to TextCopy folder
4. Run commands again

### Import errors when running test_word.py

**Problem:** Python module import issues

**Fix:** Run the simple test first:
```cmd
python test_simple.py
```

If that works but `test_word.py` fails, the issue is with imports, not with python-docx.

### Word document not opening

**Problem:** No default application for .docx files

**Fix:**
1. Install Microsoft Word, or
2. Install LibreOffice (free), or
3. Manually open the file from File Explorer

### Text only saves to captures.txt, not to .docx

**Problem:** Word saving is failing

**Fix:**
1. Check `textcopy.log` for errors
2. Run `python test_word.py` to diagnose
3. See [DEBUGGING.md](DEBUGGING.md) for detailed help

### Antivirus blocking

**Problem:** Antivirus blocks keyboard monitoring

**Fix:**
1. Add TextCopy folder to antivirus exceptions
2. Or temporarily disable antivirus while running

## File Locations

- **Configuration:** `config.yaml`
- **Captures:** `captures\my_captures.docx` and `captures.txt`
- **Logs:** `textcopy.log`
- **Source code:** `src\` folder

## Customization

Edit `config.yaml` to change:

```yaml
# Change hotkey
hotkey: "ctrl+alt+c"

# Change output format
output_format: "word"  # or "txt" or "both"

# Change file names
word_file: "my_notes.docx"

# Disable timestamps
include_timestamp: false
```

## Running on Startup (Optional)

To run TextCopy automatically when Windows starts:

### Method 1: Startup Folder
1. Press `Win+R`, type `shell:startup`, press Enter
2. Create a shortcut to `run.py` in this folder
3. Right-click shortcut → Properties
4. Set "Target" to: `C:\Python39\python.exe D:\Work\TextCopy\run.py`
5. Set "Start in" to: `D:\Work\TextCopy`

### Method 2: Task Scheduler
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger: "At log on"
4. Action: "Start a program"
5. Program: Path to python.exe
6. Arguments: Full path to run.py

## Uninstallation

```cmd
# Uninstall Python packages
pip uninstall pynput pyperclip python-docx PyYAML

# Delete TextCopy folder
rd /s /q D:\Work\TextCopy
```

## Need More Help?

- See [README.md](README.md) for full documentation
- See [QUICKSTART.md](QUICKSTART.md) for quick tutorial
- See [DEBUGGING.md](DEBUGGING.md) for troubleshooting
- Check `textcopy.log` for error details

## Quick Reference

| Action | Command |
|--------|---------|
| Install dependencies | `pip install -r requirements.txt` |
| Test installation | `python test_simple.py` |
| Run TextCopy | `python run.py` |
| Capture text | Select text + `Ctrl+Shift+C` |
| View captures | `Ctrl+Shift+V` |
| Pause/Resume | `Ctrl+Shift+P` |
| Exit | `Ctrl+Shift+Q` |

---

**Happy capturing!** 📝
