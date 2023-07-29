/*
*  Example 
* Xtrans Solutions Pvt Ltd
* www.xtranssolutions.com
* 
* Connect RM10 to RM1   //RTC Module
* Connect CN3 to CN6    //LCD Connection
* 
* Install ArduinoJson Library
*/
#include <Wire.h>
#include <TimeLib.h>
#include <DS1307RTC.h>
#include <LiquidCrystal.h>
const int rs = 6, en = 7, d4 =5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);


void setup() {
  Serial.begin(9600);
  while (!Serial) ; // wait for serial
  delay(200);
  lcd.begin(16,2);
//  setTime(hr,min,sec,day,month,yr);
  setTime(23,59,30,31,12,2019);
  RTC.set(now());
  Serial.println("DS1307RTC Read Test");
  Serial.println("-------------------");
}

void loop() {
  tmElements_t tm;

  if (RTC.read(tm)) {
    lcd.clear();
    Serial.print("Ok, Time = ");
    print2digits(tm.Hour);
    Serial.write(':');
    print2digits(tm.Minute);
    Serial.write(':');
    print2digits(tm.Second);
    Serial.print(", Date (D/M/Y) = ");
    Serial.print(tm.Day);
    Serial.write('/');
    Serial.print(tm.Month);
    Serial.write('/');
    Serial.print(tmYearToCalendar(tm.Year));
    Serial.println();
    lcd.setCursor(0,0);

    print2lcd(tm.Hour);
    lcd.print(":");
    print2lcd(tm.Minute);
    lcd.print(':');
    print2lcd(tm.Second);
    lcd.setCursor(0,1);
    print2lcd(tm.Day);
    lcd.print("/");
    print2lcd(tm.Month);
    lcd.print("/");
    lcd.print(tmYearToCalendar(tm.Year));
    } 
    else {
    if (RTC.chipPresent()) {
      Serial.println("The DS1307 is stopped.  Please run the SetTime");
      Serial.println("example to initialize the time and begin running.");
      Serial.println();
    } else {
      Serial.println("DS1307 read error!  Please check the circuitry.");
      Serial.println();
    }
    delay(9000);
  }
  delay(1000);
}

void print2digits(int number) {
  if (number >= 0 && number < 10) {
    Serial.write('0');
  }
  Serial.print(number);
  
}
void print2lcd(int number) {
  if (number >= 0 && number < 10) {
    lcd.print('0');
  }
  lcd.print(number);
  
}
