import RPi.GPIO as GPIO
import time
import math
import requests, json
import Adafruit_DHT as dht
import urllib2
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

myAPI = 'M37F81T4C543NP68' 
# URL where we will send the data, Don't change it
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

GPIO.setmode(GPIO.BCM)

GPIO.setup(13,GPIO.IN)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.IN)

sensor = dht.DHT11
dht11_pin = 4  # The Temperatur And Humiduty Sensor goes on digital port 2.
light_sensor_pin = 13
trig_pin = 19
echo_pin = 26


temp=0.0
humidity = 0.0
light_value = 0
distance = 0.0
duration = 0.0
gas_value = 0.0
moisture_value = 0.0

print("***********************")
print("")
print("IOT Development Kit")
print("")
print("***********************")
print("")
print("")


while True:
    try:
        #IR Snesor
        
        print("Scanning for sensors data....")
        time.sleep(2)
        print("---------------------")
        #print()
        humidity, temp = dht.read_retry(sensor, dht11_pin)
        
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            #print("Temparature and Humidity sensor value")
            print("------------------")
            print("Temparature = %.02f C"%(temp))
            print("------------------")
            print("Humidity = %.02f%%"%(humidity))
            print("------------------")
            
        light_value = GPIO.input(light_sensor_pin)
        if light_value==0 or light_value==1:    
            if light_value==0:
                print("------------------")
                print ('Light Detected')
                print("------------------")
            else:
                print("------------------")
                print ('Light Not Detected')
                print("------------------")
                
        GPIO.output(trig_pin, False)
        print("")
        print("------------------")
        #Set TRIG as LOW
        print "Waitng For Sensor To Settle"
        time.sleep(2)                            #Delay of 2 seconds
        print("------------------")
        GPIO.output(trig_pin, True)                  #Set TRIG as HIGH
        time.sleep(0.00001)                      #Delay of 0.00001 seconds
        GPIO.output(trig_pin, False)                 #Set TRIG as LOW

        while GPIO.input(echo_pin)==0:               #Check whether the ECHO is LOW
            pulse_start = time.time()              #Saves the last known time of LOW pulse

        while GPIO.input(echo_pin)==1:               #Check whether the ECHO is HIGH
            pulse_end = time.time()                #Saves the last known time of HIGH pulse 

        pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

        distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
        distance = round(distance, 2)            #Round to two decimal points

        if distance > 2 and distance < 400:      #Check whether the distance is within range
            print("------------------")
            print "Distance:",distance - 0.5,"cm"
            print("------------------")
        else:
            print("------------------")
            print "Out Of Range"
            print("------------------")
        gas_value = mcp.read_adc(0)
        moisture_value = mcp.read_adc(1)
        print("------------------")
        print("Gas Value : ")
        print("------------------")
        print(gas_value)
        print("------------------")
        print("soil Moisture Value : ")
        print("------------------")
        print(moisture_value)
        print("------------------")
        conn = urllib2.urlopen(baseURL + '&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s&field6=%s' % (temp, humidity,light_value,distance,gas_value,moisture_value))
        print("")
        print("------------------")
        print("Data Sent to cloud")
        print("------------------")
        print("")
        print("")
        time.sleep(5)
    except:
        print("exception")
        break
    
    
    
    
    
    
