import logging

# Create logger

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a handler
handler = logging.StreamHandler()

# Set handler level
handler.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

# Attach formatter to handler
handler.setFormatter(formatter)

# Attach handler to logger
logger.addHandler(handler)

name=input("Enter your name: ")

# Log messages
logger.debug("Checking the %s input...", name)
logger.info("%s logged in successfully.", name)
logger.warning("%s has only 2 login attempts remaining.", name)
logger.error("Could not connect to database")
logger.critical("Database server is down")
