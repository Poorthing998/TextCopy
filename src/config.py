"""
Configuration management for TextCopy
"""
import os
import yaml
import logging
from pathlib import Path
from typing import Dict, Any


class Config:
    """Configuration manager for TextCopy"""

    DEFAULT_CONFIG = {
        'hotkey': 'ctrl+shift+c',
        'pause_hotkey': 'ctrl+shift+p',
        'view_hotkey': 'ctrl+shift+v',
        'exit_hotkey': 'ctrl+shift+q',
        'output_format': 'both',
        'output_directory': 'captures',
        'word_file': 'my_captures.docx',
        'text_file': 'captures.txt',
        'include_timestamp': True,
        'include_source': True,
        'include_separator': True,
        'auto_categorize': False,
        'word_format': {
            'font_name': 'Calibri',
            'font_size': 11,
            'heading_size': 12,
            'add_page_break': False
        },
        'show_notifications': True,
        'notification_sound': False,
        'auto_copy': True,
        'copy_delay': 0.1,
        'max_capture_length': 10000,
        'deduplicate': True,
        'log_level': 'INFO',
        'log_file': 'textcopy.log'
    }

    def __init__(self, config_path: str = 'config.yaml'):
        """
        Initialize configuration

        Args:
            config_path: Path to configuration file
        """
        self.config_path = Path(config_path)
        self.config = self.DEFAULT_CONFIG.copy()
        self.load_config()
        self.setup_logging()

    def load_config(self) -> None:
        """Load configuration from YAML file"""
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r') as f:
                    user_config = yaml.safe_load(f)
                    if user_config:
                        self._update_nested_dict(self.config, user_config)
                logging.info(f"Configuration loaded from {self.config_path}")
            except Exception as e:
                logging.warning(f"Error loading config: {e}. Using defaults.")
        else:
            logging.info("Config file not found. Using default configuration.")
            self.save_config()

    def save_config(self) -> None:
        """Save current configuration to file"""
        try:
            with open(self.config_path, 'w') as f:
                yaml.dump(self.config, f, default_flow_style=False, sort_keys=False)
            logging.info(f"Configuration saved to {self.config_path}")
        except Exception as e:
            logging.error(f"Error saving config: {e}")

    def _update_nested_dict(self, base: Dict, update: Dict) -> None:
        """Recursively update nested dictionary"""
        for key, value in update.items():
            if isinstance(value, dict) and key in base and isinstance(base[key], dict):
                self._update_nested_dict(base[key], value)
            else:
                base[key] = value

    def setup_logging(self) -> None:
        """Setup logging based on configuration"""
        log_level = getattr(logging, self.config['log_level'].upper(), logging.INFO)
        log_file = self.config['log_file']

        logging.basicConfig(
            level=log_level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value

        Args:
            key: Configuration key (supports dot notation for nested keys)
            default: Default value if key not found

        Returns:
            Configuration value
        """
        keys = key.split('.')
        value = self.config

        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default

        return value

    def set(self, key: str, value: Any) -> None:
        """
        Set configuration value

        Args:
            key: Configuration key (supports dot notation for nested keys)
            value: Value to set
        """
        keys = key.split('.')
        config = self.config

        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]

        config[keys[-1]] = value

    def get_output_path(self, filename: str) -> Path:
        """
        Get full output path for a file

        Args:
            filename: Name of output file

        Returns:
            Full path to output file
        """
        output_dir = Path(self.config['output_directory'])
        output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir / filename

    def get_word_output_path(self) -> Path:
        """Get full path to Word output file"""
        return self.get_output_path(self.config['word_file'])

    def get_text_output_path(self) -> Path:
        """Get full path to text output file"""
        return self.get_output_path(self.config['text_file'])

    def __getitem__(self, key: str) -> Any:
        """Allow dictionary-style access"""
        return self.get(key)

    def __setitem__(self, key: str, value: Any) -> None:
        """Allow dictionary-style setting"""
        self.set(key, value)
