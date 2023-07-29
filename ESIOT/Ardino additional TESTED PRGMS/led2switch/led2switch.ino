const int buttonPin1 = 13;     // number of pushbutton 1 pin
int buttonState1 = LOW;       // set the default variable value for pushbutton1 status
const int ledPin1 =  A5;       // number of the LED 1 pin
const int buttonPin2 = 12;     // number of pushbutton 2 pin
int buttonState2 = LOW;       // set the default variable value for pushbutton2 status
const int ledPin2 =  A4;       // number of the LED 2 pin
const int buttonPin3 = 11;     // number of pushbutton 3 pin
int buttonState3 = LOW;       // set the default variable value for pushbutton3 status
const int ledPin3 =  A3;       // number of the LED 3 pin
const int buttonPin4 = 10;     // number of pushbutton 4 pin
int buttonState4 = LOW;       // set the default variable value for pushbutton4 status
const int ledPin4 =  A2;       // number of the LED 4 pin


void setup() {                  // Set Pins to Outputs Or Inputs 
  pinMode(buttonPin1, INPUT);   // initialize the pushbutton pins as an inputs:
  pinMode(ledPin1, OUTPUT);     // initialize the LED pins as an outputs:
  pinMode(buttonPin2, INPUT);   // initialize the pushbutton pins as an inputs:
  pinMode(ledPin2, OUTPUT);     // initialize the LED pins as an outputs:
  pinMode(buttonPin3, INPUT);   // initialize the pushbutton pins as an inputs:
  pinMode(ledPin3, OUTPUT);     // initialize the LED pins as an outputs:
  pinMode(buttonPin4, INPUT);   // initialize the pushbutton pins as an inputs:
  pinMode(ledPin4, OUTPUT);     // initialize the LED pins as an outputs:
  Serial.begin(9600);           // initialize serial communication at 9600 baud
}

void loop() {                  

  buttonState1 = digitalRead(buttonPin1);  // read current states of the pushbutton value:
  buttonState2 = digitalRead(buttonPin2);  // read current states of the pushbutton value:
  buttonState3 = digitalRead(buttonPin3);  // read current states of the pushbutton value:
  buttonState4 = digitalRead(buttonPin4);  // read current states of the pushbutton value:

// check if the pushbutton is pressed buttonState# == HIGH/LOW
  // if pressed change buttonState == HIGH to turn on ledPin# 
  // else if buttonState == LOW then digitalWrite(ledPin#, LOW) Keeps Led off.

if (buttonState1 == HIGH) {    //check buttonState
digitalWrite(ledPin1, LOW);  //if HIGH turn LED on:
} else {
digitalWrite(ledPin1, HIGH);   // turn LED off:
}
Serial.println(buttonState1); //Print buttonState to serial
if (buttonState2 == HIGH) {   //check buttonState
digitalWrite(ledPin2, LOW);  //if HIGH turn LED on:
} else {
digitalWrite(ledPin2, HIGH);   // turn LED off:
delay(10);
}
Serial.println(buttonState2); //Print buttonState to serial
if (buttonState3 == HIGH) {   //check buttonState
digitalWrite(ledPin3, LOW);  //if HIGH turn LED on:
} else {
digitalWrite(ledPin3, HIGH);   // turn LED off:
delay(10);
Serial.println(buttonState3); //Print buttonState to serial
}
if (buttonState4 == HIGH) {   //check buttonState
digitalWrite(ledPin4, LOW);  //if HIGH turn LED on:
} else {
digitalWrite(ledPin4, HIGH);   // turn LED off:
delay(10);
Serial.println(buttonState4); //Print buttonState to serial
}
}
