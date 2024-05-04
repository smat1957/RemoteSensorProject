#!/usr/bin/env python
from adrszOD import TP401A

if __name__ == "__main__":
    smel = TP401A()
    volts1 = smel.read_val( 0b10011000 ) 
    volts2 = smel.read_val( 0b10111000 ) 
    volts3 = smel.read_val( 0b11011000 ) 
    volts4 = smel.read_val( 0b11111000 )
    out_msg = f"ch1:{volts1} ,ch2:{volts2},ch3:{volts3},ch4:{volts4}" 
    print(out_msg)
