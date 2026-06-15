from shipment.logger import logging
from shipment.exception import shippingException
import sys

# logging.info('this is checking 2')

try:
    a = 1 / 0

except Exception as e:
    raise shippingException(e, sys) from e
