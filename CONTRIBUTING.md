# Contributing to TextCopy

Thank you for your interest in contributing to TextCopy! This document provides guidelines and information for contributors.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your OS and Python version
- Relevant logs from `textcopy.log`

### Suggesting Features

Feature suggestions are welcome! Please:
- Check if the feature already exists or is planned
- Describe the use case and benefits
- Provide examples of how it would work

### Code Contributions

1. **Fork the repository**

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the existing code style
   - Add comments for complex logic
   - Update documentation if needed

4. **Test your changes**
   - Test on your platform
   - Verify existing functionality still works
   - Add new tests if applicable

5. **Commit your changes**
   ```bash
   git commit -m "Add: Brief description of your changes"
   ```

6. **Push and create a Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/TextCopy.git
cd TextCopy

# Install dependencies
pip install -r requirements.txt

# Install development dependencies (if any)
pip install pytest black flake8

# Run the app
python src/textcopy.py
```

## Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and concise

## Project Structure

```
TextCopy/
├── src/              # Source code
│   ├── textcopy.py   # Main application
│   ├── config.py     # Configuration management
│   ├── capture.py    # Text capture logic
│   └── storage.py    # Storage backends
├── config.yaml       # Configuration file
├── requirements.txt  # Dependencies
└── README.md         # Documentation
```

## Areas for Contribution

### High Priority
- Cross-platform testing and bug fixes
- Performance improvements
- Better source detection algorithms
- Additional export formats (PDF, Markdown, etc.)

### Medium Priority
- GUI/System tray interface
- Cloud sync integration
- OCR support for images
- Search functionality in captures

### Low Priority
- Themes and customization
- Statistics dashboard
- Browser extension integration
- Mobile companion app

## Testing

When adding features:
- Test on multiple platforms if possible
- Test with different applications (browser, PDF, etc.)
- Verify configuration changes work correctly
- Check edge cases (empty text, very long text, special characters)

## Documentation

If your contribution changes behavior:
- Update README.md
- Update QUICKSTART.md if it affects basic usage
- Add comments in config.yaml for new options
- Update docstrings in code

## Questions?

Feel free to:
- Open an issue for discussion
- Ask in pull request comments
- Contact maintainers

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for making TextCopy better!
