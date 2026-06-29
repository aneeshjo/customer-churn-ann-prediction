"""
logger.py

This module configures the logging system for the entire project.

Features:
---------
- Creates a logs directory automatically.
- Creates a new log file for each execution.
- Logs messages with timestamps.
- Includes filename and line number.
"""

import logging
import os
from datetime import datetime
from pathlib import Path

# ------------------------------------------------------------------
# Create logs directory
# ------------------------------------------------------------------

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# ------------------------------------------------------------------
# Create log filename
# ------------------------------------------------------------------

LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

LOG_FILE_PATH = LOG_DIR / LOG_FILE

# ------------------------------------------------------------------
# Configure Logging
# ------------------------------------------------------------------

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s | %(filename)s:%(lineno)d | %(message)s"
)

# ------------------------------------------------------------------
# Logger Object
# ------------------------------------------------------------------

logger = logging.getLogger(__name__)