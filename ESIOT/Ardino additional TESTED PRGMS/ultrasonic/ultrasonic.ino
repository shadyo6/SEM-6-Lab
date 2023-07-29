/*
* Ultrasonic Sensor HC-SR04 and Arduino Tutorial
*
* by Supreeth Kumar,
* Xtrans Solutions Pvt Ltd
* www.xtranssolutions.com
*
*/
// defines pins numbers
//RM4 and RM21 connected
const int trigPin = 6;   //trig Arduino pin 21/D7   or Board pi 37
const int echoPin = 7;   //Echo Arduino pin 20/D6   or Board pi 35
// defines variables
long duration;
int distance;

void setup() {
    pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
    pinMode(echoPin, INPUT); // Sets the echoPin as an Input
    Serial.begin(9600); // Starts the serial communication
}

void loop() {
    // Clears the trigPin
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    // Sets the trigPin on HIGH state for 10 micro seconds
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    // Reads the echoPin, returns the sound wave travel time in microseconds
    duration = pulseIn(echoPin, HIGH);// duration is in terms of time
    // Calculating the distance
    distance= duration*0.034/2;
    // Prints the distance on the Serial Monitor
    Serial.print("Smaple Distance: ");
    Serial.println(distance);
    delay(1000);
}
