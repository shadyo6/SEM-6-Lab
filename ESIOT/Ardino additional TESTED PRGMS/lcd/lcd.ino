/*
  LiquidCrystal Library - display() and noDisplay()
 Demonstrates the use a 16x2 LCD display.  The LiquidCrystal
 library works with all LCD displays that are compatible with the
 Hitachi HD44780 driver. There are many of them out there, and you
 can usually tell them by the 16-pin interface.
 This sketch prints "WELCOME TO ALS" in the first line of LCD
 and " BENGALURU - 58 "in the 2nd line of the LCD.
 The circuit:
 * LCD RS pin to digital pin 6
 * LCD Enable pin to digital pin 7
 * LCD D4 pin to digital pin 5
 * LCD D5 pin to digital pin 4
 * LCD D6 pin to digital pin 3
 * LCD D7 pin to digital pin 2
 * LCD R/W pin to ground
 * 10K resistor:
 * ends to +5V and ground
 * wiper to LCD VO pin (pin 3)
 Connect 10 pin frc cable from CN3 to CN6
*/
// include the library code:
#include <LiquidCrystal.h>

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 6, en = 7, d4 =5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print(" WELCOME TO ALS ");
  lcd.setCursor(0,1);
  lcd.print(" BENGALURU - 58 ");
}

void loop() {
  // Turn off the display:
 lcd.noDisplay();
 // delay(500);
  // Turn on the display:
  lcd.display();
  delay(5000);
}
