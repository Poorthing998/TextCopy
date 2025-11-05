"""
Text capture functionality for TextCopy
"""
import time
import logging
import pyperclip
import platform
from datetime import datetime
from typing import Optional, Dict, Any
from dataclasses import dataclass


@dataclass
class CapturedText:
    """Represents a captured text snippet"""
    text: str
    timestamp: datetime
    source: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


class TextCapture:
    """Handles text capture from clipboard and source detection"""

    def __init__(self, config):
        """
        Initialize TextCapture

        Args:
            config: Configuration object
        """
        self.config = config
        self.last_capture = None
        self.logger = logging.getLogger(__name__)

    def capture_text(self, auto_copy: bool = True) -> Optional[CapturedText]:
        """
        Capture text from clipboard

        Args:
            auto_copy: Whether to automatically trigger copy (Ctrl+C)

        Returns:
            CapturedText object or None if capture failed
        """
        try:
            # Auto-copy if enabled
            if auto_copy and self.config.get('auto_copy', True):
                self._trigger_copy()
                time.sleep(self.config.get('copy_delay', 0.1))

            # Get text from clipboard
            text = pyperclip.paste()

            if not text or not text.strip():
                self.logger.warning("No text in clipboard")
                return None

            # Check maximum length
            max_length = self.config.get('max_capture_length', 10000)
            if max_length > 0 and len(text) > max_length:
                self.logger.warning(f"Text too long ({len(text)} chars), truncating to {max_length}")
                text = text[:max_length] + "... [truncated]"

            # Check for duplicates
            if self.config.get('deduplicate', True) and self._is_duplicate(text):
                self.logger.info("Duplicate text detected, skipping")
                return None

            # Create capture object
            capture = CapturedText(
                text=text,
                timestamp=datetime.now(),
                source=self._detect_source() if self.config.get('include_source', True) else None
            )

            self.last_capture = capture
            self.logger.info(f"Captured {len(text)} characters from {capture.source or 'unknown source'}")

            return capture

        except Exception as e:
            self.logger.error(f"Error capturing text: {e}")
            return None

    def _trigger_copy(self) -> None:
        """Trigger system copy command (Ctrl+C)"""
        try:
            from pynput.keyboard import Controller, Key

            keyboard = Controller()

            # Press Ctrl+C
            keyboard.press(Key.ctrl)
            keyboard.press('c')
            keyboard.release('c')
            keyboard.release(Key.ctrl)

        except Exception as e:
            self.logger.debug(f"Could not trigger copy: {e}")

    def _is_duplicate(self, text: str) -> bool:
        """
        Check if text is duplicate of last capture

        Args:
            text: Text to check

        Returns:
            True if duplicate, False otherwise
        """
        if self.last_capture is None:
            return False

        # Compare stripped text to avoid whitespace differences
        return text.strip() == self.last_capture.text.strip()

    def _detect_source(self) -> Optional[str]:
        """
        Detect source application/window

        Returns:
            Source application name or None
        """
        try:
            system = platform.system()

            if system == "Windows":
                return self._detect_source_windows()
            elif system == "Darwin":  # macOS
                return self._detect_source_macos()
            elif system == "Linux":
                return self._detect_source_linux()
            else:
                return None

        except Exception as e:
            self.logger.debug(f"Could not detect source: {e}")
            return None

    def _detect_source_windows(self) -> Optional[str]:
        """Detect source on Windows"""
        try:
            import pygetwindow as gw

            # Get active window
            active_window = gw.getActiveWindow()
            if active_window:
                return active_window.title

        except ImportError:
            self.logger.debug("pygetwindow not available")
        except Exception as e:
            self.logger.debug(f"Error detecting Windows source: {e}")

        return None

    def _detect_source_macos(self) -> Optional[str]:
        """Detect source on macOS"""
        try:
            from AppKit import NSWorkspace

            active_app = NSWorkspace.sharedWorkspace().activeApplication()
            app_name = active_app['NSApplicationName']

            # Try to get window title (more complex on macOS)
            return app_name

        except ImportError:
            self.logger.debug("AppKit not available")
        except Exception as e:
            self.logger.debug(f"Error detecting macOS source: {e}")

        return None

    def _detect_source_linux(self) -> Optional[str]:
        """Detect source on Linux"""
        try:
            import subprocess

            # Try X11 first
            try:
                window_id = subprocess.check_output(
                    ['xdotool', 'getactivewindow'],
                    stderr=subprocess.DEVNULL
                ).decode().strip()

                window_name = subprocess.check_output(
                    ['xdotool', 'getwindowname', window_id],
                    stderr=subprocess.DEVNULL
                ).decode().strip()

                return window_name

            except (FileNotFoundError, subprocess.CalledProcessError):
                # Try Wayland with alternative methods
                pass

        except Exception as e:
            self.logger.debug(f"Error detecting Linux source: {e}")

        return None

    def clear_last_capture(self) -> None:
        """Clear last capture (useful for resetting duplicate detection)"""
        self.last_capture = None


class CaptureHistory:
    """Manages capture history and statistics"""

    def __init__(self):
        self.captures = []
        self.total_captures = 0
        self.total_characters = 0

    def add_capture(self, capture: CapturedText) -> None:
        """
        Add capture to history

        Args:
            capture: CapturedText object
        """
        self.captures.append(capture)
        self.total_captures += 1
        self.total_characters += len(capture.text)

    def get_recent(self, count: int = 10) -> list:
        """
        Get recent captures

        Args:
            count: Number of recent captures to return

        Returns:
            List of recent CapturedText objects
        """
        return self.captures[-count:]

    def get_statistics(self) -> Dict[str, Any]:
        """
        Get capture statistics

        Returns:
            Dictionary with statistics
        """
        sources = {}
        for capture in self.captures:
            if capture.source:
                sources[capture.source] = sources.get(capture.source, 0) + 1

        return {
            'total_captures': self.total_captures,
            'total_characters': self.total_characters,
            'unique_sources': len(sources),
            'top_sources': sorted(sources.items(), key=lambda x: x[1], reverse=True)[:5],
            'average_length': self.total_characters / self.total_captures if self.total_captures > 0 else 0
        }

    def clear(self) -> None:
        """Clear capture history"""
        self.captures.clear()
        self.total_captures = 0
        self.total_characters = 0
