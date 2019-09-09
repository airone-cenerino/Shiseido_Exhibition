#include <Servo.h>

#define SERVO_PIN 38
#define SERVO_INITIAL_ANGLE 70
#define SERVO_RAISE_ANGLE 160

int nowAngle = 70;

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
  }
}

void ServoDown() {
  if (isServoUp) {
    servo1.write(SERVO_RAISE_ANGLE, SERVO_ROTATE_SPEED, true);
    isServoUp = false;
    delay(500);
  }
}
