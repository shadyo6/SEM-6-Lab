# @Auth Xtrans Solutions Pvt. Ltd.
# Program to test Buzzer
# Connect RM9 to RM17

import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(38, gpio.OUT)

try:
    while(1):
        gpio.output(38,0)
        print("Buzzer OFF")
        time.sleep(1)
        gpio.output(38,1)
        print("Buzzer ON")
        time.sleep(1)
        #gpio.cleanup()
except KeyboardInterrupt:
        gpio.cleanup()
        exit
