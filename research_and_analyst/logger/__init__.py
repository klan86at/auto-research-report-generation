# logger/__init__.py
from research_and_analyst.logger.custom_logger import CustomLogger
# Create a single shared logger instance
GLOBAL_LOGGER = CustomLogger().get_logger("research_and_analyst")