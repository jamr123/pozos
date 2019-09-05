#include <SPI.h>
#include <RF24.h>

RF24 radio(7, 8); // CE, CSN
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



void setup() {

  pinMode(caudal1, INPUT_PULLUP);
  pinMode(caudal2, INPUT_PULLUP);

  attachInterrupt(digitalPinToInterrupt(caudal1), isr_caudal1, FALLING);
  attachInterrupt(digitalPinToInterrupt(caudal2), isr_caudal2, FALLING);

  radio.begin();
  radio.openWritingPipe(identificacion);
  radio.setPALevel(RF24_PA_MIN);
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
   const char texto[] = "Pozo 3";
   radio.write(&texto, sizeof(texto));
  
    pasadoMillis = millis();
  }

}

void isr_caudal1() {
  countCaudal1 ++;
}

void isr_caudal2() {
  countCaudal2 ++;
}

void calculoCaudal() {

valCaudal1=(countCaudal1*litrosPulso1)/intervaloCaudal;
valCaudal2=(countCaudal2*litrosPulso2)/intervaloCaudal;

}
