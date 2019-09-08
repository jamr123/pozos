import time
import serial
import threading
import config
import ubidotsHttp

ubi=ubidotsHttp.Ubidots()

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
            nivel1=valorInstrumentacion(config.POZO_1_S1,int(data[1]),)
            print(nivel1)
            nivel2=valorInstrumentacion(config.POZO_1_S2,int(data[2]),)
            print(nivel2)
            presion1=valorInstrumentacion(config.POZO_1_S3,int(data[3]),)
            print(presion1)
            presion2=valorInstrumentacion(config.POZO_1_S4,int(data[4]),)
            print(presion1)
            caudal1=data[5]
            caudal2=data[6]

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
   
    def valorInstrumentacion(self,calibracion,val):
        
        ri_min=calibracion[0]
        ri_max=calibracion[1]
        rp_min=calibracion[2]
        rp_max=calibracion[4]
        try:
            x=self.readInputCorriente(val)
            
            
            rangoInstrumentacion=ri_max-ri_min
            rangoProceso=rp_max-rp_min
            rirp=rangoInstrumentacion/rangoProceso
            val=((ri_max-x)/rirp)-rp_max
            val=val*-1
            return val
            
        except Exception as e:
            return 0
    

    def readInputCorriente(self,value):
        adcMax=3723
        mA=20
        resolucion=20/3723
        corriente=value*resolucion
        return corriente
        
           

           
           
           
           



