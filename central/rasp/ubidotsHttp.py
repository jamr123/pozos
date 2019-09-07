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

    pozo_1=[
            config.UBIDOTS_POZO_1_NiVEL_1:0,
            config.UBIDOTS_POZO_1_PRESION_1:0,
            config.UBIDOTS_POZO_1_CAUDAL_1:0,
            ]
    pozo_2=[
            config.UBIDOTS_POZO_2_NiVEL_1,
            config.UBIDOTS_POZO_2_PRESION_1,
            config.UBIDOTS_POZO_2_CAUDAL_1,
           ]
    pozo_3=[
            config.UBIDOTS_POZO_3_NiVEL_1,
            config.UBIDOTS_POZO_3_PRESION_1,
            config.UBIDOTS_POZO_3_PRESION_2,
            config.UBIDOTS_POZO_3_CAUDAL_1,
            config.UBIDOTS_POZO_3_CAUDAL_2,
           ]
    temperaturas=[
                config.UBIDOTS_TEMPERATURA_1,
                config.UBIDOTS_TEMPERATURA_2,
                config.UBIDOTS_TEMPERATURA_3,
                ]
    
    
    

    def __init__(self):
        try:
            self.auth()                                
            self.deviceFind()
            self.configVariables()
            #self.stop_threads =False

            #thread = threading.Thread(target=self.sync, args=())
            #thread.daemon = True                            
            #thread.start()
            

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
        for dato in config.VARS_POZO_1:
               self.pozo_1[dato]=getVariable(config.UBIDOTS_POZO_1,dato)
               time.sleep(1)
        for dato in config.VARS_POZO_2:
               self.pozo_1[dato]=getVariable(config.UBIDOTS_POZO_2,dato)
               time.sleep(1)
        for dato in config.VARS_POZO_3:
               self.pozo_1[dato]=getVariable(config.UBIDOTS_POZO_3,dato)
               time.sleep(1)
        for dato in config.VARS_TEMPERATURAS:
               self.pozo_1[dato]=getVariable(config.UBIDOTS_TEMPERATURAS,dato)
               time.sleep(1)
                

        
    def actualizarVal(self, varName, value):
        
            data =json.dumps( {"value": value,"timestamp": math.trunc(time.time())*1000})

            try:
               
                url=config.HTTP_VALUE+config.UBIDOTS_NAME_DEVICE+'/'+varName+'/values/'
                data2='POST$'+url+'$'+self.token +'$'+data
                ds2=self.readSerial(data2)
                print(ds2)
                return ds2
            except Exception as e:
                print(e)    
        
    def getVariable(self,device,varName):
        
        try:
            uriHttp=config.URI_DEVICE+device+'/'+varName+'/'
            response=requests.post(uriHttp,headers={'X-Auth-Token': self.token})
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
            
            self.transmision=True
            for dato in self.lecturas:
                self.actualizarVal(dato,self.lecturas[dato])
                time.sleep(1)
            
            self.transmision=False
            print(self.lecturas)
            time.sleep(config.REPORT_TIMER)     
            
    def auth2(self):
        data='TOKEN$'+config.HTTP_CREATE_TOKEN+'$'+config.UBIDOTS_API_KEY
        self.token=tk['token']

    
        



