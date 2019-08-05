// データここから-------------------------------------------------------------------------------------------------------------
// ステップ(配列の0番目要素は必ずデータ数を格納せよ)--------------------------------
int X1_1[] = {4,2466,96,93,95};
int Y1_1[] = {4,3913,7,-2,3};
int X1_2[] = {1,1};
int Y1_2[] = {1,2};
int X1_3[] = {1,3};
int Y1_3[] = {1,4};

int X2_1[] = {1,0};
int Y2_1[] = {1,0};

// x, y----------------------------------
int* line1_1[] = {X1_1, Y1_1};
int* line1_2[] = {X1_2, Y1_2};
int* line1_3[] = {X1_3, Y1_3};

int* line2_1[] = {X2_1, Y2_1};


// 線-------------------------------------
int** picture1[] = {line1_1, line1_2, line1_3};
int** picture2[] = {line2_1};

int linesLen[] = {sizeof(picture1)/sizeof(int**), sizeof(picture2)/sizeof(int**)};  // 絵が増えたらここも追加

// 絵-------------------------------------
int*** pictures[] = {picture1, picture2};
int picturesLen = sizeof(pictures)/sizeof(int***);

// データここまで-------------------------------------------------------------------------------------------------------------

void setup() {
  Serial.begin(9600);

  for(int k=0;k<picturesLen;k++){  // 絵   
    for(int j=0;j<linesLen[k];j++){ // 線
      for(int i=1;i<=pictures[k][j][0][0];i++){  // ステップ
        Serial.println(pictures[k][j][0][i]);
        Serial.println(pictures[k][j][1][i]);
        Serial.println("--");
      }
    }
  }
}

void loop() {

}
