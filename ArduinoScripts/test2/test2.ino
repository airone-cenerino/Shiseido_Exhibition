#include <Servo.h>
#define SERVO_PIN 38

Servo servo1;

void setup(){
  servo1.attach(38);
}

void loop(){
  servo1.write(30);
  delay(1000);
  servo1.write(120);
  delay(1000);
}
