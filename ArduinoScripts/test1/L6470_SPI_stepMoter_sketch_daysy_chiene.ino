#include<SPI.h>
#include<stdio.h>

//// ピン定義。-------Due用
//#define PIN_SPI_MOSI MOSI
//#define PIN_SPI_MISO MISO
//#define PIN_SPI_SCK SCK
//#define PIN_SPI_SS 4
//#define PIN_BUSY 30
//#define PIN_BUSY2 29

//----------------Uno用
#define PIN_SPI_MOSI 11
#define PIN_SPI_MISO 12
#define PIN_SPI_SCK 13
#define PIN_SPI_SS 10
#define PIN_BUSY 9
#define PIN_BUSY2 8
//-----------------------

void MotorSetUp(){
  delay(1000);
  
  pinMode(PIN_SPI_MOSI, OUTPUT);
  pinMode(PIN_SPI_MISO, INPUT);
  pinMode(PIN_SPI_SCK, OUTPUT);
  pinMode(PIN_SPI_SS, OUTPUT);
  pinMode(PIN_BUSY, INPUT_PULLUP);
  pinMode(PIN_BUSY2, INPUT_PULLUP);
  SPI.begin();
  SPI.setDataMode(SPI_MODE3);
  SPI.setBitOrder(MSBFIRST);
  digitalWrite(PIN_SPI_SS, HIGH);
 
  L6470_resetdevice(); //1台目のL6470リセット
  L6470_resetdevice2(); //2台目のL6470リセット
  L6470_setup();  //1台目のL6470を設定 
  L6470_setup2();  //2台目のL6470を設定 
  L6470_getstatus(); //1台目のフラグ解放
  L6470_getstatus2();//2台目のフラグ解放

  delay(2000);
}

void L6470_setup(){
L6470_setparam_acc(0x30); //[R, WS] 加速度default 0x08A (12bit) (14.55*val+14.55[step/s^2])
L6470_setparam_dec(0x30); //[R, WS] 減速度default 0x08A (12bit) (14.55*val+14.55[step/s^2])
L6470_setparam_maxspeed(0x2a); //[R, WR]最大速度default 0x041 (10bit) (15.25*val+15.25[step/s])
L6470_setparam_minspeed(0x1200); //[R, WS]最小速度default 0x000 (1+12bit) (0.238*val[step/s])
L6470_setparam_fsspd(0x027); //[R, WR]μステップからフルステップへの切替点速度default 0x027 (10bit) (15.25*val+7.63[step/s])
L6470_setparam_kvalhold(0x28); //[R, WR]停止時励磁電圧default 0x29 (8bit) (Vs[V]*val/256)
L6470_setparam_kvalrun(0x28); //[R, WR]定速回転時励磁電圧default 0x29 (8bit) (Vs[V]*val/256)
L6470_setparam_kvalacc(0x28); //[R, WR]加速時励磁電圧default 0x29 (8bit) (Vs[V]*val/256)
L6470_setparam_kvaldec(0x28); //[R, WR]減速時励磁電圧default 0x29 (8bit) (Vs[V]*val/256)

L6470_setparam_stepmood(0x02); //ステップモードdefault 0x07 (1+3+1+3bit)
}

void L6470_setup2(){
L6470_setparam_acc2(0x30); //[R, WS] 加速度default 0x08A (12bit) (14.55*val+14.55[step/s^2])
L6470_setparam_dec2(0x30); //[R, WS] 減速度default 0x08A (12bit) (14.55*val+14.55[step/s^2])
L6470_setparam_maxspeed2(0x2a); //[R, WR]最大速度default 0x041 (10bit) (15.25*val+15.25[step/s])
L6470_setparam_minspeed2(0x1200); //[R, WS]最小速度default 0x000 (1+12bit) (0.238*val[step/s])
L6470_setparam_fsspd2(0x027); //[R, WR]μステップからフルステップへの切替点速度default 0x027 (10bit) (15.25*val+7.63[step/s])
L6470_setparam_kvalhold2(0x28); //[R, WR]停止時励磁電圧default 0x29 (8bit) (Vs[V]*val/256)
L6470_setparam_kvalrun2(0x28); //[R, WR]定速回転時励磁電圧default 0x29 (8bit) (Vs[V]*val/256)
L6470_setparam_kvalacc2(0x28); //[R, WR]加速時励磁電圧default 0x29 (8bit) (Vs[V]*val/256)
L6470_setparam_kvaldec2(0x28); //[R, WR]減速時励磁電圧default 0x29 (8bit) (Vs[V]*val/256)

L6470_setparam_stepmood2(0x02); //ステップモードdefault 0x07 (1+3+1+3bit)
}


void fulash(){
  

long a=L6470_getparam_abspos();
long b=L6470_getparam_speed();
long c=L6470_getparam_abspos2();
long d=L6470_getparam_speed2();
char str[15];
snprintf(str,sizeof(str),"1pos=0x%6.6X ",a);
Serial.print(str);
snprintf(str,sizeof(str),"1spd=0x%5.5X ",b);
Serial.print(str);
snprintf(str,sizeof(str),"2pos=0x%6.6X ",c);
Serial.print(str);
snprintf(str,sizeof(str),"2spd=0x%5.5X ",d);
Serial.println(str);
  
 /* Serial.print("0x");
  Serial.print( L6470_getparam_abspos(),HEX);
  Serial.print(" 0x");
  Serial.print( L6470_getparam_speed(),HEX);
  Serial.print(" 0x");
  Serial.print( L6470_getparam_abspos2(),HEX);
  Serial.print(" 0x");
  Serial.println( L6470_getparam_speed2(),HEX);
  */
}
