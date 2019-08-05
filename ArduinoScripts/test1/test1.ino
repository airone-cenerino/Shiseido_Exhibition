// ステップ--------------------------------
int X1_1[] = {2466,96,93,95};
int Y1_1[] = {3913,7,-2,3};
int X1_2[] = {1};
int Y1_2[] = {2};
int X1_3[] = {3};
int Y1_3[] = {4};

int X2_1[] = {0};
int Y2_1[] = {0};

// x, y----------------------------------
int* line1_1[] = {X1_1, Y1_1};
int* line1_2[] = {X1_2, Y1_2};
int* line1_3[] = {X1_3, Y1_3};

int* line2_1[] = {X2_1, Y2_1};

// 線-------------------------------------
int** picture1[] = {line1_1, line1_2, line1_3};
int** picture2[] = {line2_1};

//int* linesLen;

// 絵-------------------------------------
int*** pictures[] = {picture1};
int picturesLen;


void setup() {
  Serial.begin(9600);
  picturesLen = sizeof(pictures)/sizeof(int***);
  //MotorSetUp();

  for(int k=0;k<picturesLen;k++){  // 絵   
    for(int j=0;j<sizeof(pictures[k])/sizeof(int);j++){ // 線
        for(int i=0;i<sizeof(pictures[0][0][0])/sizeof(int);i++){  // ステップ
//        if(pictures[0][0][0][i] > 0){
//          L6470_move(1,pictures[0][0][0][i]);
//        }else{
//          L6470_move(0,-pictures[0][0][0][i]);
//        }
//    
//        if(pictures[0][0][1][i] > 0){
//          L6470_move2(1,pictures[0][0][1][i]);
//        }else{
//          L6470_move2(0,-pictures[0][0][1][i]);
//        }
//        
//        L6470_busydelay(0);
//        L6470_busydelay2(0);
          Serial.println(pictures[0][0][0][i]);
          Serial.println(pictures[0][0][1][i]);
          Serial.println("--");
        }
//    }
//  }
}

void loop() {

}
