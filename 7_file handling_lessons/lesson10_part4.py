import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

logger = logging.getLogger(__name__)

try:
    # Take input from user
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    logger.info("User entered a=%s and b=%s", a, b)

    # Division
    result = a / b

    logger.info("Division successful")
    print("Result:", result)

except ZeroDivisionError:
    logger.error("Cannot divide by zero")
    print("Error: Cannot divide by zero")

except ValueError:
    logger.error("User entered invalid input")
    print("Error: Please enter numbers only")

finally:
    logger.info("Division program finished")
    print("Program finished")
