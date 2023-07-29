# @Auth Xtrans Solutions Pvt. Ltd.
# Program to test seven segment display
# Connect from RM1 to RM10
# Connect CN3 to CN6
import RPi.GPIO as GPIO
import lcdlib
import commands

GPIO.setmode(GPIO.BOARD)
#s=commands.getstatusoutput('sudo hwclock -w')
s=commands.getstatusoutput('sudo hwclock -r')
print(s[1][0:19])
lcdlib.lcd_init()
lcdlib.lcd_string(s[1][0:19],0x80)