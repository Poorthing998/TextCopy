# TextCopy - SIMPLE Instructions

TextCopy has been **SIMPLIFIED** for reliability and ease of use.

## Quick Start

### 1. Run TextCopy
```cmd
python -m src
```

### 2. Capture Text
1. **Copy text** first with `Ctrl+C` (like normal)
2. Press `Ctrl+Alt+C` to save it
3. Done!

Your text is saved in `captures\my_captures.docx` with simple numbering:

```
1. First text you captured

2. Second text you captured

3. Third text...
```

## Hotkeys (NEW - Changed to avoid conflicts)

| Action | Hotkey |
|--------|--------|
| **Capture** | `Ctrl+Alt+C` |
| View captures | `Ctrl+Alt+V` |
| Pause/Resume | `Ctrl+Alt+P` |
| Exit | `Ctrl+Alt+Q` |

## How It Works (SIMPLIFIED)

1. Copy something with `Ctrl+C` (normal copy)
2. Press `Ctrl+Alt+C`
3. TextCopy reads your clipboard
4. Saves it to Word with a number (1. 2. 3. etc.)
5. Done!

## What's Different Now?

### ✅ SIMPLIFIED:
- **No timestamps** - just simple numbers
- **No source tracking** - keep it simple
- **No fancy formatting** - just text
- **No auto-copy** - you control when to copy
- **Less errors** - removed complex features

### ✅ FIXED:
- **New hotkey** `Ctrl+Alt+C` - avoids conflicts
- **No double-triggers** - added cooldown
- **Simpler saves** - less things to go wrong
- **Better error messages** - tells you what to do

## Troubleshooting

### "No text in clipboard"
**Solution:** Copy something with `Ctrl+C` BEFORE pressing `Ctrl+Alt+C`

### "Failed - Could not save"
**Solution:** Close `my_captures.docx` in Microsoft Word

### Hotkey not working
**Solution:** The new hotkey is `Ctrl+Alt+C` (not Ctrl+Shift+C anymore)

### Captured twice
**Solution:** Fixed! Now has 0.3 second cooldown to prevent double-triggers

## Example Workflow

```
1. Open a PDF or website
2. Select text you want to save
3. Press Ctrl+C (normal copy)
4. Press Ctrl+Alt+C (capture it)
5. See notification: "✓ Captured!"
6. Repeat for more text
7. Press Ctrl+Alt+V to view all captures
```

Your captures will look like:

```
1. First quote or text

2. Second quote or text

3. Third quote or text
```

Simple and clean!

## Configuration

If you want to change settings, edit `config.yaml`:

```yaml
# Change hotkey if needed
hotkey: "ctrl+alt+c"

# Only save to Word (no text file)
output_format: "word"

# Change Word file name
word_file: "my_notes.docx"
```

## Tips

1. **Always copy first** with `Ctrl+C`, then press `Ctrl+Alt+C`
2. **Close Word** before capturing if you have the file open
3. **Use Ctrl+Alt+V** to quickly view your captures
4. **Simple is better** - just numbered text, no fancy stuff

## What Was Removed (To Make It Work Better)

- ❌ Auto-copy feature (was causing issues)
- ❌ Timestamps (not needed, just use numbers)
- ❌ Source detection (too complex)
- ❌ Fancy separators (keep it simple)
- ❌ Duplicate detection (let user decide)
- ❌ Complex error handling (was hiding problems)

## Need Help?

Common issues:
- Copy text with `Ctrl+C` **first**, then press `Ctrl+Alt+C`
- Close Word file if you get "Failed" error
- Use the new hotkey `Ctrl+Alt+C` (changed from Ctrl+Shift+C)

---

**Remember:**
1. Copy with `Ctrl+C`
2. Capture with `Ctrl+Alt+C`
3. View with `Ctrl+Alt+V`

That's it! 🎉
