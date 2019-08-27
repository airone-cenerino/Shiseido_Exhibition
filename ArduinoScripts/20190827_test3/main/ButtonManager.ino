// Pin番号----------------------------
#define INITIALIZE_BUTTON_PIN 3
#define START_STOP_BUTTON_PIN 2
#define RESTART_BUTTON_PIN 4
#define SELECT_BUTTON_PIN 5

bool initialButtonCondition = false;
bool startStopButtonCondition = false;
bool restartButtonCondition = false;
bool selectButtonCondition = false;

void InitializeButtonDown() {
  Serial.println("初期化ボタンが押されました。");

  if (condition == STOP) {
    Serial.println("位置調整を行います。");
    // ここでモータを回して中心に持ってくる。


  }
}

void StartStopButtonDown() {
  Serial.println("スタート/ストップボタンが押されました。");
  switch (condition) {
    case DRAW:
      condition = STOP;
      break;
    case STOP:
      condition = DRAW;
      break;
  }
}

void RestartButtonDown() {
  Serial.println("リスタートボタンが押されました。");

  // 次に描く絵を最初から描き始める
  picture = nextPicture;
  if (picture + 1 == picturesLen) {
    nextPicture = 0;
  } else {
    nextPicture = picture + 1;
  }
  line = 0;
  point = 1;
  condition = DRAW;
}

void SelectButtonDown() {
  Serial.println("セレクトボタンが押されました。");
  if (picture + 1 == picturesLen) {
    nextPicture = 0;
  } else {
    nextPicture = picture + 1;
  }
}








void PinSetUp() {
  pinMode(INITIALIZE_BUTTON_PIN, INPUT);
  pinMode(START_STOP_BUTTON_PIN, INPUT);
  pinMode(RESTART_BUTTON_PIN, INPUT);
  pinMode(SELECT_BUTTON_PIN, INPUT);
  pinMode(13, OUTPUT);
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
