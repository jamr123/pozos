#include <SPI.h>
#include <RF24.h>
RF24 radio(9, 10); 


const uint64_t rAddress[] = {0x010000111111, 0x020000111111, 0X030000111111, 0x040000111111, 0x050000111111, 0x060000111111 };

void setup() {
  Serial.begin(9600);
  radio.begin(); 

           
 
  radio.openReadingPipe(0,rAddress[0]);//pozo1
  radio.openReadingPipe(1,rAddress[1]);//pozo2
  radio.openReadingPipe(2,rAddress[2]);//pozo3
  radio.openReadingPipe(3,rAddress[3]);//t1
  radio.openReadingPipe(4,rAddress[4]);//t2
  radio.openReadingPipe(5,rAddress[5]);//t3
  radio.setPALevel(RF24_PA_MAX); 
  radio.startListening();                 // Start listening for messages
}

void loop() {
  
  if (radio.available()) {
  char texto[158] = ""; 
  radio.read(&texto, sizeof(texto)); 
  Serial.println(texto);

 }
}
