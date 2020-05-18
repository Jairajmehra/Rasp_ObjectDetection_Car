
from time import sleep
from pathlib import Path
import cv2, os, threading


from ObjectDetectionClass import ObjectDetection
from ServerClass import Server
import sys

import keyboard
if __name__ == "__main__":
    server_thread = Server("192.168.137.1",8161)
    server_thread.start()
    object_detection_thread = ObjectDetection(3)
    object_detection_thread.start()


