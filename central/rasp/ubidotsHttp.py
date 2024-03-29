import requests
import config
from ubidots import ApiClient
import threading
import logging
import time
import math
import json



class Ubidots:
    token=None

    pozos={
            config.UBIDOTS_POZO_1_NiVEL_1:0,
            config.UBIDOTS_POZO_1_NiVEL_2:0,
            config.UBIDOTS_POZO_1_PRESION_1:0,
            config.UBIDOTS_POZO_1_PRESION_2:0,
            config.UBIDOTS_POZO_1_CAUDAL_1:0,
            config.UBIDOTS_POZO_1_CAUDAL_2:0,
            config.UBIDOTS_POZO_2_NiVEL_1:0,
            config.UBIDOTS_POZO_2_NiVEL_2:0,
            config.UBIDOTS_POZO_2_PRESION_1:0,
            config.UBIDOTS_POZO_2_PRESION_2:0,
            config.UBIDOTS_POZO_2_CAUDAL_1:0,
            config.UBIDOTS_POZO_2_CAUDAL_2:0,
            config.UBIDOTS_POZO_3_NiVEL_1:0,
            config.UBIDOTS_POZO_3_NiVEL_2:0,
            config.UBIDOTS_POZO_3_PRESION_1:0,
            config.UBIDOTS_POZO_3_PRESION_2:0,
            config.UBIDOTS_POZO_3_CAUDAL_1:0,
            config.UBIDOTS_POZO_3_CAUDAL_2:0,
           }
    temperaturas={
                config.UBIDOTS_TEMPERATURA_1:0,
                config.UBIDOTS_TEMPERATURA_2:0,
                config.UBIDOTS_TEMPERATURA_3:0,
    }
    estanques={
            config.UBIDOTS_ESTANQUE_1_NiVEL_1:0,
            config.UBIDOTS_ESTANQUE_1_NiVEL_2:0,
            config.UBIDOTS_ESTANQUE_1_PRESION_1:0,
            config.UBIDOTS_ESTANQUE_1_PRESION_2:0,
            config.UBIDOTS_ESTANQUE_1_CAUDAL_1:0,
            config.UBIDOTS_ESTANQUE_1_CAUDAL_2:0,
    }
    
    
    

    def __init__(self):
        print("ubidots")
        
        try:
           
            self.auth()
            print("auth")                               
            self.deviceFind()
            print("devices") 
            self.configVariables()
            print("variables")
            self.stop_threads =False

            thread = threading.Thread(target=self.sync, args=())
            thread.daemon = True                            
            thread.start()

            thread2 = threading.Thread(target=self.auth2, args=())
            thread2.daemon = True                            
            thread2.start()
            

        except Exception as e:
            print(e)
        
    
    def threadCancel(self):
        self.stop_threads =True

        
    def auth(self):
        response=requests.post(config.URI_CREAR_TOKEN, headers={'x-ubidots-apikey': config.UBIDOTS_API_KEY})
        if response.status_code == 201:
           self.token=response.json()
           self.token=self.token['token']
        elif response.status_code == 404:
            print('Not Found.')
        
        
    def deviceFind(self):
        for device in config.VARS_DEVICES:
            uriHttp=config.URI_DEVICE+device+'/'
            response=requests.post(uriHttp,headers={'X-Auth-Token': self.token})
            if response.status_code == 201:
                print("device creado")
            elif response.status_code == 404:
                print('Not Found.')
            time.sleep(1)

    def configVariables(self):
        for dato in config.VARS_POZOS:
               self.pozos[dato]=self.getVariable(config.UBIDOTS_POZOS,dato)
               time.sleep(1)
        for dato in config.VARS_ESTANQUES:
               self.estanques[dato]=self.getVariable(config.UBIDOTS_ESTANQUES,dato)
               time.sleep(1)
               
        for dato in config.VARS_TEMPERATURAS:
               self.temperaturas[dato]=self.getVariable(config.UBIDOTS_TEMPERATURAS,dato)
               time.sleep(1)
                

        
    def actualizarVal(self, device, varName, value):
        
            data ={"value": value,"timestamp": math.trunc(time.time())*1000}
            try:
                uriHttp=config.URI_DEVICE+device+'/'+varName+'/values/'
                response=requests.post(uriHttp,headers={'X-Auth-Token': self.token},json=data)
                if response.status_code == 201:
                    print("variable creada")
                elif response.status_code == 404:
                    print('Not Found.')
            except Exception as e:
                print(e)
                  
        
    def getVariable(self,device,varName):
        
        try:
            uriHttp=config.URI_DEVICE+device+'/'+varName+'/'
            response=requests.get(uriHttp,headers={'X-Auth-Token': self.token})
            if response.status_code == 200:
                res=response.json()
                res=res['last_value']
                res=res['value']
                return res
            elif response.status_code == 404:
                return 0
            time.sleep(1)
            
            return ds
        except Exception as e:
            print(e)

    
    def sync(self):
        while True: 
            try:
                print("ACT>>>>>>>>>>>>>>>>>>>>>")
                self.transmision=True
                print(self.pozos)
                print(self.estanques)
                print(self.temperaturas)
                for dato in config.VARS_POZOS:
                        self.actualizarVal(config.UBIDOTS_POZOS,dato,self.pozos[dato])
                        time.sleep(1)

                for dato in config.VARS_ESTANQUES:
                        self.actualizarVal(config.UBIDOTS_ESTANQUES,dato,self.estanques[dato])
                        time.sleep(1)

                for dato in config.VARS_TEMPERATURAS:
                        self.actualizarVal(config.UBIDOTS_TEMPERATURAS,dato,self.temperaturas[dato])
                        time.sleep(1)
                
                self.transmision=False
                time.sleep(config.REPORT_TIMER)
            except Exception as e:
                print(e)     
            
    def auth2(self):
        while True:
            time.sleep(3600)
            self.auth()

    
        



