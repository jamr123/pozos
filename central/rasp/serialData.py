import time
import serial
import threading
import config
import ubidotsHttp

ubi=ubidotsHttp.Ubidots()

# configure the serial connections (the parameters differs on the device you are connecting to)
#ser =serial.Serial('/dev/ttyAMA0', 115200, timeout=1)
#ser =serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser =serial.Serial('/dev/ttyACM0', 9600, timeout=1)

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
            d1=int(data[1])
            if d1>0:
                nivel1=self.valorInstrumentacion(config.POZO_1_S1,d1)
                nivel1=config.POZO_1_INSTALACION_NIVEL_1 - nivel1
                nivel1=float("{0:.2f}".format(nivel1))
                ubi.pozos[config.UBIDOTS_POZO_1_NiVEL_1]=nivel1
                #print(nivel1)
            else:
                d1=0

            d2=int(data[2])
            if d2>0:   
                nivel2=self.valorInstrumentacion(config.POZO_1_S2,d2)
                nivel2=config.POZO_1_INSTALACION_NIVEL_2 - nivel2
                nivel2=float("{0:.2f}".format(nivel2))
                ubi.pozos[config.UBIDOTS_POZO_1_NiVEL_2]=nivel2
                #print(nivel2)
            else:
                d2=0
            d3=int(data[3])
            if d3>0:
                presion1=self.valorInstrumentacion(config.POZO_1_S3,d3)
                presion1=float("{0:.2f}".format(presion1))
                ubi.pozos[config.UBIDOTS_POZO_1_PRESION_1]=presion1
                #print(presion1)
            else:
                d3=0
            d4=int(data[4])
            if d4>0:
                presion2=self.valorInstrumentacion(config.POZO_1_S4,d4)
                presion2=float("{0:.2f}".format(presion2))
                ubi.pozos[config.UBIDOTS_POZO_1_PRESION_2]=presion2
                #print(presion2)
            else:
                d4=0
            
            caudal1=int(data[5])
            ubi.pozos[config.UBIDOTS_POZO_1_CAUDAL_1]=caudal1
            caudal2=int(data[6])
            ubi.pozos[config.UBIDOTS_POZO_1_CAUDAL_2]=caudal2



        elif puntero =="POZO2":
            #print("data pozo2")
            d11=int(data[1])
            if d11>0:
                nivel11=self.valorInstrumentacion(config.POZO_2_S1,d11)
                nivel11=config.POZO_2_INSTALACION_NIVEL_1 - nivel11
                nivel11=float("{0:.2f}".format(nivel11))
                ubi.pozos[config.UBIDOTS_POZO_2_NiVEL_1]=nivel11
                #print(nivel11)
            else:
                d11=0

            d12=int(data[2])
            if d12>0:   
                nivel12=self.valorInstrumentacion(config.POZO_2_S2,d12)
                nivel12=config.POZO_2_INSTALACION_NIVEL_2 - nivel12
                nivel12=float("{0:.2f}".format(nivel12))
                ubi.pozos[config.UBIDOTS_POZO_2_NiVEL_2]=nivel12
                #print(nivel12)
            else:
                d12=0
            d13=int(data[3])
            if d13>0:
                presion11=self.valorInstrumentacion(config.POZO_2_S3,d3)
                presion11=float("{0:.2f}".format(presion11))
                ubi.pozos[config.UBIDOTS_POZO_2_PRESION_1]=presion11
                #print(presion11)
            else:
                d13=0
            d14=int(data[4])
            if d14>0:
                presion12=self.valorInstrumentacion(config.POZO_2_S4,d14)
                presion12=float("{0:.2f}".format(presion12))
                ubi.pozos[config.UBIDOTS_POZO_2_PRESION_2]=presion12
                #print(presion12)
            else:
                d14=0
            
            caudal11=int(data[5])
            ubi.pozos[config.UBIDOTS_POZO_2_CAUDAL_1]=caudal11
            caudal12=int(data[6])
            ubi.pozos[config.UBIDOTS_POZO_2_CAUDAL_2]=caudal12

        elif puntero =="POZO3":
           
            d21=int(data[1])
            if d21>0:
                nivel21=self.valorInstrumentacion(config.POZO_3_S1,d21)
                nivel21=config.POZO_3_INSTALACION_NIVEL_1 - nivel21
                nivel21=float("{0:.2f}".format(nivel21))
                ubi.pozos[config.UBIDOTS_POZO_3_NiVEL_1]=nivel21
                
            else:
                d21=0

            d22=int(data[2])
            if d22>0:   
                nivel22=self.valorInstrumentacion(config.POZO_3_S2,d22)
                nivel22=config.POZO_3_INSTALACION_NIVEL_2 - nivel22
                nivel22=float("{0:.2f}".format(nivel22))
                ubi.pozos[config.UBIDOTS_POZO_3_NiVEL_2]=nivel22
                
            else:
                d22=0
            d23=int(data[3])
            if d23>0:
                presion21=self.valorInstrumentacion(config.POZO_3_S3,d23)
                presion21=float("{0:.2f}".format(presion21))
                ubi.pozos[config.UBIDOTS_POZO_3_PRESION_1]=presion21
                
            else:
                d23=0
            d24=int(data[4])
            if d24>0:
                presion22=self.valorInstrumentacion(config.POZO_3_S4,d24)
                presion22=float("{0:.2f}".format(presion22))
                ubi.pozos[config.UBIDOTS_POZO_3_PRESION_2]=presion22
                #print(presion22)
            else:
                d24=0
            
            caudal21=int(data[5])
            ubi.pozos[config.UBIDOTS_POZO_3_CAUDAL_1]=caudal21
            caudal22=int(data[6])
            ubi.pozos[config.UBIDOTS_POZO_3_CAUDAL_1]=caudal22

        elif puntero =="ESTANQUE1":
            d31=int(data[1])
            if d31>0:
                nivel31=self.valorInstrumentacion(config.ESTANQUE_1_S1,d31)
                nivel31=config.ESTANQUE_1_INSTALACION_NIVEL_1 - nivel31
                nivel31=float("{0:.2f}".format(nivel31))
                ubi.estanques[config.UBIDOTS_ESTANQUE_1_NiVEL_1]=nivel31
                #print(nivel1)
            else:
                d31=0

            d32=int(data[2])
            if d32>0:   
                nivel32=self.valorInstrumentacion(config.ESTANQUE_1_S2,d32)
                nivel31=config.ESTANQUE_1_INSTALACION_NIVEL_2 - nivel32
                nivel32=float("{0:.2f}".format(nivel32))
                ubi.estanques[config.UBIDOTS_ESTANQUE_1_NiVEL_2]=nivel32
                #print(nivel2)
            else:
                d32=0
            d33=int(data[3])
            if d33>0:
                presion31=self.valorInstrumentacion(config.ESTANQUE_1_S3,d33)
                presion31=float("{0:.2f}".format(presion31))
                ubi.estanques[config.UBIDOTS_ESTANQUE_1_PRESION_1]=presion31
                #print(presion1)
            else:
                d33=0
            d34=int(data[4])
            if d34>0:
                presion32=self.valorInstrumentacion(config.ESTANQUE_1_S4,d34)
                presion32=float("{0:.2f}".format(presion32))
                ubi.estanques[config.UBIDOTS_ESTANQUES_1_PRESION_2]=presion32
                #print(presion2)
            else:
                d4=0
            
            caudal31=int(data[5])
            ubi.estanques[config.UBIDOTS_ESTANQUE_1_CAUDAL_1]=caudal31
            caudal32=int(data[6])
            ubi.estanques[config.UBIDOTS_ESTANQUES_1_CAUDAL_2]=caudal32



        elif puntero =="TEMPERATURA1":
            #print("data T1")
            d41=int(data[1])
            ubi.temperaturas[config.UBIDOTS_TEMPERATURA_1]=d41

        elif puntero =="TEMPERATURA2":
            #print("data T2")
            d51=int(data[1])
            ubi.temperaturas[config.UBIDOTS_TEMPERATURA_2]=d51

        elif puntero =="TEMPERATURA3":
            #print("data T3")
            d61=int(data[1])
            ubi.temperaturas[config.UBIDOTS_TEMPERATURA_3]=d61
   
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
        
           

           
           
           
           



