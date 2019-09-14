#include <LiquidCrystal.h>

LiquidCrystal lcd(33, 32, 31, 30, 29, 28);

int elapsedTime = 0;

void DisPlayManager_loop(){  // 1秒おきにDisplayUpdate()を呼ぶ
  if(int(millis()/1000) != elapsedTime){
    DisplayManager_DisplayUpdate();
    elapsedTime = int(millis()/1000);
  }
}

void DisPlayManager_DisplaySetUp() {
  lcd.begin(16, 2);
  DisplayManager_DisplayUpdate();
}

void DisplayManager_DisplayUpdate(){
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Now:" + String(picture+ 1) + " " + String(line+1) + "/" + String(lineNum[picture]));
  lcd.setCursor(0, 1);
  lcd.print("Next:"+ String(nextPicture+ 1));
  lcd.setCursor(7, 1);
  lcd.print(String(TimeKeeper_GetTimeRemaining()));
}
