"""
Application Configuration

This file contains all configurable values used by the application.
Keeping everything here avoids hardcoding values throughout the project.
"""


MODEL = "qwen3:8b"
#MODEL = "llama3.1:8b"

TEMPERATURE = 0

MAX_TOKENS = 4096

REQUEST_TIMEOUT = 60