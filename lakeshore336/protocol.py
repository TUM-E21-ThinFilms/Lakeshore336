# Lakeshore336, (c) 2016, see AUTHORS. Licensed under the GNU GPL.

from slave.protocol import Protocol
import logging

class LakeShore336Protocol(Protocol):
    def __init__(self, terminal="\r\n", separator=',', encoding='ascii', logger=None):

        if logger is None:
            logger = logging.getLogger(__name__)
            logger.addHandler(logging.NullHandler())

        self.terminal = terminal
        self.separator = separator
        self.logger = logger
        self.encoding = encoding

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
        
