// Pin番号----------------------------
#define INITIALIZE_BUTTON_PIN 45
#define START_STOP_BUTTON_PIN 42
#define RESTART_BUTTON_PIN 44
#define SELECT_BUTTON_PIN 43
#define INITIALIZE_BUTTON_LAMP_PIN 25
#define START_STOP_BUTTON_LAMP_PIN 22
#define RESTART_BUTTON_LAMP_PIN 24
#define SELECT_BUTTON_LAMP_PIN 23

bool initialButtonCondition = false;
bool startStopButtonCondition = false;
bool restartButtonCondition = false;
bool selectButtonCondition = false;


void ButtonManager_ButtonSetUp() {
  pinMode(INITIALIZE_BUTTON_PIN, INPUT);
  pinMode(START_STOP_BUTTON_PIN, INPUT);
  pinMode(RESTART_BUTTON_PIN, INPUT);
  pinMode(SELECT_BUTTON_PIN, INPUT);
  pinMode(INITIALIZE_BUTTON_LAMP_PIN, OUTPUT);
  pinMode(START_STOP_BUTTON_LAMP_PIN, OUTPUT);
  pinMode(RESTART_BUTTON_LAMP_PIN, OUTPUT);
  pinMode(SELECT_BUTTON_LAMP_PIN, OUTPUT);
  pinMode(13, OUTPUT);

  // ボタンのLEDの消灯
  digitalWrite(22, HIGH);
  digitalWrite(23, HIGH);
  digitalWrite(24, HIGH);
  digitalWrite(25, HIGH);
}

void ButtonManager_ButtonCheck() {
  if (digitalRead(INITIALIZE_BUTTON_PIN) == 0) {
    if (!initialButtonCondition) {
      ButtonManager_InitializeButtonDown();
      initialButtonCondition = true;
    }
  } else {
    initialButtonCondition = false;
  }

  if (digitalRead(START_STOP_BUTTON_PIN) == 0) {
    if (!startStopButtonCondition) {
      ButtonManager_StartStopButtonDown();
      startStopButtonCondition = true;
    }
  } else {
    startStopButtonCondition = false;
  }

  if (digitalRead(RESTART_BUTTON_PIN) == 0) {
    if (!restartButtonCondition) {
      ButtonManager_RestartButtonDown();
      restartButtonCondition = true;
    }
  } else {
    restartButtonCondition = false;
  }

  if (digitalRead(SELECT_BUTTON_PIN) == 0) {
    if (!selectButtonCondition) {
      ButtonManager_SelectButtonDown();
      selectButtonCondition = true;
    }
  } else {
    selectButtonCondition = false;
  }
}



void ButtonManager_InitializeButtonDown() {
  if (condition == STOP) {
    digitalWrite(INITIALIZE_BUTTON_LAMP_PIN, LOW);
    MotorManager_InitializeMotorMove();
    digitalWrite(INITIALIZE_BUTTON_LAMP_PIN, HIGH);
  }
}

void ButtonManager_StartStopButtonDown() {
  Serial.println("スタート/ストップボタンが押されました。");
  switch (condition) {
    case DRAW:
      ServoManager_ServoUp();
      TimeKeeper_SetPauseStartTime();    
      MainLoop_SetCondition(STOP);
      break;
    case STOP:
      if(line == 0 && point == 1){
        TimeKeeper_ResetTime();
      }else{
        TimeKeeper_RestartReviseStartTime();
      }
      
      ServoManager_ServoDown();
      MainLoop_SetCondition(DRAW);
      break;
  }

  delay(500);
}

void ButtonManager_RestartButtonDown() {
  Serial.println("リスタートボタンが押されました。");

  // 次に描く絵を最初から描き始める
  picture = nextPicture;
  if (nextPicture + 1 == picturesLen) {
    nextPicture = 0;
    Serial.println("test");
  } else {
    nextPicture = picture + 1;
  }
  line = 0;
  point = 1;
  MainLoop_SetCondition(DRAW);
  TimeKeeper_ResetTime();

  digitalWrite(RESTART_BUTTON_LAMP_PIN, LOW);
  DisplayManager_DisplayUpdate();
  delay(500);
  digitalWrite(RESTART_BUTTON_LAMP_PIN, HIGH);
}

void ButtonManager_SelectButtonDown() {
  if (nextPicture + 1 == picturesLen) {
    nextPicture = 0;
  } else {
    nextPicture = nextPicture + 1;
  }

  digitalWrite(SELECT_BUTTON_LAMP_PIN, LOW);
  DisplayManager_DisplayUpdate();
  delay(500);
  digitalWrite(SELECT_BUTTON_LAMP_PIN, HIGH);
}
