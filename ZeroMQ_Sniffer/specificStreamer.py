import cv2
import zmq
import socket
import numpy as np


class params:
    height = 376
    width = 672
    channels = 3
    frame_name = "Frame"

    def setHeight(self, val):
        self.height = val

    def setWidth(self, val):
        self.width = val

    def setChannel(self, val):
        self.channels = val

    def setFrameName(self, val):
        self.frame_name = val


class SpecificStreamer:
    def __init__(self, lookat):
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.connect(lookat)
        socket.setsockopt(zmq.SUBSCRIBE, b"image")

    def Stream(self):
        while True:
            [address, img_data] = socket.recv_multipart()
            # print(address)

            img_array = np.frombuffer(img_data, dtype=np.uint8)
            img = img_array.reshape(params.height, params.width, params.channels)
            # #
            cv2.imshow(params.frame_name, img)
            # #
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break