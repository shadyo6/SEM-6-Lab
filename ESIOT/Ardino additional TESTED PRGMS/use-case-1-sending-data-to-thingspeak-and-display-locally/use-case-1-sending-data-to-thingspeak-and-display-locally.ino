#include <SoftwareSerial.h>
#include <LiquidCrystal.h>
#include<SerialESP8266wifi.h>
#include<ThingSpeak.h>
#include<DHT.h>
#include<ArduinoJson.h>
#include <Wire.h>
String rawData;
#define RX 2
#define TX 3
const int rs = 16, en = 17, d4 =13, d5 = 12, d6 = 11, d7 = 10;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
#define DHTTYPE DHT11
#define dht_pin 4
#define light_pin 5
#define trig_pin 6
#define echo_pin 7
#define gas_pin A0
#define soil_pin A1
float temp = 0.0;
float humidity = 0.0;
int light = 1;
float distance = 0.0;
long duration;
int gas_value = 0;
int moisture_value = 0;

String AP = "TMi Phone";       // CHANGE ME
String PASS = "8B5637E4"; // CHANGE ME
String API = "QSLE1LS2MZERE6IB";   // CHANGE ME
String HOST = "api.thingspeak.com";
String PORT = "80";
int countTrueCommand;
int countTimeCommand; 
boolean found = false; 
SoftwareSerial esp8266(RX,TX); 
StaticJsonBuffer<200> jsonBuffer;
DHT dht(dht_pin,DHTTYPE);
void setup() 
{
  Serial.begin(115200);
  esp8266.begin(115200);
  sendCommand("AT",5,"OK");
  sendCommand("AT+IPR = 9600",5,"OK");
  sendCommand("AT+UART_DEF=9600,8,1,0,0",5,"OK");
  Serial.begin(9600);
  esp8266.begin(9600);
  lcd.begin(16, 2);
  lcd.print("welcome");
  //Serial.begin(9600);
  //esp8266.begin(9600);
  dht.begin();
  pinMode(light_pin,INPUT);
  pinMode(trig_pin,OUTPUT);
  pinMode(echo_pin,INPUT);
  pinMode(gas_pin,INPUT);
  pinMode(soil_pin,INPUT);
  //sendCommand("AT",5,"OK");
  //sendCommand("AT+IPR = 9600",5,"OK");
  //sendCommand("AT+UART_DEF=9600,8,1,0,0",5,"OK");
  sendCommand("AT",5,"OK");
  sendCommand("AT+CWMODE=1",5,"OK");
  sendCommand("AT+CWJAP=\""+ AP +"\",\""+ PASS +"\"",20,"OK");
}
void loop() {
  temp = dht.readTemperature();
  Serial.print("Temperature : ");
  Serial.println(temp);
  humidity = dht.readHumidity();
  Serial.print("Humidity : ");
  Serial.println(humidity);
  lcd.setCursor(0,0);
  lcd.print("T:");
  lcd.print(temp);
  lcd.print(" H:");
  lcd.print(humidity);
  light = digitalRead(light_pin);
  Serial.print("Light : ");
  Serial.println(light);
  digitalWrite(trig_pin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trig_pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig_pin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echo_pin, HIGH);
  // Calculating the distance
  distance= duration*0.034/2;
  Serial.print("Distance : ");
  Serial.print(distance);
  Serial.println(" cm");
  gas_value = analogRead(gas_pin);
  Serial.print("Gas Value : ");
  Serial.println(gas_value);
  lcd.setCursor(0,1);
  lcd.print("D:");
  lcd.print(distance);
  lcd.print(" G:");
  lcd.print(gas_value);
  moisture_value = analogRead(soil_pin);
  Serial.print("Moisture Level: ");
  Serial.println(moisture_value);
  String getData = "GET /update?api_key="+ API +"&field1="+temp+"&field2="+humidity+"&field3="+light+"&field4="+distance+"&field5="+gas_value+"&field6="+moisture_value;
  //String getData = "GET /channels/695467/fields/1/last.json?api_key=Z4Y31YEM9I2VUNBH";
  sendCommand("AT+CIPMUX=1",5,"OK");
  delay(1000);
  sendCommand("AT+CIPSTART=0,\"TCP\",\""+ HOST +"\","+ PORT,15,"OK");
  delay(1000);
  sendCommand("AT+CIPSEND=0," +String(getData.length()+4),4,">");
  delay(1000);
  esp8266.println(getData);
  delay(1500);
//  if(esp8266.available()>0)
//  {
//    Serial.println("OKKKKK");
//    rawData = esp8266.readString();
//    delay(2000);
//    Serial.println(rawData);
//    delay(1000);
//  }
  countTrueCommand++;
  sendCommand("AT+CIPCLOSE=0",5,"OK");
  Serial.println();
  Serial.println("Data sent to cloud Success");
  lcd.clear();
   
  
  
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
    Serial.println("OYI");
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
