# @Auth Xtrans Solutions Pvt. Ltd.
# Program to test LED and Switches
# Connect CN9 to CN4
# Dont forget to short the jumper pins
import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD) 

led4 = 5    # pin is connected to LED and it should be OUT
led3 = 3     # pin is connected to LED and it should be OUT
led2 = 12     # pin is connected to LED and it should be OUT
led1 = 15   # pin is connected to LED and it should be OUT
switch4 = 23  # pin is connected to SWITC and it should be IN
switch3 = 21  # pin is connected to SWITC and it should be IN
switch2 = 19  # pin is connected to SWITC and it should be IN
switch1= 24 # pin is connected to SWITC and it should be IN

gpio.setup(led1,gpio.OUT,initial=0)
gpio.setup(led2,gpio.OUT,initial=0)
gpio.setup(led3,gpio.OUT,initial=0)
gpio.setup(led4,gpio.OUT,initial=0)
gpio.setup(switch1,gpio.IN)
gpio.setup(switch2,gpio.IN)
gpio.setup(switch3,gpio.IN)
gpio.setup(switch4,gpio.IN)

def glow_led(event):
    if event == switch1 :
        gpio.output(led1, True)
        time.sleep(0.2)
        gpio.output(led1, False)
    
    elif event == switch2 :
        gpio.output(led2, True)
        time.sleep(0.2) 
        gpio.output(led2, False)
        
    
    elif event == switch3 :
        gpio.output(led3, True) 
        time.sleep(0.2)
        gpio.output(led3, False)
    
    elif event == switch4 :
        gpio.output(led4, True)
        time.sleep(0.2)
        gpio.output(led4, False)

gpio.add_event_detect(switch1, gpio.RISING , callback = glow_led, bouncetime = 1)
gpio.add_event_detect(switch2, gpio.RISING , callback = glow_led, bouncetime = 1)
gpio.add_event_detect(switch3, gpio.RISING , callback = glow_led, bouncetime = 1) 
gpio.add_event_detect(switch4, gpio.RISING , callback = glow_led, bouncetime = 1)

try:
    while(True):
    #to avoid 100% CPU usage
       time.sleep(1)
except KeyboardInterrupt:
    #cleanup GPIO settings before exiting
    gpio.cleanup()

