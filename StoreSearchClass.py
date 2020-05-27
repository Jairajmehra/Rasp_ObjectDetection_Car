import cv2, os
from PIL import Image
from pathlib import Path
import uuid

class store_Search:
    def __init__(self, location):
        self.Location = location

    def SaveDetected(self, frame, name):
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        path = os.path.join(self.Location, (name+str(uuid.uuid1())+".png"))
        Image.fromarray(img).save(path,"PNG" )
    
    def SaveNotDetected(self, frame):
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        path = os.path.join(self.Location, (str(uuid.uuid1())+".png"))
        Image.fromarray(img).save(path)

    
    def search(self, name):      
        items = Path(self.Location).glob(f'*{name}&*.png')
        items = sorted(items, key=os.path.getctime)[:3]
        names = []
        for x in items:
            names.append(os.path.basename(x))
        return names
     