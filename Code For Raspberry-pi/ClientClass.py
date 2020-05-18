import cv2
import socket
import struct
import time
import pickle
import threading

class Client(threading.Thread):
    def __init__(self, ip, port):
        threading.Thread.__init__(self)
        self.encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        self.IP = ip
        self.PORT = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False
        
    def run(self):
        print("waiting for connection")
        self.client_socket.connect((self.IP, self.PORT))
        self.cam = cv2.VideoCapture(0)
        self.cam.set(3, 320)
        self.cam.set(4, 240)
        self.connected = True
        self.SendFrame()

    def SendFrame(self):
        while(self.connected):
            print("Sending Frame")
            ret, frame = self.cam.read()
            result, frame = cv2.imencode('.jpg', frame, self.encode_param)
            data = pickle.dumps(frame, 0)
            self.client_socket.sendall(struct.pack(">L", len(data)) + data)
        
