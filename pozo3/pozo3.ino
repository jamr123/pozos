
#include <SPI.h>
#include <RF24.h>

RF24 radio(9, 10); // CE, CSN
const byte identificacion[6] = "00001";

#define SELPIN 8 //Selection Pin 
#define DATAOUT 5//MOSI 
#define DATAIN  6//MISO 
#define SPICLOCK  7//Clock 
int readvalue;

volatile unsigned long presenteMillis = 0;
volatile unsigned long pasadoMillis = 0;

const int caudal1 = 2;
const int caudal2 = 3;

volatile int countCaudal1 = 0;
volatile int countCaudal2 = 0;

volatile int intervaloCaudal = 180;
volatile int segundosCaudal = 0;
volatile int litrosPulso1 = 100;
volatile int litrosPulso2 = 100;
volatile int valCaudal1 = 0;
volatile int actCaudal1=0;
volatile int valCaudal2 = 0;
volatile int actCaudal2=0;

volatile int segundosEnvio=0;
const int intervaloEnvio=5;


void setup() {
  pinMode(caudal1, INPUT_PULLUP);
  pinMode(caudal2, INPUT_PULLUP);

  attachInterrupt(digitalPinToInterrupt(caudal1), isr_caudal1, FALLING);
  attachInterrupt(digitalPinToInterrupt(caudal2), isr_caudal2, FALLING);
  
  //set pin modes
  pinMode(SELPIN, OUTPUT);
  pinMode(DATAOUT, OUTPUT);
  pinMode(DATAIN, INPUT);
  pinMode(SPICLOCK, OUTPUT);
  //disable device to start with
  digitalWrite(SELPIN, HIGH);
  digitalWrite(DATAOUT, LOW);
  digitalWrite(SPICLOCK, LOW);
  
  radio.begin();
  radio.openWritingPipe(identificacion);
  radio.setPALevel(RF24_PA_MAX);
  radio.stopListening();

  Serial.begin(9600);
  pasadoMillis = millis();
}

int read_adc(int channel) {
  int adcvalue = 0;
  byte commandbits = B11000000; //command bits - start, mode, chn (3), dont care (3)

  //allow channel selection
  commandbits |= ((channel - 1) << 3);

  digitalWrite(SELPIN, LOW); //Select adc
  // setup bits to be written
  for (int i = 7; i >= 3; i--) {
    digitalWrite(DATAOUT, commandbits & 1 << i);
    //cycle clock
    digitalWrite(SPICLOCK, HIGH);
    digitalWrite(SPICLOCK, LOW);
  }

  digitalWrite(SPICLOCK, HIGH);   //ignores 2 null bits
  digitalWrite(SPICLOCK, LOW);
  digitalWrite(SPICLOCK, HIGH);
  digitalWrite(SPICLOCK, LOW);

  //read bits from adc
  for (int i = 11; i >= 0; i--) {
    adcvalue += digitalRead(DATAIN) << i;
    //cycle clock
    digitalWrite(SPICLOCK, HIGH);
    digitalWrite(SPICLOCK, LOW);
  }
  digitalWrite(SELPIN, HIGH); //turn off device
  return adcvalue;
}


void loop() {

  presenteMillis =  millis();

  

  if (presenteMillis > (pasadoMillis + 1000))
  {

  segundosCaudal ++;
  segundosEnvio ++;

  if(segundosCaudal==intervaloCaudal){
     segundosCaudal=0;
     calculoCaudal();
    }
    if(segundosEnvio==intervaloEnvio){
     segundosEnvio=0;
     enviarData(read_adc(1),read_adc(2),read_adc(3),read_adc(4),valCaudal1,valCaudal2,actCaudal1,actCaudal2);
     if(actCaudal1==1){
      actCaudal1=0;
      }
      if(actCaudal2==1){
       actCaudal2=0;
      }
    }
    
    pasadoMillis = millis();
  }




}


void enviarData(int adc1, int adc2 ,int adc3, int adc4, int cdl1, int cdl2,int act1,int act2,)
{
  String sendDato = "POZO3";
   sendDato =  sendDato + "$" + String(adc1);
   sendDato =  sendDato + "$" + String(adc2);
   sendDato =  sendDato + "$" + String(adc3);
   sendDato =  sendDato + "$" + String(adc4);
   sendDato =  sendDato + "$" + String(cdl1);
   sendDato =  sendDato + "$" + String(cdl2);
   sendDato =  sendDato + "$" + String(act1);
   sendDato =  sendDato + "$" + String(act2);
   sendDato =  sendDato + "$";


  Serial.println(sendDato);

  int str_len =  sendDato.length() + 1;
  char data[str_len];
  sendDato.toCharArray(data, str_len);
  radio.write(&data, sizeof(data));


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
  actCaudal1=1;
  actCaudal2=1

}
