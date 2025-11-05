# Common Windows Issues - TextCopy

Quick solutions for common Windows-specific problems.

## ⚠️ Issue: "Permission denied" when saving Word document

### Error Message
```
PermissionError: [Errno 13] Permission denied: 'captures\my_captures.docx'
```

### Cause
The Word document file is **currently open** in Microsoft Word, LibreOffice, or another program.

### ✅ Quick Solution

**Close the Word document** and try again.

1. Close `my_captures.docx` in Word
2. Press `Ctrl+Shift+C` again to capture
3. It should work now

### 🔧 Automatic Solution (Built-in)

TextCopy now has **automatic backup** feature! If the main file is locked:

1. **First attempt**: Tries to save to `my_captures.docx`
2. **Second attempt**: If locked, saves to `my_captures_backup1.docx`
3. **Third attempt**: If still locked, saves to `my_captures_backup2.docx`

You'll see messages like:
```
WARNING - File is locked (attempt 1/3): captures\my_captures.docx
WARNING - This usually means the file is open in Word or another program
WARNING - Original file locked, trying: captures\my_captures_backup1.docx
✓ Saved to backup file: captures\my_captures_backup1.docx
⚠ Please close my_captures.docx and merge files manually
```

### 📝 After Using Backup Files

When you have backup files, you need to merge them:

1. **Close the main file** in Word
2. **Open `my_captures_backup1.docx`**
3. **Copy all content**
4. **Paste into `my_captures.docx`**
5. **Delete the backup file** (optional)

Or just keep using the backup file if you prefer!

### ⚙️ Disable Backup Feature

If you don't want automatic backups, edit `config.yaml`:

```yaml
use_backup_on_lock: false
```

Now TextCopy will just fail if the file is locked, forcing you to close it first.

## 🔄 Alternative: Use Text-Only Mode

If you keep having Word file locking issues, use text-only mode:

Edit `config.yaml`:
```yaml
output_format: "txt"  # Only save to captures.txt (no Word file)
```

Benefits:
- Text files don't get locked like Word files
- Faster saves
- Still captures everything with timestamps

Downsides:
- No formatting
- Harder to read
- No colors or fonts

## 🎯 Best Practices to Avoid This Issue

### Option 1: Keep Word Closed
- Don't open `my_captures.docx` while TextCopy is running
- Only open it to review after you're done capturing

### Option 2: Use View Hotkey
- Press `Ctrl+Shift+V` to view captures
- This opens it quickly
- Close it right after viewing

### Option 3: Use Separate Files
- Configure different Word file names for different sessions
- Example: `my_captures_morning.docx`, `my_captures_evening.docx`

Edit `config.yaml`:
```yaml
word_file: "captures_session1.docx"
```

### Option 4: Enable Auto-Backup
- Keep the default setting: `use_backup_on_lock: true`
- TextCopy will automatically use backup files
- Merge them later when convenient

## 🐛 Other Permission Errors

### Captures folder is read-only

**Error:**
```
Permission denied: 'captures'
```

**Solution:**
```cmd
# Make folder writable
attrib -r captures /s /d
```

Or:
1. Right-click `captures` folder
2. Properties → Uncheck "Read-only"
3. Apply to all files and subfolders

### Running from restricted location

**Problem:** TextCopy is in a protected folder (like `C:\Program Files`)

**Solution:** Move TextCopy to your Documents or user folder:
```cmd
# Example
mkdir %USERPROFILE%\TextCopy
move D:\Work\TextCopy\* %USERPROFILE%\TextCopy\
```

### Antivirus blocking

**Problem:** Antivirus blocks file writes

**Solution:**
1. Add TextCopy folder to antivirus exceptions
2. Or temporarily disable antivirus while testing

## 📊 Checking File Status

To see if a file is open:

### Using Task Manager:
1. Open Task Manager (`Ctrl+Shift+Esc`)
2. Go to "Details" tab
3. Right-click columns → Select "Command line"
4. Look for any program opening your .docx file

### Using Command Prompt:
```cmd
# See what has the file open
handle my_captures.docx

# If handle.exe not found, download from Microsoft Sysinternals
```

## 🔍 Debug Mode

Enable detailed logging to see exactly what's happening:

Edit `config.yaml`:
```yaml
log_level: "DEBUG"
```

Then check `textcopy.log` for detailed information:
```cmd
type textcopy.log
```

Look for:
- `DEBUG - Word output path: ...`
- `DEBUG - Loading existing Word document: ...`
- `DEBUG - Saving Word document to: ...`
- Any `PermissionError` messages

## ✅ Verify the Fix Works

After closing the Word file:

1. Run TextCopy: `python -m src`
2. Select some text
3. Press `Ctrl+Shift+C`
4. Check the log for: `✓ Saved to Word document`
5. No more permission errors!

## 📞 Still Having Issues?

If you still get permission errors after:
- ✅ Closing Word
- ✅ Checking file permissions
- ✅ Enabling backup mode

Then:
1. Check `textcopy.log` for detailed errors
2. See [DEBUGGING.md](DEBUGGING.md) for more help
3. Try text-only mode as workaround

---

**Quick Summary:**
- **Problem:** File is open in Word
- **Solution:** Close Word first
- **Auto-fix:** TextCopy uses backup files automatically
- **Alternative:** Use text-only mode
