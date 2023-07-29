#include <SoftwareSerial.h>

#include<SerialESP8266wifi.h>
#include<ArduinoJson.h>
#include <Wire.h>
String rawData;
#define RX 2
#define TX 3
int countTrueCommand;
int countTimeCommand; 
boolean found = false; 
SoftwareSerial esp8266(RX,TX); 
StaticJsonBuffer<200> jsonBuffer;

void setup() 
{
  delay(3);
//  Serial.begin(9600);
//  esp8266.begin(9600);
//  sendCommand("AT",5,"OK");
//  sendCommand("AT+IPR = 115200",5,"OK");
//  sendCommand("AT+UART_DEF=115200,8,1,0,0",5,"OK");

  Serial.begin(115200);
  esp8266.begin(115200);
  sendCommand("AT",5,"OK");
  sendCommand("AT+IPR = 9600",5,"OK");
  sendCommand("AT+UART_DEF=9600,8,1,0,0",5,"OK");
}
void loop() {

} 
void sendCommand(String command, int maxTime, char readReplay[]) {
  Serial.print(countTrueCommand);
  Serial.print(". at command => ");
  Serial.print(command);
  Serial.print(" ");
  while(countTimeCommand < (maxTime*1))
  {
    esp8266.println(command);//at+cipsend
    if(esp8266.find(readReplay))//ok
    {
      found = true;
      break;
    }
  
    countTimeCommand++;
  }
  
  if(found == true)
  {
    Serial.println("OKK");
    countTrueCommand++;
    countTimeCommand = 0;
  }
  
  if(found == false)
  {
    Serial.println("Fail");
    countTrueCommand = 0;
    countTimeCommand = 0;
  }
  
  found = false;
 }
