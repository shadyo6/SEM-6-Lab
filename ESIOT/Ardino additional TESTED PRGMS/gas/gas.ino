/*
*  Example testing sketch for Analog Gas sensor
*
* by Supreeth Kumar,
* Xtrans Solutions Pvt Ltd
* www.xtranssolutions.com
*
*/
//Define pin
// RM5 - RM22 connected 
int gas_pin = 0;     // Arduino pin #8/A0  or Board pin P11

void setup() {
  pinMode(gas_pin, INPUT);
  Serial.begin(9600);
}

void loop() {
  int gas_value = analogRead(gas_pin);

  Serial.print("Gas Value : ");
  Serial.println(gas_value);
  // Checks if it has reached the threshold value
  
  delay(1000);
}
