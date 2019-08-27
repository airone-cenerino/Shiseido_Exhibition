void setup() {
  Serial.begin(9600);
  PinSetUp();
  MotorSetUp();
}

void loop() {
  ButtonCheck();

  if (condition == DRAW) {
    MotorMove();

    // イテレータをずらす
    if (point == pictures[picture][line][0][0]) { // その線を引き終わった場合
      Serial.println("線引き終わった");

      if (line + 1 == lineNum[picture]) {         // その絵を描き終わった時
        Serial.println("絵描き終わった");
        picture = nextPicture;
        if (picture + 1 == picturesLen) {
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
    } else {
      point++;
    }
  }
}

void MotorMove() {
  if (pictures[picture][line][0][point] > 0) {
    L6470_move(1, pictures[picture][line][0][point]);
  } else {
    L6470_move(0, -pictures[picture][line][0][point]);
  }

  Serial.println(pictures[picture][line][0][point]);

  if (pictures[picture][line][1][point] > 0) {
    L6470_move2(1, pictures[picture][line][1][point]);
  } else {
    L6470_move2(0, -pictures[picture][line][1][point]);
  }
  L6470_busydelay(0);
  L6470_busydelay2(0);
}
