  
  float width = 160;
  float l = width*sqrt(2)/2+0;
  float r = width*sqrt(2)/2+0;
  int rstep = 0;
  int lstep = 0;
  float cos = 0;
  float sin = 0;
  float x , y ;
  String linesL[];
  String linesR[];
  int ln = 0;
  String linR,linL;
  PFont Font1;
  
  int pointx[] = new int[3753];
  int pointy[] = new int[3753];
  
  void setup(){
    frameRate(400);
  size(500,500);
  background(255);
  
  linesR = loadStrings("RightMotor.csv");
  linesL = loadStrings("LeftMotor.csv");
  
  Font1 = loadFont("AgencyFB-Reg-30.vlw");
  
  }
  
  void draw(){
    delay(30);
    
    if(ln < 3753)
    {      
    background(255);
    fill(0);
    
    linR = linesR[ln];
    linL = linesL[ln];
    
    String [] coR = split(linR,',');
    String [] coL = split(linL,',');
    
    if(coR.length == 1)
    {
      rstep += float(coR[0]);
      r = width*sqrt(2)/2+float(rstep)/400;
      print(int(rstep));
      print(" ");
    }
  
      
    if(coL.length == 1)
    {
      lstep += float(coL[0]);
      l = width*sqrt(2)/2+float(lstep)/400;
      print(int(lstep));
      print("\n");
  
    }
    
    
    
  cos = (l*l + width*width - r*r)/(2*l*width);
  
  x = l*cos;
  sin = sqrt((1 + cos)*(1 - cos));
  
  y = l*sin;
  
  fill(0);
  ellipse(x*500/width,y*500/width,1,1);
  strokeWeight(2);
  line(0,0,x*500/width,y*500/width);
  line(500,0,x*500/width,y*500/width);
  
  for(int i = 0 ; i < ln ; i++)
  {
    ellipse(pointx[i],pointy[i],1,1);
  }
  
  pointx[ln]=int(x*500/width);
  pointy[ln]=int(y*500/width);
  ln++;
  
      textFont(Font1);
    textAlign(LEFT);
    textSize(20);
    text(r,70,70);
    text("r",40,70);
    text(l,70,100);
    text("l",40,100);
    
    text("rstep",200,70);
    text(int(rstep),300,70);
    text("lstep",200,100);
    text(int(lstep),300,100);
   //print(ln);
  
    }
  
  
  
  }
