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
    
    
    

    def __init__(self):
        try:
            self.auth()                                
            #self.deviceFind()
            #self.configVariables()
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
           self.token=response.json().token
           print(self.token)
        elif response.status_code == 404:
            print('Not Found.')
        
        
    def deviceFind(self):
        dev=json.dumps({"":""})
        data='POST$https://industrial.api.ubidots.com/api/v1.6/devices/'+config.UBIDOTS_NAME_DEVICE+'/$'+self.token+'$'+dev
        ds=self.readSerial(data)
        self.variables = 0

    def configVariables(self):
        for dato in config.UBIDOTS_VAR_NAMES:
                self.lecturas[dato]=self.getVariable(dato)
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
        
    def getVariable(self,varName):
        
        try:
            
            url=config.HTTP_VALUE+config.UBIDOTS_NAME_DEVICE+'/'+varName
            data2='GET$'+url+'$'+self.token
            ds2=self.readSerial(data2)
            print(ds2)
            ds1=ds2['last_value']
            ds=ds1['value']
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

    
        



