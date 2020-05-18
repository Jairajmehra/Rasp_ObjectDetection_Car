import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
from time import sleep


class Car:
    def __init__(self):
        self.LEFT1 = 20 
        self.LEFT2 = 21
        self.RIGHT1 = 6
        self.RIGHT2 = 13
    
    def Setup(self):
        gpio.setup(self.LEFT1, gpio.OUT)
        gpio.setup(self.LEFT2, gpio.OUT)
        gpio.setup(self.RIGHT1, gpio.OUT)
        gpio.setup(self.RIGHT2, gpio.OUT)
    
    
    def Stop(self):
        gpio.output(self.LEFT1, gpio.LOW)
        gpio.output(self.LEFT2, gpio.LOW)
        gpio.output(self.RIGHT1, gpio.LOW)
        gpio.output(self.RIGHT2, gpio.LOW)

    def Forward(self,delay):
        gpio.output(self.RIGHT2, gpio.HIGH)
        gpio.output(self.LEFT2, gpio.HIGH)
        sleep(delay)
        self.Stop()
    
    def Back(self, delay):
        gpio.output(self.RIGHT1, gpio.HIGH)
        gpio.output(self.LEFT1, gpio.HIGH)
        sleep(delay)
        self.Stop()

    def Right(self, delay):
        gpio.output(self.RIGHT2, gpio.HIGH)
        sleep(delay)
        self.Stop()
    
    
    def Left(self, delay):
        gpio.output(self.LEFT2, gpio.HIGH)
        sleep(delay)
        self.Stop()
        
    def Exit(self):
        self.Stop()
        gpio.cleanup()
