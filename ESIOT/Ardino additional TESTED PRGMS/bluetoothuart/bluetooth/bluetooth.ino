/*
*  Example sketch to test Bluetooth
*
* Xtrans Solutions Pvt Ltd
* www.xtranssolutions.com
* Connect RM18 to RM8
* 
* to check PIN use Command AT+PIN
*
*
* Download and Install "Serial Bluetooth Terminal" App from Android Phone(Play Store)
* Connect to HM10(Bluetooth LE) I.e. Open the app and go to Devices from menu and Connect to MLT-BT-05 under BLUETOOTH LE.
* Now you can send and receive messages from App to Aurduino Serial Monitor and vice versa
*/

#include<SoftwareSerial.h>

/* Create object named bt of the class SoftwareSerial */
SoftwareSerial bt(11,10); /* (Rx,Tx) */

void setup() {
  bt.begin(9600); /* Define baud rate for software serial communication */
  Serial.begin(9600); /* Define baud rate for serial communication */
}

void loop() {

    if (bt.available()) /* If data is available on serial port */
    {
     Serial.write(bt.read()); /* Print character received on to the serial monitor */
    }
    if(Serial.available())
    {
      bt.write(Serial.read());
    }
}
