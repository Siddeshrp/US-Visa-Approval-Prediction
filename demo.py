from US_visa.logger import logging
from US_visa.exception import USvisaException
import sys

try:
    a = 1 / "10"
except Exception as e:
    logging.info(e)
    raise USvisaException(e, sys) from e