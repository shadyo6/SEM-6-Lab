// Add "AccelStepper-master" to the libary from git library link
#include <AccelStepper.h>
#define HALFSTEP 4

// Motor pin definitions
// Board pins P-29,P-31,P-7,P-33  
// Arduino pins 16, 17, 18, 19
// CN7-CN9 connected
#define motorPin1  13     // IN1 on the ULN2003 driver 1
#define motorPin2  12    // IN2 on the ULN2003 driver 1
#define motorPin3  11     // IN3 on the ULN2003 driver 1
#define motorPin4  10    // IN4 on the ULN2003 driver 1

// Initialize with pin sequence IN1-IN3-IN2-IN4 for using the AccelStepper with 28BYJ-48
AccelStepper stepper1(HALFSTEP, motorPin1, motorPin3, motorPin2, motorPin4);

void setup() {
 // stepper1.setMaxSpeed(1000.0);
 // stepper1.setAcceleration(1000.0);
 // stepper1.setSpeed(200);
  stepper1.moveTo(200);

}//--(end setup )---

void loop() {

  //Change direction when the stepper reaches the target position
  if (stepper1.distanceToGo() == 0) {
    stepper1.moveTo(-stepper1.currentPosition());
  }
  stepper1.run();
  delay(100);
}
