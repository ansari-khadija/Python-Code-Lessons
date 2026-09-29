import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

# Create logger
logger = logging.getLogger(__name__)

# Get information from user
name = input("Enter your name: ")

# DEBUG
logger.debug("Checking the %s input...", name)

# INFO
logger.info("%s logged in successfully.", name)

# WARNING
logger.warning("%s has only 2 login attempts remaining.", name)

# ERROR
logger.error("Could not connect to the database.")

# CRITICAL
logger.critical("Database server is completely down!")
