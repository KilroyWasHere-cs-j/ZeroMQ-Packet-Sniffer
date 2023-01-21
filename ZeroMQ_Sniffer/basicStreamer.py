import imagezmq
import datetime
import cv2


class BasicStream:
    def __init__(self):
        self.image_hub = imagezmq.ImageHub()

    # Get current datetime private because I'm the only one who gets to know the time
    def __getTime(self):
        return datetime.datetime.now()

    # Send OK
    def sendOK(self):
        self.image_hub.send_reply(b"OK")

    # Streams video
    def Stream(self):
        while True:
            name, frame = self.image_hub.recv_image()
            cv2.imshow(name, frame)  # 1 window for each RPi

            cv2.waitKey(1)
            self.sendOK()
