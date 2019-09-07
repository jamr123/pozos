import time
import serial
import threading

# configure the serial connections (the parameters differs on the device you are connecting to)
#ser =serial.Serial('/dev/ttyAMA0', 115200, timeout=1)
ser =serial.Serial('/dev/ttyUSB0', 9600, timeout=1)


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
                    print(s)
                  
            
            except Exception as e:
                print(e)

            time.sleep(1)

   

    


        
           

           
           
           
           



