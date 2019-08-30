#include <Servo.h>

#define SERVO_PIN 38
#define SERVO_INITIAL_ANGLE 30
#define SERVO_RAISE_ANGLE 120

Servo servo1;
bool isServoUp = true;

void ServoSetUp() {
  servo1.attach(SERVO_PIN);
  ServoUp();
}

void ServoUp() {
  if (!isServoUp) {
    servo1.write(SERVO_INITIAL_ANGLE);
    isServoUp = true;
    delay(500);
  }

}

void ServoDown() {
  if (isServoUp) {
    servo1.write(SERVO_RAISE_ANGLE);
    isServoUp = false;
    delay(500);
  }
}
