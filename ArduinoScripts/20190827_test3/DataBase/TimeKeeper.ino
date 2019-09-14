unsigned long startTime = 0;
unsigned long pauseStartTime = 0;

// startTime を絵を描き始めた時間にセットする。
// 表示するのはmillis()との差の時間
// 一時停止中は止めたときの時間、始めたときの時間を記録し、startTimeに補正をかける

void TimeKeeper_ResetTime(){  // startTimeを現在時刻にする
  startTime = int(millis()/1000);
}

void TimeKeeper_SetPauseStartTime(){  // pauseStartTimeを現在時刻にする
  pauseStartTime = int(millis()/1000);
}

void TimeKeeper_RestartReviseStartTime(){  // 絵を一時停止から書き始めたときのstartTimeの補正
  startTime += int(millis()/1000) - pauseStartTime; 
}

int TimeKeeper_GetElapsedTime(){
  if(condition == DRAW){
    return int(millis()/1000) - startTime;
  }else{
    return pauseStartTime - startTime;
  }
}

int TimeKeeper_GetTimeRemaining(){
  return timeRequiredToDraw[picture] - TimeKeeper_GetElapsedTime();
}
