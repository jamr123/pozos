#include <SPI.h>
#include <RF24.h>

RF24 radio(9, 10); // CE, CSN
const byte identificacion[6] = "00001";

const int caudal1 = 2;
const int caudal2 = 3;

volatile int countCaudal1 = 0;
volatile int countCaudal2 = 0;

volatile unsigned long presenteMillis = 0;
volatile unsigned long pasadoMillis = 0;

volatile int intervaloCaudal = 180;
volatile int segundosCaudal = 0;
volatile int litrosPulso1 = 100;
volatile int litrosPulso2 = 100;
volatile int valCaudal1 = 0;
volatile int valCaudal2 = 0;


#define SELPIN 8 //Selection Pin 
#define DATAOUT 5//MOSI 
#define DATAIN  6//MISO 
#define SPICLOCK  7//Clock

int readA1 = 0;
int readA2 = 0;
int readA3 = 0;
int readA4 = 0;
int inA1 = 0;
int inA2 = 0;
int inA3 = 0;
int inA4 = 0;
String sendData = "";

void setup() {

  pinMode(caudal1, INPUT_PULLUP);
  pinMode(caudal2, INPUT_PULLUP);

  attachInterrupt(digitalPinToInterrupt(caudal1), isr_caudal1, FALLING);
  attachInterrupt(digitalPinToInterrupt(caudal2), isr_caudal2, FALLING);

  radio.begin();
  radio.openWritingPipe(identificacion);
  radio.setPALevel(RF24_PA_MAX);
  radio.stopListening();
  pasadoMillis = millis();

  Serial.begin(9600);
}

void loop() {

  presenteMillis =  millis();
  if (presenteMillis > (pasadoMillis + 1000))
  {
    segundosCaudal ++;

    if (segundosCaudal == intervaloCaudal)
    {
      segundosCaudal = 0;
      calculoCaudal();

    }

    Serial.println("");
    Serial.println(countCaudal1);
    Serial.println(countCaudal2);
    Serial.println("");
    enviarData();

    pasadoMillis = millis();
  }

  readTarjeta();

}

void isr_caudal1() {
  countCaudal1 ++;
}

void isr_caudal2() {
  countCaudal2 ++;
}

void calculoCaudal() {

  valCaudal1 = (countCaudal1 * litrosPulso1) / intervaloCaudal;
  valCaudal2 = (countCaudal2 * litrosPulso2) / intervaloCaudal;
  countCaudal1 = 0;
  countCaudal2 = 0;

}

int read_adc(int channel) {
  int adcvalue = 0;
  byte commandbits = B11000000; 
  commandbits |= ((channel - 1) << 3);

  digitalWrite(SELPIN, LOW);
  for (int i = 7; i >= 3; i--) {
    digitalWrite(DATAOUT, commandbits & 1 << i);
    digitalWrite(SPICLOCK, HIGH);
    digitalWrite(SPICLOCK, LOW);
  }

  digitalWrite(SPICLOCK, HIGH);   
  digitalWrite(SPICLOCK, LOW);
  digitalWrite(SPICLOCK, HIGH);
  digitalWrite(SPICLOCK, LOW);

  for (int i = 11; i >= 0; i--) {
    adcvalue += digitalRead(DATAIN) << i;
    digitalWrite(SPICLOCK, HIGH);
    digitalWrite(SPICLOCK, LOW);
  }
  digitalWrite(SELPIN, HIGH); 
  return adcvalue;
}

void enviarData()
{
  sendData = "POZO1";
  sendData = sendData + "$" + String(readA1);
  sendData = sendData + "$" + String(readA2);
  sendData = sendData + "$" + String(readA3);
  sendData = sendData + "$" + String(readA4);
  sendData = sendData + "$" + String(valCaudal1);
  sendData = sendData + "$" + String(valCaudal2);


  Serial.println(sendData);

  int str_len =  sendData.length() + 1;
  char data[str_len];
  sendData.toCharArray(data, str_len);
  radio.write(&data, sizeof(data));


}

void readTarjeta() {
  inA1 = read_adc(1);
  inA2 = read_adc(2);
  inA3 = read_adc(3);
  inA4 = read_adc(4);

  if (inA1 > 0) {
    readA1 = A1;
  }
  if (inA2 > 0) {
    readA2 = A2;
  }
  if (inA3 > 0) {
    readA3 = A3;
  }
  if (inA4 > 0) {
    readA4 = A4;
  }
}
