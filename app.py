from acneDetection.logger import logging
from acneDetection.exception import AcneException
import sys

try:
     x = 7/'9'
     
except Exception as e:
     raise AcneException(e, sys) from e