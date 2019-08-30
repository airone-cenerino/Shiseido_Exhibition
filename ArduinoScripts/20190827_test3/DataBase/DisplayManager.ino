#include <LiquidCrystal.h>

LiquidCrystal lcd(33, 32, 31, 30, 29, 28);

void DisplaySetUp() {
  lcd.begin(16, 2);
  DisplayUpdate();
}

void DisplayUpdate(){
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Now:" + String(picture) + " " + String(line+1) + "/" + String(lineNum[picture]));
  lcd.setCursor(0, 1);
  lcd.print("Next:" + String(nextPicture));
}
