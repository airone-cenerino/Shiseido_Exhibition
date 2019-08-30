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


void ButtonSetUp() {
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

void ButtonCheck() {
  if (digitalRead(INITIALIZE_BUTTON_PIN) == 0) {
    if (!initialButtonCondition) {
      InitializeButtonDown();
      initialButtonCondition = true;
    }
  } else {
    initialButtonCondition = false;
  }

  if (digitalRead(START_STOP_BUTTON_PIN) == 0) {
    if (!startStopButtonCondition) {
      StartStopButtonDown();
      startStopButtonCondition = true;
    }
  } else {
    startStopButtonCondition = false;
  }

  if (digitalRead(RESTART_BUTTON_PIN) == 0) {
    if (!restartButtonCondition) {
      RestartButtonDown();
      restartButtonCondition = true;
    }
  } else {
    restartButtonCondition = false;
  }

  if (digitalRead(SELECT_BUTTON_PIN) == 0) {
    if (!selectButtonCondition) {
      SelectButtonDown();
      selectButtonCondition = true;
    }
  } else {
    selectButtonCondition = false;
  }
}



void InitializeButtonDown() {
  if (condition == STOP) {
    digitalWrite(INITIALIZE_BUTTON_LAMP_PIN, LOW);
    InitializeMotorMove();
    digitalWrite(INITIALIZE_BUTTON_LAMP_PIN, HIGH);
  }
}

void StartStopButtonDown() {
  Serial.println("スタート/ストップボタンが押されました。");
  switch (condition) {
    case DRAW:
      ServoUp();

    
      SetCondition(STOP);
      break;
    case STOP:

      ServoDown();
    
      SetCondition(DRAW);
      break;
  }
}

void RestartButtonDown() {
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
  SetCondition(DRAW);

  digitalWrite(RESTART_BUTTON_LAMP_PIN, LOW);
  DisplayUpdate();
  delay(500);
  digitalWrite(RESTART_BUTTON_LAMP_PIN, HIGH);
}

void SelectButtonDown() {
  if (nextPicture + 1 == picturesLen) {
    nextPicture = 0;
  } else {
    nextPicture = picture + 1;
  }

  digitalWrite(SELECT_BUTTON_LAMP_PIN, LOW);
  DisplayUpdate();
  delay(500);
  digitalWrite(SELECT_BUTTON_LAMP_PIN, HIGH);
}
