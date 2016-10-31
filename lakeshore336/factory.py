# Copyright (C) 2016, see AUTHORS.md
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
