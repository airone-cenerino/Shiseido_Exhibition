void setup() {
  Serial.begin(9600);
  ButtonSetUp();
  DisplaySetUp();
  ServoSetUp();
  MotorSetUp();   
}

void loop() {
  ButtonCheck();

  if (condition == DRAW) {
    MotorMove();

    // イテレータをずらす
    if (point == pictures[picture][line][0][0]) { // その線を引き終わった場合
      if (line + 1 == lineNum[picture]) {         // その絵を描き終わった時
        Serial.println("絵描き終わった");
        picture = nextPicture;
        if (nextPicture + 1 == picturesLen) {
          nextPicture = 0;
        } else {
          nextPicture = picture + 1;
        }
        line = 0;
        point = 1;
        condition = STOP;
      } else {
        line++;
        point = 1;
      }
      
      DisplayUpdate();
    } else {
      point++;
    }
  }
}
