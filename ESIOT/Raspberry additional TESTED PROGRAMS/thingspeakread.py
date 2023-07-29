#!/usr/bin/env python
import urllib2,json
import time
import RPi.GPIO as GPIO
temp=0
led4 = 5    # pin is connected to LED and it should be OUT
led3 = 3     # pin is connected to LED and it should be OUT
led2 = 12     # pin is connected to LED and it should be OUT
led1 = 15   # pin is connected to LED and it should be OUT
READ_API_KEY='Z4Y31YEM9I2VUNBH'
CHANNEL_ID=695467
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
def main():
    
    conn = urllib2.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s"%(CHANNEL_ID,READ_API_KEY))
    response = conn.read()
    print "http status code=%s" % (conn.getcode())
    data=json.loads(response)
    temp = str(data['field1'])
    humi = str(data['field2'])
    
    print(temp)
    if(temp == "29.0"):
        GPIO.output(led1,0)
        time.sleep(10)
        print("Temperature too high")
    else:
        #GPIO.output(38,1)
        GPIO.output(led2,0)
        print("Temperarture is normal")
        time.sleep(5)
    conn.close()
    
if __name__ == '__main__':
    try:
     main()
    except KeyboardInterrupt:
     pass
    finally:
     GPIO.cleanup()
    
