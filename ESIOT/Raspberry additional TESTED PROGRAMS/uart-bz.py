#!/usr/bin/env python
import urllib2,json
import time
import RPi.GPIO as GPIO
import serial

ser = serial.Serial(
        port='/dev/ttyS0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
buzzer = 38
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(buzzer,GPIO.OUT)
    GPIO.output(buzzer,False)
def main():
 setup()
 try:
  while True:
    try:
        x=ser.readline()
        print x
        if(x=='1'):
            GPIO.output(buzzer,True)
            print("high")
##        time.sleep(2)
        elif(x=='0'):
            GPIO.output(buzzer,False)
            print("low")
            time.sleep(2)
    except serial.SerialException:
        print("Serial read error")
 except KeyboardInterrupt:
    GPIO.cleanup() 
if __name__ == '__main__':
    main()
    