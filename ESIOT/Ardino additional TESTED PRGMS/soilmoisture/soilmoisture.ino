/*
*  Example testing sketch for Analog Gas sensor
*
* by Supreeth Kumar,
* Xtrans Solutions Pvt Ltd
* www.xtranssolutions.com
*
*/
//Define pin
// RM6 - RM23 connected 
int soil_pin = 1;     // Arduino pin #9/A1  or Board pin P11

void setup() {
  pinMode(soil_pin, INPUT);
  Serial.begin(9600);
}

void loop() {
  int moisture_value = analogRead(soil_pin);

  Serial.print("Soil Moisture value : ");
  Serial.println(moisture_value);
  // Checks if it has reached the threshold value
  
  delay(1000);
}

