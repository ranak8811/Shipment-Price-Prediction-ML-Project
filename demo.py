from shipment.logger import logging
from shipment.exception import shippingException
import sys
from shipment.utils.main_utils import MainUtils
from shipment.constants import DB_URL
from shipment.configuration.mongo_operations import MongoDBOperation

# ------------------------> 1 <------------------------
# logging.info('this is checking 2')

# ------------------------> 2 <------------------------

# try:
#     a = 1 / 0

# except Exception as e:
#     raise shippingException(e, sys) from e

# ------------------------> 3 <------------------------

# obj = MainUtils()

# data = obj.read_yaml_file('config/model.yaml')

# print(data)

# ------------------------> 4 <------------------------

# print(DB_URL)

# ------------------------> 5 <------------------------

obj = MongoDBOperation()

df = obj.get_collection_as_dataframe(
    db_name='ShipmentDB', collection_name='shipment_collection')

print(df.head())
