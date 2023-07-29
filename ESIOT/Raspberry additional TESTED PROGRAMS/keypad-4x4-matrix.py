# @Auth Xtrans Solutions Pvt. Ltd.
# Program to test 4x4 Keypad Matrix
# Connect CN9 to CN5
#Before Execute the program install pad4pi library using following command
#sudo apt-get install pad4pi
import RPi.GPIO as GPIO
import time
from pad4pi import rpi_gpio

KEYPAD = [
        ["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]
]

ROW_PINS = [22,18,2,3] # BCM numbering  # board [24,19,21,23]
COL_PINS = [8,10,9,11]# BCM numbering    #board [15,12,3,5]

factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)


def printKey(key):
    print(key)
    time.sleep(0.2)

keypad.registerKeyPressHandler(printKey)

def destroy():   #When program ending, the function is executed. 
    GPIO.cleanup()
    

if __name__ == '__main__': #Program starting from here 
    try:
        while True:
            time.sleep(0.5)  
    except KeyboardInterrupt:  
            destroy()
    except :
        keypad.cleanup()