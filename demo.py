from shipment.logger import logging
from shipment.exception import shippingException
import sys
from shipment.utils.main_utils import MainUtils

# logging.info('this is checking 2')

# try:
#     a = 1 / 0

# except Exception as e:
#     raise shippingException(e, sys) from e

obj = MainUtils()

data = obj.read_yaml_file('config/model.yaml')

print(data)
