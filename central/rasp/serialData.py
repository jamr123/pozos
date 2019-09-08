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
        print(data)
        if puntero =="POZO1":
            print("data pozo1")
            d1=int(data[1])
            if d1>0:
                nivel1=self.valorInstrumentacion(config.POZO_1_S1,d1)
                nivel1=float("{0:.2f}".format(nivel1))
                print(nivel1)
            else:
                d1=0

            d2=int(data[2])
            if d2>0:   
            nivel2=self.valorInstrumentacion(config.POZO_1_S2,d2)
            nivel2=float("{0:.2f}".format(nivel2))
            print(nivel2)
            else:
                d2=0
            d3=int(data[3])
            if d3>0:
                presion1=self.valorInstrumentacion(config.POZO_1_S3,d3)
                presion1=float("{0:.2f}".format(presion1))
                print(presion1)
            else:
                d3=0
            d4=int(data[4])
            if d4>0:
                presion2=self.valorInstrumentacion(config.POZO_1_S4,d4)
                presion2=float("{0:.2f}".format(presion2))
                print(presion1)
            else:
                d4=0
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
        rp_max=calibracion[3]
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
        
           

           
           
           
           



