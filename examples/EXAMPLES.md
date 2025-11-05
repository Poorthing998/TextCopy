# TextCopy Examples

This directory contains examples of how TextCopy works and sample outputs.

## Example Workflow

### Scenario: Research Paper Reading

You're reading a PDF research paper and want to capture important quotes.

**Steps:**

1. Open your PDF in any reader (Adobe, Preview, Chrome, etc.)

2. Highlight this text:
   ```
   "Machine learning is a subset of artificial intelligence that focuses on
   the development of algorithms and statistical models."
   ```

3. Press `Ctrl+Shift+C`

4. Continue reading and highlight another passage:
   ```
   "Deep learning is a class of machine learning algorithms that uses
   multiple layers to progressively extract higher-level features."
   ```

5. Press `Ctrl+Shift+C` again

**Result:**

Your captures are saved to `captures/my_captures.docx` with formatting like:

```
═══════════════════════════════════════════════════════════════
📅 Captured: 2025-11-05 14:32:15
📱 Source: Adobe Acrobat Reader DC - paper.pdf
───────────────────────────────────────────────────────────────
"Machine learning is a subset of artificial intelligence that
focuses on the development of algorithms and statistical models."
═══════════════════════════════════════════════════════════════
📅 Captured: 2025-11-05 14:33:42
📱 Source: Adobe Acrobat Reader DC - paper.pdf
───────────────────────────────────────────────────────────────
"Deep learning is a class of machine learning algorithms that
uses multiple layers to progressively extract higher-level
features."
═══════════════════════════════════════════════════════════════
```

### Scenario: Web Research

Collecting information from multiple websites.

**Steps:**

1. Visit https://example.com/article1
2. Select important text: "The company was founded in 1998..."
3. Press `Ctrl+Shift+C`
4. Visit https://example.com/article2
5. Select more text: "Revenue increased by 45% in 2024..."
6. Press `Ctrl+Shift+C`

**Result:**

Captures from different sources are automatically organized:

```
═══════════════════════════════════════════════════════════════
📅 Captured: 2025-11-05 15:10:23
📱 Source: Article 1 - Mozilla Firefox
───────────────────────────────────────────────────────────────
The company was founded in 1998...
═══════════════════════════════════════════════════════════════
📅 Captured: 2025-11-05 15:12:05
📱 Source: Article 2 - Mozilla Firefox
───────────────────────────────────────────────────────────────
Revenue increased by 45% in 2024...
═══════════════════════════════════════════════════════════════
```

### Scenario: eBook Highlighting

Building a quote collection from books.

**Steps:**

1. Open your eBook in Kindle, Apple Books, or any reader
2. Highlight memorable quotes as you read
3. Press `Ctrl+Shift+C` after each highlight
4. Continue reading and capturing

**Result:**

All your favorite quotes in one document, perfect for:
- Book reviews
- Quote collections
- Reference materials
- Study notes

## Sample Outputs

### Word Document Format

The Word document (`my_captures.docx`) includes:

- **Professional formatting** with headers and separators
- **Timestamps** for each capture
- **Source tracking** (when available)
- **Easy navigation** with visual dividers
- **Customizable fonts** and styles

### Plain Text Format

The text file (`captures.txt`) provides:

- **Simple format** for easy parsing
- **Searchable content**
- **Backup** of all captures
- **Compatible** with any text editor

Example:
```
============================================================
[2025-11-05 14:32:15]
Source: Adobe Acrobat Reader DC - paper.pdf

Machine learning is a subset of artificial intelligence...

============================================================
[2025-11-05 14:33:42]
Source: Adobe Acrobat Reader DC - paper.pdf

Deep learning is a class of machine learning algorithms...

============================================================
```

## Advanced Examples

### Using Pause Mode

When you want to copy text without saving:

1. Press `Ctrl+Shift+P` to pause TextCopy
2. Copy text normally with `Ctrl+C`
3. Paste where needed
4. Press `Ctrl+Shift+P` again to resume capturing

### Custom Configuration

Edit `config.yaml` for specific use cases:

**For Academic Papers:**
```yaml
word_format:
  font_name: "Times New Roman"
  font_size: 12
include_source: true
include_timestamp: true
```

**For Quick Notes:**
```yaml
output_format: "txt"
include_timestamp: false
include_separator: false
```

**For Code Snippets:**
```yaml
word_format:
  font_name: "Courier New"
  font_size: 10
max_capture_length: 50000
```

## Tips and Tricks

1. **Organize by Project**: Create different config files for different projects
   ```bash
   python src/textcopy.py -c research_project.yaml
   ```

2. **Review Regularly**: Press `Ctrl+Shift+V` to quickly view your captures

3. **Export and Share**: Your captures are in standard formats (Word, TXT)

4. **Combine with Other Tools**: Import captures into note-taking apps

5. **Use Deduplication**: Enable `deduplicate: true` to avoid saving the same text twice

## Use Cases

- 📚 **Academic Research**: Collect quotes from papers and books
- 🌐 **Web Research**: Save information from multiple websites
- 📖 **eBook Reading**: Build personal quote collections
- 💻 **Code Learning**: Save code snippets while studying
- 📝 **Content Creation**: Gather references for writing
- 🎓 **Study Notes**: Capture important information while studying
- 📰 **News Reading**: Save articles and excerpts
- 🔍 **Comparison Shopping**: Capture product details from different sites

## Need More Examples?

Check out the main [README.md](../README.md) for detailed documentation and [QUICKSTART.md](../QUICKSTART.md) for a quick tutorial.
