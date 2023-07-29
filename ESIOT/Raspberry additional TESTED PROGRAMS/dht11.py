# @Auth Xtrans Solutions Pvt. Ltd.
# Program to test DHT11 sensor
#Before executing this program intsall Adafruit_DHT11 Library using follwing command
#sudo apt-get install Adafruit_DHT11
import time
import Adafruit_DHT

#Set the type of sensor and the pin for sensor
sensor = Adafruit_DHT.DHT11
pin = 4


while(1):
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        print ("Humidity ="+str(humidity))
        print ("Temperature ="+str(temperature))
    except ValueError:
        print ("Unable to read data")

