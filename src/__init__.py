"""
TextCopy - System-wide text capture tool
"""

__version__ = '1.0.0'
__author__ = 'TextCopy Contributors'
__license__ = 'MIT'

from .config import Config
from .capture import TextCapture, CapturedText, CaptureHistory
from .storage import StorageManager
from .textcopy import TextCopyApp

__all__ = [
    'Config',
    'TextCapture',
    'CapturedText',
    'CaptureHistory',
    'StorageManager',
    'TextCopyApp'
]
