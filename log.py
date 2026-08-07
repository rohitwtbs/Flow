import logging
from  logging.handlers import RotatingFileHandler
logger = logging.getLogger("Driverlogger")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
console = logging.StreamHandler()
file = RotatingFileHandler("driver.log", maxBytes=1000000, backupCount=3)
logger.addHandler(console)
logger.addHandler(file)
logger.info("a bisc check of logging")
logger.debug("This won't print because level is set to INFO")
logger.warning("This is a warning message")
logger.error("This is an error message")
