#include <Servo.h>

#define SERVO_PIN 38

void ServoSetUp() {
  Servo servo1;
  servo1.attach(SERVO_PIN);
}
