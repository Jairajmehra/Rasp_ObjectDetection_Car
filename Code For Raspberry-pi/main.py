
from ClientClass import Client
from LineFollowClass import Track

if __name__ == "__main__":
    client_thread = Client("192.168.137.1",8161)
    client_thread.start()
    track_thread = Track()
    track_thread.start()