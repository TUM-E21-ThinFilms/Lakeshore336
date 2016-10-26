# Lakeshore336, (c) 2016, see AUTHORS. Licensed under the GNU GPL.

from slave.driver import Driver, Command
from slave.types import Mapping, Float, String, Integer, Boolean, SingleType
from protocol import LakeShore336Protocol

class Empty(SingleType):
    def __convert__(self, value):
        return None

class LakeShore336Driver(Driver):

    def __init__(self, transport, protocol=None):
        if protocol is None:
            protocol = LakeShore336Protocol()
        
        self.thread = None
        
        super(LakeShore336Driver, self).__init__(transport, protocol)

    def query_command(self, cmd):
        return cmd.query(self._transport, self._protocol)

    def get_identification(self):
        cmd = Command(('*IDN?', [String, String, String, Float]))
        return self.query_command(cmd)
    
    def get_temperature(self, input_channel):
        input_channel = self.to_str_channel(input_channel)
        cmd = Command(('KRDG? ' + str(input_channel), Float))
        return self.query_command(cmd)
    
    def set_control_setpoint(self, channel, value):
        channel = self.to_int_channel(channel)
        cmd = Command(('SETP '+str(channel)+','+str(value)))
        return self.query_command(cmd)
                      
    def get_control_setpoint(self, channel):
        channel = self.to_int_channel(channel)
        cmd = Command(('SETP? '+str(channel), Float))
        return self.query_command(cmd)
    
    def set_pid(self, channel, p, i, d):
        channel = self.to_int_channel(channel)
        if channel > 2: 
            raise ValueError('Channel 1 or 2 are only allowed for PID values')
        
        cmd = Command(('PID '+str(channel)+','+str(p)+','+str(i)+','+str(d)))
        return self.query_command(cmd)
    
    def get_pid(self, channel):
        channel = self.to_int_channel(channel)
        cmd = Command(('PID? '+str(channel), [Float, Float, Float]))
        return self.query_command(cmd)
    
    def set_temperature_limit(self, channel, limit):
        channel = self.to_str_channel(channel)
        cmd = Command(('TLIMIT '+str(channel)+','+str(limit)))
        return self.query_command(cmd)
    
    def get_temperature_limit(self, channel):
        channel = self.to_str_channel(channel)
        cmd = Command(('TLIMIT? '+str(channel), Float))
        return self.query_command(cmd)
    
    def clear(self):
        self._write('*CLS')
    
    def operation_complete(self):
        self._write(('*OPC'))
    
    def is_operation_complete(self):
        cmd = Command(('*OPC?', Boolean))
        return self.query_command(cmd)
    
    def reset(self):
        self._write(('RST'))
    
    def set_alarm(self, channel, enabled, high, low, deadband, latch_enabled, audible, visible):
        channel = self.to_str_channel(channel)
        self._write('ALARM ' + ",".join([channel, str(enabled), str(high), str(low), str(deadband), str(latch_enabled), str(audible), str(visible)]))
                      
    def get_alarm(self, channel):
        channel = self.to_str_channel(channel)
        cmd = Command(('ALARM? ' + channel, [Boolean, Float, Float, Float, Boolean, Boolean, Boolean]))
        return self.query_command(cmd)
    
    def get_alarm_status(self, channel, high, low):
        channel = self.to_str_channel(channel)
        cmd = Command(('ALARMST? ' + channel, [Boolean, Boolean]))
        return self.query_command(cmd)
    
    def reset_alarm(self):
        self._write('ALMRST')
        
    def get_heater_output(self, channel):
        channel = self.to_int_channel(channel)
        cmd = Command(('HTR? ' + str(channel), Float))
        return self.query_command(cmd)
    
    def setup_heater(self, channel, resistance, max_current, max_user_current, display_current_or_power):
        self._write('HTRSET ' + ",".join([str(self.to_int_channel(channel)), str(resistance), str(max_user_current), str(display_current_or_power)]))
        
    def get_heater_config(self, channel):
        channel = str(self.to_int_channel(channel))
        cmd = Command(('HTRSET? ' + channel, [Integer, Integer, Float, Integer]))
        return self.query_command(cmd)
    
    def get_heater_status(self, channel):
        channel = str(self.to_int_channel(channel))
        cmd = Command(('HTRST? ' + channel, Integer))
        return self.query_command(cmd)
    
    def set_input_curve(self, channel, number):
        channel = self.to_str_channel(channel)
        self._write('INCRV ' + ",".join([channel, str(number)]))
        
    def get_input_curve(self, channel):
        cmd = Command(('INCRV? ' + self.to_str_channel(channel), Integer))
        return self.query_command(cmd)
    
    def set_input_name(self, channel, name):
        self._write('INNAME ' ",".join([self.to_str_channel(channel), str(name)]))
        
    def get_input_name(self, channel):
        cmd = Command(('INNAME? ' + self.to_str_channel(channel), String))
        return self.query_command(cmd)
    
    def set_led(self, enable):
        self._write('LEDS '+str(enalbe))
        
    def get_led(self):
        cmd = Command(('LEDS?', Boolean))
        return self.query_command(cmd)
    
    def set_ramp_setpoint(self, channel, enabled, rate):
        self._write('RAMP '+ ",".join([str(self.to_int_channel(channel)), str(enabled), str(rate)]))
                                       
    def get_ramp_setpoint(self, channel):
        cmd = Command(('RAMP? ' + str(self.to_int_channel(channel)), [Boolean, Float]))
        return self.query_command(cmd)
                                       
    def get_ramp_status(self, channel):
        cmd = Command(('RAMPST? ' + str(self.to_int_channel(channel)), Boolean))
        return self.query_command(cmd)
                                       
    def set_heater_range(self, channel, rng):
        self._write('RANGE ' + ",".join([str(self.to_int_channel(channel)), str(rng)]))
                                       
    def get_heater_range(self, channel):
        cmd = Command(('RANGE? ' + str(self.to_int_channel(channel)), Integer))
        return self.query_command(cmd)
                                       
    def get_temp(self):
        cmd = Command(('TEMP?', Float))
        return self.query_command(cmd)
                                       
    def set_warmup(self, channel, control, percentage):
        self._write('WARMUP ' + ",".join([str(self.to_int_channel(channel)), str(control), str(percentage)]))
                                       
    def get_warmup(self, channel):
        cmd = Command(('WARMUP? ' + str(self.to_int_channel(channel)), [Boolean, Float]))
        return self.query_command(cmd)
                                       
    def get_analog_output(self, channel):
        cmd = Command(('AOUT? ' + str(self.to_int_channel(channel)), Float))
        return self.query_command(cmd)
    
    
    def is_channel_str(self, channel):
        channel = str(channel).upper()
        return channel == 'A' or channel == 'B' or channel == 'C' or channel == 'D'
    
    def is_channel_int(self, channel):
        return isinstance( channel, (int, long)) and channel <= 4 and channel >= 1
        
    def channel_str_to_int(self, channel):
        switcher = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4
        }
        
        return switcher.get(channel.upper(), 1)
    
    def channel_int_to_str(self, channel):
        switcher = {
            1: 'A',
            2: 'B',
            3: 'C',
            4: 'D',
            '1': 'A',
            '2': 'B',
            '3': 'C',
            '4': 'D'
        }
        return switcher.get(channel, 'A')
    
    def to_int_channel(self, channel):
        if self.is_channel_int(channel):
            return channel
        else:
            return self.channel_str_to_int(channel)
        
    def to_str_channel(self, channel):
        if self.is_channel_str(channel):
            return channel.upper()
        else:
            return self.channel_int_to_str(channel)
