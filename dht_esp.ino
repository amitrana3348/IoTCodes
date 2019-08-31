#include <SoftwareSerial.h>
#include <SimpleDHT.h>

#define RX 2  
#define TX 3
String AP = "Robotics Center";       // CHANGE ME
String PASS = "vidya123"; // CHANGE ME
String API = "CR66EXHNNRZJKKPP";   // CHANGE ME
String HOST = "api.thingspeak.com";
String PORT = "80";
String field = "field1";
int countTrueCommand;
int countTimeCommand; 
boolean found = false; 
int valSensor = 1;

SoftwareSerial esp8266(RX,TX); 
int pinDHT11 = 7;
SimpleDHT11 dht11(pinDHT11);


void setup() 
{
  Serial.begin(115200);
  esp8266.begin(115200);
  sendCommand("AT",5,"OK"); // justing
  sendCommand("AT+CWMODE=1",5,"OK");  // specify the mode, as an end device connected to existing wifi
  sendCommand("AT+CWJAP=\""+ AP +"\",\""+ PASS +"\"",20,"OK"); // connect to wifi network
}
void loop() 
{

 // read without samples.
  byte temperature = 0;
  byte humidity = 0;
  int err = SimpleDHTErrSuccess;
  if ((err = dht11.read(&temperature, &humidity, NULL)) != SimpleDHTErrSuccess) 
  {
    Serial.print("Read DHT11 failed, err="); Serial.println(err);delay(1000);
    return;
  }
  
  Serial.print("Sample OK: ");
  Serial.print((int)temperature); Serial.print(" *C, "); 
  Serial.print((int)humidity); Serial.println(" H");

  
 valSensor = getSensorData();
 String getData = "GET /update?api_key="+ API +"&"+ field +"="+String(temperature) + "&field2=" + String(humidity);
 
 sendCommand("AT+CIPMUX=1",5,"OK");
 sendCommand("AT+CIPSTART=0,\"TCP\",\""+ HOST +"\","+ PORT,15,"OK");
 sendCommand("AT+CIPSEND=0," +String(getData.length()+4),4,">");
 esp8266.println(getData);delay(1500);countTrueCommand++;
 sendCommand("AT+CIPCLOSE=0",5,"OK");

 delay(15000);
}

int getSensorData()
{
  return random(1000); // Replace with 
}
void sendCommand(String command, int maxTime, char readReplay[]) {
  Serial.print(countTrueCommand);
  Serial.print(". at command => ");
  Serial.print(command);
  Serial.print(" ");
  while(countTimeCommand < (maxTime*1))
  {
    esp8266.println(command);//at+cipsend
    if(esp8266.find(readReplay))//ok
    {
      found = true;
      break;
    }
  
    countTimeCommand++;
  }
  
  if(found == true)
  {
    Serial.println(" Ok");
    countTrueCommand++;
    countTimeCommand = 0;
  }
  
  if(found == false)
  {
    Serial.println("Fail");
    countTrueCommand = 0;
    countTimeCommand = 0;
  }
  
  found = false;
 }
