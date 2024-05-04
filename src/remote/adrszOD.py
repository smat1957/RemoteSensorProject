#!/usr/bin/env python
import smbus
import time

class I2C:
    bus_number = 1
    bus = smbus.SMBus(bus_number)

class TP401A(I2C):
    Vref=2.048

    def __init__(self, address=0x68) -> None:
        if address is not None:
            self.address = address
        else:
            self.address = 0x68

    def swap16(self, x):
        return (((x << 8) & 0xFF00) |
            ((x >> 8) & 0x00FF))

    def sign16(self, x):
        return ( -(x & 0b1000000000000000) |
            (x & 0b0111111111111111) )

    def read_val(self, x):
        I2C.bus.write_byte(self.address, x) #16bit
        time.sleep(0.2)
        data = I2C.bus.read_word_data(self.address,0x00)
        raw = self.swap16(int(hex(data),16))
        raw_s = self.sign16(int(hex(raw),16))
        volts = round((TP401A.Vref * raw_s / 32767),5)
        return volts

if __name__ == "__main__":
    smel = TP401A(0x68)
    volts1 = smel.read_val( 0b10011000 ) 
    volts2 = smel.read_val( 0b10111000 ) 
    volts3 = smel.read_val( 0b11011000 ) 
    volts4 = smel.read_val( 0b11111000 )
    out_msg = f"ch1:{volts1} , ch2:{volts2} , ch3:{volts3} , ch4:{volts4}" 
    print(out_msg)
