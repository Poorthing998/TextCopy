# Changelog

All notable changes to TextCopy will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-05

### Initial Release

#### Added
- System-wide text capture with customizable hotkey
- Support for Windows, macOS, and Linux
- Multiple output formats (Word .docx, plain text, or both)
- Automatic timestamp for each capture
- Source application detection
- Configurable hotkeys for capture, pause, view, and exit
- Smart duplicate detection
- Automatic copy functionality (Ctrl+C before capture)
- Customizable Word document formatting
- Text file export as backup
- Configuration via YAML file
- Comprehensive logging system
- Pause/Resume functionality
- View captures with hotkey
- Session statistics
- Capture history tracking
- Beautiful formatting in Word documents with separators and metadata

#### Features
- **Hotkey Support**: Global hotkeys work from any application
- **Word Export**: Professional formatting with timestamps and source tracking
- **Text Export**: Simple plain text format for backup
- **Configuration**: Extensive customization via config.yaml
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Source Detection**: Automatically detects source window/application
- **Deduplication**: Avoids saving duplicate consecutive captures
- **Notifications**: Optional system notifications on capture (platform-dependent)
- **Auto-Copy**: Automatically triggers Ctrl+C before reading clipboard
- **Max Length**: Configurable maximum capture length with truncation
- **Session Stats**: Track captures, characters, and sources per session

#### Documentation
- Comprehensive README.md with full documentation
- Quick start guide (QUICKSTART.md)
- Contributing guidelines (CONTRIBUTING.md)
- Example configuration with detailed comments
- Platform-specific installation notes

#### Known Limitations
- Source detection requires platform-specific libraries
- Notifications may not work on all Linux distributions
- Some applications may not allow programmatic clipboard access
- Maximum 10,000 characters per capture by default (configurable)

## [Unreleased]

### Planned Features
- GUI/System tray interface
- Multiple capture collections/documents
- Search functionality
- Auto-categorization by source or date
- Export to additional formats (PDF, Markdown, HTML)
- Cloud sync integration
- OCR support for capturing text from images
- Browser extension integration
- Capture templates and formatting presets
- Statistics dashboard
- Tag support for organizing captures
- Keyboard shortcuts customization UI

### Planned Improvements
- Better source detection on Linux/Wayland
- Performance optimization for large documents
- Better error handling and recovery
- Installation package (pip installable)
- Auto-updater
- Unit tests and CI/CD
- Documentation website

---

## Version History

- **1.0.0** (2025-11-05) - Initial release with core functionality
