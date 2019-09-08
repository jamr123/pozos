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
            nivel1=int(data[1])
            print(nivel1)

        elif puntero =="POZO2":
            print("data pozo2")

        elif puntero =="POZO3":
            print("data pozo3")

        elif puntero =="TEMP1":
            print("data T1")

        elif puntero =="TEMP2":
            print("data T2")

        elif puntero =="TEMP3":
            print("data T3")
   
    def valorInstrumentacion(self,data):
        sen=data[0]
        ri_min=data[1]
        ri_max=data[2]
        rp_min=data[3]
        rp_max=data[4]
        try:
            x=self.readInputCorriente(sen)
            
            
            rangoInstrumentacion=ri_max-ri_min
            rangoProceso=rp_max-rp_min
            rirp=rangoInstrumentacion/rangoProceso
            val=((ri_max-x)/rirp)-rp_max
            val=val*-1
            return val
            
        except Exception as e:
            return 0
    


        
           

           
           
           
           



