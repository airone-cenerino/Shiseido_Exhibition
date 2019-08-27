// Condition--------------------------
#define DRAW 0
#define STOP 1

// ステップ量-------------------------
int X1_1[] = {2466,96,93,95};
int Y1_1[] = {3913,7,-2,3};
int X1_2[] = {1};
int Y1_2[] = {2};
int X1_3[] = {3};
int Y1_3[] = {4};

int X2_1[] = {0};
int Y2_1[] = {0};
int X2_2[] = {0};
int Y2_2[] = {0};

// x, y-----------------------------
int* line1_1[] = {X1_1, Y1_1};
int* line1_2[] = {X1_2, Y1_2};
int* line1_3[] = {X1_3, Y1_3};

int* line2_1[] = {X2_1, Y2_1};
int* line2_2[] = {X2_2, Y2_2};

// 線-------------------------------
int** picture1[] = {line1_1, line1_2, line1_3};
int** picture2[] = {line2_1, line2_2};

// 絵-------------------------------
int*** pictures[] = {picture1, picture2};
int picturesLen;


int condition = STOP;
int picture = 1;
int line = 1;
int point = 1;
int nextPicutre = 2;



void setup() {
  Serial.begin(9600);
  PinSetUp();
  MotorSetUp();
}

void loop() {
  ButtonCheck();

  if (condition == DRAW) {
    // 次に回すべきステップ数を確認し、モータを動かす。
  }
}
