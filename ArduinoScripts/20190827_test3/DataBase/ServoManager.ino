#include <Servo.h>

#define SERVO_PIN 38
#define SERVO_INITIAL_ANGLE 70
#define SERVO_RAISE_ANGLE 160

Servo servo1;
bool isServoUp = false;

void ServoManager_ServoSetUp() {
  servo1.attach(SERVO_PIN);
  ServoManager_ServoUp();
}

void ServoManager_ServoUp() {
  if (!isServoUp) {
    servo1.write(SERVO_INITIAL_ANGLE);
    isServoUp = true;
  }
}

void ServoManager_ServoDown() {
  if (isServoUp) {
    servo1.write(SERVO_RAISE_ANGLE);
    isServoUp = false;
    delay(500);
  }
}
