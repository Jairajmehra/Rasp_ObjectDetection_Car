
import threading
import RPi.GPIO as gpio
from PathClass import Path
from CarClass import Car

class Track (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        gpio.setmode(gpio.BCM)
        self.path = Path(16,12)    
        self.path.Setup()
        self.car = Car()
        self.car.Setup()
        self.Stop = False
        
    def run(self):
        while(self.Stop == False):
            self.move = self.path.TellPath()
            if(self.move=='f'):
                self.car.Forward(0.01)
            elif(self.move=='l'):
                self.car.Left(0.01)
            elif(self.move=='r'):
                self.car.Right(0.01)
            else:
                self.car.Stop()
        
        


