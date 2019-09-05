#include <SPI.h>
#include <RF24.h>
RF24 radio(9, 10); // CE, CSN


const byte identificacion[6] = "00001";

void setup() {
  Serial.begin(9600); // Iniciamos la comunicacion serie hacia el Monitor Serie en la PC


  radio.begin();


  radio.openReadingPipe(0, identificacion);


  radio.setPALevel(RF24_PA_MIN);

/* La funcion radio.startListening() establece al 
modulo como receptor. */
  radio.startListening();
}

void loop() {
  if (radio.available()) {
  char texto[32] = ""; 
/* Creamos una matriz de caracteres donde recibir el 
mensaje */

  radio.read(&texto, sizeof(texto)); // Esperamos que llegue algo por RF desde el módulo


  Serial.println(texto);
  

 }
}
