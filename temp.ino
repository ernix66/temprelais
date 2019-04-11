#include <OneWire.h>
#include <DallasTemperature.h>
 
#define ONE_WIRE_BUS 2
 
OneWire oneWire(ONE_WIRE_BUS);
 
DallasTemperature sensors(&oneWire);
 
void setup(void)
{
  Serial.begin(9600);
 
  sensors.begin();
  
  pinMode(3, OUTPUT);
    
}
 
 float t1;
 float t2;
 float tmpon = 40;
 float tmpoff =38;
 int luefter=0;
  
void loop(void)
{
 
  
  sensors.requestTemperatures(); 
  
  t1=sensors.getTempCByIndex(0);
  t2=sensors.getTempCByIndex(1);
  
  Serial.print(t1);
  Serial.print(" ");
  Serial.print(t2);
  Serial.print(" ");
  Serial.print(luefter);
  Serial.print("\n");
  if ((t1 > tmpon) or (t2 > tmpon))
  {
    digitalWrite(3, LOW);
    luefter=1;
  }
  
  if ((t1 < tmpoff) and (t2 < tmpoff))
  {
    digitalWrite(3, HIGH);
    luefter=0;
  }
  delay(10000);
}


