#!/usr/bin/env python
import smbus
import time

i2c = smbus.SMBus(1)
addr=0x68
Vref=2.048

def swap16(x):
  return (((x << 8) & 0xFF00) | ((x >> 8) & 0x00FF))

def sign16(x):
  return ( -(x & 0b1000000000000000) | (x & 0b0111111111111111) )

def readval(x):
  i2c.write_byte(addr, x) #16bit
  time.sleep(0.2)
  data = i2c.read_word_data(addr,0x00)
  raw = swap16(int(hex(data),16))
  raw_s = sign16(int(hex(raw),16))
  volts = round((Vref * raw_s / 32767),5)
  return volts

if __name__=="__main__":
  volts1 = readval( 0b10011000 )
  volts2 = readval( 0b10111000 )
  volts3 = readval( 0b11011000 )
  volts4 = readval( 0b11111000 )
  out_msg = 'ch1:' + str(volts1) + ' ,ch2:' + str(volts2)+\
    ' ,ch3:' + str(volts3)+ ' ,ch4:' + str(volts4)
  print(out_msg)
