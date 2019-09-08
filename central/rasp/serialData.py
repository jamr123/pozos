import time
import serial
import threading

# configure the serial connections (the parameters differs on the device you are connecting to)
#ser =serial.Serial('/dev/ttyAMA0', 115200, timeout=1)
ser =serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
#ser =serial.Serial('/dev/ttyACM0', 9600, timeout=1)

#http=httpRequest.Http()
class Data:
    responseData=None
    flagResponse=False
    def __init__(self):
            
                    
        thread = threading.Thread(target=self.sync, args=())
        thread.daemon = True                            
        thread.start()

    def sync(self):
        
        while True:
            try:
                if ser.inWaiting()>0:
                    s=ser.readline()
                    dato=s.decode("utf-8")
                    datos=dato.split('$')
                    self.procData(datos)
                  
            
            except Exception as e:
                print(e)

            time.sleep(1)

    def procData(self, data):
        puntero=data[0]
        if puntero =="POZO1":
            print("data pozo1")

        elif puntero =="POZO2":
            print("data pozo1")

        elif puntero =="POZO3":
            print("data pozo1")

        elif puntero =="TEMP1":
            print("data pozo1")

        elif puntero =="TEMP2":
            print("data pozo1")

        elif puntero =="TEMP3":
            print("data pozo1")
   

    


        
           

           
           
           
           



