#include <SPI.h>
#include <RF24.h>
#include <OneWire.h>                
#include <DallasTemperature.h>

OneWire onewire(2); 

RF24 radio(9, 10); // CE, CSN
const uint64_t rAddress[] = {0x010000111111, 0x020000111111, 0x030000111111, 0x040000111111, 0x050000111111, 0x060000111111 };


volatile unsigned long presenteMillis = 0;
volatile unsigned long pasadoMillis = 0;

void setup() {

  radio.begin();
  radio.openWritingPipe(rAddress[3]);
  radio.setPALevel(RF24_PA_MAX);
  radio.stopListening();
  Serial.begin(9600);  
  pasadoMillis = millis();
}




void loop() {
float temperature;
char tempC[6];
  if (sensor_read(&temperature))
  {
    dtostrf(temperature, 3, 2, tempC);
    enviarData(String(tempC));
  }
  else
  {
    Serial.println(F("Fallo de comunicacion con DS18B20"));
  }

delay(1000);


}

void enviarData(String temp1)
{
  String sendDato = "TEMPERATURA1";
   sendDato =  sendDato + "$" + temp1;
   sendDato =  sendDato + "$";


  Serial.println(sendDato);

  int str_len =  sendDato.length() + 1;
  char data[str_len];
  sendDato.toCharArray(data, str_len);
  radio.write(&data, sizeof(data));


}

bool sensor_read(float *result)
{
  uint8_t data[12];
  int i;
  *result = -100.0;
  onewire.reset();
  onewire.skip();
  onewire.write(0x44);
  delay(1000);
  if (!onewire.reset())
    return false;
  onewire.skip();
  onewire.write(0xBE);
  for (i = 0; i < 9; i++)
    data[i] = onewire.read();
  int16_t temp = (((int16_t)data[1]) << 11) | (((int16_t)data[0]) << 3);
  *result = (float)temp * 0.0078125;
  return true;
}
