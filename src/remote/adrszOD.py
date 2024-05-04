#!/usr/bin/env python
import smbus
import time

class I2C:
    i2c_bus = None
    def __init__(self, bus_number=1):
        cls = type(self)    # 旧スタイルなら、cls = self.__class__
        cls.i2c_bus = smbus.SMBus(bus_number) 

class TP401A(I2C):
    def __init__(self, address=0x68, Vref=2.048) -> None:
        super().__init__(bus_number=1)
        self.address = address
        self.Vref = Vref

    def swap16(self, x):
        return (((x << 8) & 0xFF00) |
            ((x >> 8) & 0x00FF))

    def sign16(self, x):
        return ( -(x & 0b1000000000000000) |
            (x & 0b0111111111111111) )

    def read_val(self, x):
        # self.変数名でのアクセス：インスタンス変数→クラス変数→親クラスのクラス変数の順に探索
        self.i2c_bus.write_byte(self.address, x) #16bit
        time.sleep(0.2)
        data = self.i2c_bus.read_word_data(self.address,0x00)
        raw = self.swap16(int(hex(data),16))
        raw_s = self.sign16(int(hex(raw),16))
        volts = round((self.Vref * raw_s / 32767),5)
        return volts

if __name__ == "__main__":
    smel = TP401A()
    volts1 = smel.read_val( 0b10011000 ) 
    volts2 = smel.read_val( 0b10111000 ) 
    volts3 = smel.read_val( 0b11011000 ) 
    volts4 = smel.read_val( 0b11111000 )
    out_msg = f"ch1:{volts1} , ch2:{volts2} , ch3:{volts3} , ch4:{volts4}" 
    print(out_msg)
