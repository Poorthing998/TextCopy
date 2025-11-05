#!/usr/bin/env python3
"""
TextCopy - System-wide text capture tool
Captures selected text with a hotkey and saves to documents
"""
import sys
import logging
import time
from pathlib import Path
from pynput import keyboard
from typing import Optional

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent))

from config import Config
from capture import TextCapture, CaptureHistory
from storage import StorageManager


class TextCopyApp:
    """Main TextCopy application"""

    def __init__(self, config_path: str = 'config.yaml'):
        """
        Initialize TextCopy application

        Args:
            config_path: Path to configuration file
        """
        self.config = Config(config_path)
        self.logger = logging.getLogger(__name__)

        self.capture_handler = TextCapture(self.config)
        self.storage = StorageManager(self.config)
        self.history = CaptureHistory()

        self.is_paused = False
        self.is_running = True
        self.listener: Optional[keyboard.GlobalHotKeys] = None

        self.logger.info("TextCopy initialized")

    def start(self) -> None:
        """Start the TextCopy application"""
        self.logger.info("=" * 60)
        self.logger.info("TextCopy - System-wide Text Capture Tool")
        self.logger.info("=" * 60)
        self.logger.info(f"Capture hotkey: {self.config['hotkey']}")
        self.logger.info(f"Pause/Resume: {self.config['pause_hotkey']}")
        self.logger.info(f"View captures: {self.config['view_hotkey']}")
        self.logger.info(f"Exit: {self.config['exit_hotkey']}")
        self.logger.info(f"Output format: {self.config['output_format']}")
        self.logger.info(f"Output directory: {self.config['output_directory']}")
        self.logger.info("=" * 60)
        self.logger.info("TextCopy is running. Press configured hotkeys to capture text.")
        self.logger.info("=" * 60)

        # Set up hotkeys
        hotkeys = {
            self._parse_hotkey(self.config['hotkey']): self.on_capture_hotkey,
            self._parse_hotkey(self.config['pause_hotkey']): self.on_pause_hotkey,
            self._parse_hotkey(self.config['view_hotkey']): self.on_view_hotkey,
            self._parse_hotkey(self.config['exit_hotkey']): self.on_exit_hotkey,
        }

        # Start listener
        self.listener = keyboard.GlobalHotKeys(hotkeys)
        self.listener.start()

        # Keep application running
        try:
            while self.is_running:
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.logger.info("\nReceived keyboard interrupt")
            self.stop()

    def stop(self) -> None:
        """Stop the TextCopy application"""
        self.logger.info("Stopping TextCopy...")

        if self.listener:
            self.listener.stop()

        # Print statistics
        stats = self.history.get_statistics()
        self.logger.info("=" * 60)
        self.logger.info("Session Statistics:")
        self.logger.info(f"  Total captures: {stats['total_captures']}")
        self.logger.info(f"  Total characters: {stats['total_characters']}")
        self.logger.info(f"  Average length: {stats['average_length']:.1f} chars")
        self.logger.info(f"  Unique sources: {stats['unique_sources']}")

        if stats['top_sources']:
            self.logger.info("  Top sources:")
            for source, count in stats['top_sources']:
                self.logger.info(f"    - {source}: {count} captures")

        self.logger.info("=" * 60)
        self.logger.info("TextCopy stopped. Goodbye!")

        self.is_running = False
        sys.exit(0)

    def on_capture_hotkey(self) -> None:
        """Handle capture hotkey press"""
        if self.is_paused:
            self.logger.info("Capture is paused. Press pause hotkey to resume.")
            return

        self.logger.info("Capture hotkey pressed!")

        # Capture text
        capture = self.capture_handler.capture_text()

        if capture:
            # Save to storage
            success = self.storage.save_capture(capture)

            if success:
                # Add to history
                self.history.add_capture(capture)

                # Show notification
                if self.config.get('show_notifications', True):
                    self._show_notification(
                        f"Captured {len(capture.text)} characters",
                        f"From: {capture.source or 'Unknown'}"
                    )

                self.logger.info(f"✓ Successfully captured and saved {len(capture.text)} characters")
            else:
                self.logger.error("✗ Failed to save capture")
        else:
            self.logger.warning("✗ No text captured")

    def on_pause_hotkey(self) -> None:
        """Handle pause/resume hotkey press"""
        self.is_paused = not self.is_paused

        if self.is_paused:
            self.logger.info("⏸  TextCopy PAUSED - captures disabled")
        else:
            self.logger.info("▶  TextCopy RESUMED - captures enabled")

    def on_view_hotkey(self) -> None:
        """Handle view captures hotkey press"""
        self.logger.info("Opening captures...")

        success = self.storage.open_captures()

        if not success:
            self.logger.error("Failed to open captures file")

    def on_exit_hotkey(self) -> None:
        """Handle exit hotkey press"""
        self.logger.info("Exit hotkey pressed")
        self.stop()

    def _parse_hotkey(self, hotkey_string: str) -> str:
        """
        Parse hotkey string to pynput format

        Args:
            hotkey_string: Hotkey string (e.g., "ctrl+shift+c")

        Returns:
            Formatted hotkey string for pynput
        """
        # pynput uses <ctrl>+<shift>+c format
        parts = hotkey_string.lower().split('+')
        formatted_parts = []

        for part in parts:
            part = part.strip()
            if part in ['ctrl', 'shift', 'alt', 'cmd']:
                formatted_parts.append(f'<{part}>')
            else:
                formatted_parts.append(part)

        return '+'.join(formatted_parts)

    def _show_notification(self, title: str, message: str) -> None:
        """
        Show system notification

        Args:
            title: Notification title
            message: Notification message
        """
        try:
            import platform

            system = platform.system()

            if system == "Windows":
                # Try Windows 10 notifications
                try:
                    from win10toast import ToastNotifier
                    toaster = ToastNotifier()
                    toaster.show_toast(title, message, duration=3, threaded=True)
                except ImportError:
                    self.logger.debug("win10toast not available")

            elif system == "Darwin":  # macOS
                import subprocess
                subprocess.run([
                    'osascript', '-e',
                    f'display notification "{message}" with title "{title}"'
                ])

            elif system == "Linux":
                import subprocess
                subprocess.run(['notify-send', title, message])

        except Exception as e:
            self.logger.debug(f"Could not show notification: {e}")


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description='TextCopy - System-wide text capture tool'
    )
    parser.add_argument(
        '-c', '--config',
        default='config.yaml',
        help='Path to configuration file (default: config.yaml)'
    )
    parser.add_argument(
        '--version',
        action='version',
        version='TextCopy 1.0.0'
    )

    args = parser.parse_args()

    try:
        app = TextCopyApp(config_path=args.config)
        app.start()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except Exception as e:
        logging.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
