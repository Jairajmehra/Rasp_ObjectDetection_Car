import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)

class Path:
    def __init__(self, left, right):
        self.LEFT = left
        self.RIGHT = right
        
    def Setup(self):
        gpio.setup(self.LEFT, gpio.IN)
        gpio.setup(self.RIGHT, gpio.IN)
        
    def Exit(self):
        gpio.cleanup()
    
    def TellPath(self):
        if(not gpio.input(self.LEFT) and not gpio.input(self.RIGHT)):
            return "s"
        
        elif((not gpio.input(self.LEFT)) and (gpio.input(self.RIGHT))):
            return "r"
        
        elif( (gpio.input(self.LEFT)) and (not gpio.input(self.RIGHT))):
            return "l"
        
        elif( gpio.input(self.LEFT) and  gpio.input(self.RIGHT)):
            return "f"
