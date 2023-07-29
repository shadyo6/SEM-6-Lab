# @Auth Xtrans Solutions Pvt. Ltd.
# Program to test seven segment display
# Connect from CN2 to CN8
import RPi.GPIO as GPIO
import time

SDI   = 21  #data  
RCLK  = 19  #Latch  
SRCLK = 24  #Clock  

segCode = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]
#,0x77,0x7c,0x39,0x5e,0x79,0x71

def print_msg():
    print ('Program is running...')
    print ('Please press Ctrl+C to end the program...')

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(SDI, GPIO.OUT)
    GPIO.setup(RCLK, GPIO.OUT)
    GPIO.setup(SRCLK, GPIO.OUT)
    GPIO.output(SDI, GPIO.LOW)
    GPIO.output(RCLK, GPIO.LOW)
    GPIO.output(SRCLK, GPIO.LOW)

def hc595_shift(dat):
        for bit in range(0,16):
            #print(hex(0x8080 & (dat << bit)))
            GPIO.output(SDI, 0x8000 & (dat << bit))
            GPIO.output(SRCLK, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(SRCLK, GPIO.LOW)
        GPIO.output(RCLK, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(RCLK, GPIO.LOW)
def loop():
    while True:
        for i in range(0, len(segCode)):
            for j in range(0, len(segCode)):
                            hc595_shift(segCode[j]<<8|segCode[i])
                            time.sleep(0.5)
            

def destroy():   #When program ending, the function is executed. 
    GPIO.cleanup()

if __name__ == '__main__': #Program starting from here 
    print_msg()
    setup() 
    try:
        loop()  
    except KeyboardInterrupt:  
        destroy()
