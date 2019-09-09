#include <SPI.h>
#include <RF24.h>
#include <OneWire.h>                
#include <DallasTemperature.h>
 
OneWire ourWire(2);   
DallasTemperature sensors(&ourWire);

RF24 radio(9, 10); // CE, CSN
const byte identificacion[6] = "00001";

volatile unsigned long presenteMillis = 0;
volatile unsigned long pasadoMillis = 0;

void setup() {

  radio.begin();
  radio.openWritingPipe(identificacion);
  radio.setPALevel(RF24_PA_MAX);
  radio.stopListening();

  Serial.begin(9600);
  sensors.begin();   
  pasadoMillis = millis();
}



void loop() {
sensors.requestTemperatures();   //Se envía el comando para leer la temperatura
float temp= sensors.getTempCByIndex(0); //Se obtiene la temperatura en ºC
enviarData(temp);
delay(5000);


}

void enviarData(float temp1)
{
  String sendDato = "TEMPERATURA1";
   sendDato =  sendDato + "$" + String(temp1);
   sendDato =  sendDato + "$";


  Serial.println(sendDato);

  int str_len =  sendDato.length() + 1;
  char data[str_len];
  sendDato.toCharArray(data, str_len);
  radio.write(&data, sizeof(data));


}
