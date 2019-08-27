// Condition--------------------------
#define DRAW 0
#define STOP 1

// ステップ(配列の0番目の要素は必ずデータ数を格納せよ)--------------------------------
int X1_1[] = {4, 2466, 96, 93, 95};
int Y1_1[] = {4, 3913, 7, -2, 3};
int X1_2[] = {1, 1};
int Y1_2[] = {1, 2};
int X1_3[] = {1, 3};
int Y1_3[] = {1, 4};

int X2_1[] = {2, 5, 10};
int Y2_1[] = {2, 6, 23};
int X2_2[] = {1, 3};
int Y2_2[] = {1, 5};

// x, y-----------------------------
int* line1_1[] = {X1_1, Y1_1};
int* line1_2[] = {X1_2, Y1_2};
int* line1_3[] = {X1_3, Y1_3};

int* line2_1[] = {X2_1, Y2_1};
int* line2_2[] = {X2_2, Y2_2};

// 線-------------------------------
int** picture1[] = {line1_1, line1_2, line1_3};
int** picture2[] = {line2_1, line2_2};

int lineNum[] = {3, 2};
// 絵-------------------------------
int*** pictures[] = {picture1, picture2};
int picturesLen = 2;


int condition = STOP;
int picture = 0;
int line = 0;
int point = 1;
int nextPicture = 1;



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
