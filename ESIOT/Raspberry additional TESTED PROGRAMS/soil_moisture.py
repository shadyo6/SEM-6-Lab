# @Auth Xtrans Solutions Pvt. Ltd.
# Program to test Moisture sensor
# Connect from RM23 to RM13
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import time

SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
 
while True :
	value = mcp.read_adc(1)
	print("Moisture Value : ")
	print(value)
	time.sleep(2)
        