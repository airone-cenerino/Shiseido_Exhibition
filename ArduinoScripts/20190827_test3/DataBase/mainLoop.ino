void setup() {
  Serial.begin(9600);
  ButtonManager_ButtonSetUp();
  DisPlayManager_DisplaySetUp();
  ServoManager_ServoSetUp();
  MotorManager_MotorSetUp();   
}

void loop() {
  DisPlayManager_loop();
  ButtonManager_ButtonCheck();

  if (condition == DRAW) {
    if(point==1 || (line+1==lineNum[picture] && point == pictures[picture][line][0][0])){ // 最初の移動だった時
      ServoManager_ServoUp();
    }else{
      ServoManager_ServoDown();
    }
    
    MotorManager_MotorMove();

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
        MainLoop_SetCondition(STOP);
      } else {
        line++;
        point = 1;
      }
      
      DisplayManager_DisplayUpdate();
    } else {
      point++;
    }
  }
}

void MainLoop_SetCondition(int nextCondition){
  condition = nextCondition;

  if(condition == DRAW){
    digitalWrite(START_STOP_BUTTON_LAMP_PIN, LOW);
  }else{
    digitalWrite(START_STOP_BUTTON_LAMP_PIN, HIGH);
    ServoManager_ServoUp();
  }
}
