// Example testing sketch for Digital light sensor

//Connect RM3 to RM20

int light_pin = 5;     //Arduino board pin #19 / D5

void setup() {
  pinMode(light_pin, INPUT);
  Serial.begin(9600);
}

void loop() {
  int light_data = digitalRead(light_pin);
  if(light_data)
    Serial.println("Light Not Detected!");
  else
    Serial.println("Light Detected!");
    
  delay(1000);
}
