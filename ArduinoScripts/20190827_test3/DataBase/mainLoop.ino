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
    if(point==1 || (line+1==lineNum[picture] && point == pictures[picture][line][0][0])){ // 最初の移動だった時
      ServoUp();
    }else{
      ServoDown();
    }
    
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
        SetCondition(STOP);
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

void SetCondition(int nextCondition){
  condition = nextCondition;

  if(condition == DRAW){
    digitalWrite(START_STOP_BUTTON_LAMP_PIN, LOW);
  }else{
    digitalWrite(START_STOP_BUTTON_LAMP_PIN, HIGH);
    ServoUp();
  }
}
