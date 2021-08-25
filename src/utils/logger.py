import logging.config
from os import path
import sys

logfilename = "%s/../cfg/logger.config" %path.dirname(path.abspath(__file__))
try:
    logging.config.fileConfig(fname=logfilename, disable_existing_loggers=False)
except Exception as e:
    print("Exception %s while trying to load logger config file from location %s" %(str(e), logfilename))
    sys.exit(1)

# Get the logger specified in the file
logger = logging.getLogger(__name__)