# @Auth Xtrans Solutions Pvt. Ltd.
# Program to test Gas sensor
# Connect from RM22 to RM12
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import time

SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
 
while True :
	value1 = mcp.read_adc(0)
	print("Gas Value : ")
	print(value1)
	time.sleep(2)
        