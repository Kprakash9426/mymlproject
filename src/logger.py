import logging
import os
from datetime import datetime

# Create the log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the log directory path
logs_path = os.path.join(os.getcwd(), "logs")  # Corrected os.getcwd() usage
os.makedirs(logs_path, exist_ok=True)

# Complete log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Set up the logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s-%(levelname)s-%(message)s",  # Added missing comma
    level=logging.INFO
)

# Test logging
if __name__ == "__main__":
    logging.info("Logging has started")
