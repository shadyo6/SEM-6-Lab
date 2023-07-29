# @Auth Xtrans Solutions Pvt. Ltd.
# Program to test light sensor

import RPi.GPIO as GPIO
import time

light = 33 #Board number

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(light,GPIO.IN)

def read_light():
    while True:
        light_state = GPIO.input(light)
        if light_state == 0:
            print("Light Detected")
        elif light_state == 1:
            print("Light Not Detected")
        
        time.sleep(.3)

def destroy():   #When program ending, the function is executed. 
    GPIO.cleanup()
    

if __name__ == '__main__': #Program starting from here 
    try:
        setup()
        read_light()
    except KeyboardInterrupt:  
        destroy()