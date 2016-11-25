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

import slave
import logging

from slave.protocol import Protocol
from slave.transport import Timeout


class LakeShore336Protocol(Protocol):
    def __init__(self, terminal="\r\n", separator=',', encoding='ascii', logger=None):

        if logger is None:
            logger = logging.getLogger(__name__)
            logger.addHandler(logging.NullHandler())

        self.terminal = terminal
        self.separator = separator
        self.logger = logger
        self.encoding = encoding

    def clear(self, transport):
        try:
            while True:
                transport.read_bytes(5)
        except slave.transport.Timeout:
            return

    def set_logger(self, logger):
        self.logger = logger

    def create_message(self, header, *data):
        msg = []
        msg.append(header)
        msg.extend(data)
        msg.append(self.terminal)
        return ''.join(msg).encode(self.encoding)    

    def parse_response(self, response, header):
        return response.decode(self.encoding).split(self.separator)         
    
    def query(self, transport, header, *data):
        message = self.create_message(header, *data)
        self.logger.debug('Query: %s', repr(message))
        with transport:
            transport.write(message)
            response = transport.read_until(self.terminal.encode(self.encoding))
        self.logger.debug('Response: %s', repr(response))
        return self.parse_response(response,header)

    def write(self, transport, header, *data):
        message = self.create_message(header, *data)
        self.logger.debug('Write: %s', repr(message))
        with transport:
            transport.write(message)
        
