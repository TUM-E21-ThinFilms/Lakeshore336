# Lakeshore336, (c) 2016, see AUTHORS. Licensed under the GNU GPL.

from protocol import LakeShore336Protocol
from driver import LakeShore336Driver
from slave.transport import Serial
import logging

class LakeShore336Factory:

    def get_logger(self):
	logger = logging.getLogger('Lake Shore Model 336')
	logger.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	fh = logging.FileHandler('lakeshore336.log')
	fh.setLevel(logging.DEBUG)
	fh.setFormatter(formatter)
	logger.addHandler(fh)
	return logger
	
    def create_lakeshore(self, device='/dev/ttyUSB0', logger=None):
	if logger is None:
	    logger = self.get_logger()

        protocol = LakeShore336Protocol(logger=logger)
        return LakeShore336Driver(Serial(device, 57600, 7, 'O', 1, 0.05), protocol)
