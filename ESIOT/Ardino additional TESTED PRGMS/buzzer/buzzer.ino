/*
*  Example testing sketch to test Buzzer
*
* by Supreeth Kumar,
* Xtrans Solutions Pvt Ltd
* www.xtranssolutions.com
*
*/
//Define pin
// RM17 - RM9 connected 
int buzzer_pin = 9;     // Arduino pin #23/D9  or Board pin P38

void setup() 
{
  pinMode(buzzer_pin, OUTPUT);
  Serial.begin(9600);
  digitalWrite(buzzer_pin,HIGH);
}

void loop() {
  digitalWrite(buzzer_pin, LOW);
  delay(5000);
  digitalWrite(buzzer_pin, HIGH);
  delay(2000);
}
