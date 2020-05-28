import socket
import cv2
import pickle
import threading
import struct
import os
from StoreSearchClass import store_Search

class Server(threading.Thread):
    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.Host = host
        self.Port = port
        self.data = b""
        self.payload_size = struct.calcsize(">L")
        self.Store_Search = store_Search(os.path.join(os.getcwd(), 'images'))
        self.Stop = True

    def run(self):
        self.s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.bind((self.Host,self.Port))
        self.s.listen(1)
        print('Socket now listening')
        self.conn, self.addr = self.s.accept()
        print("Connection recieved")
        self.Stop = False
        self.FetchData()

    def FetchData(self):
        frameCounter = 0

        while(self.Stop == False):
            frameCounter +=1
            while len(self.data) < self.payload_size:
                self.data += self.conn.recv(16000)
            packed_msg_size = self.data[:self.payload_size]

            self.data = self.data[self.payload_size:]
            msg_size = struct.unpack(">L", packed_msg_size)[0]

            while len(self.data) < msg_size:
                self.data += self.conn.recv(16000)
            frame_data = self.data[:msg_size]

            self.data = self.data[msg_size:]
            frame= pickle.loads(frame_data, fix_imports=True, encoding="bytes")
            frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
            cv2.imshow('Real Time video feed', frame)
            cv2.waitKey(1)
            if(frameCounter == 120):
                print("saving To images Folder")
                self.Store_Search.SaveNotDetected(frame)
                frameCounter = 0
            
        self.s.close()
        return

            

        