import cv2
import imagezmq
import datetime


def getTime():
    return datetime.datetime.now()


def stream():
    image_hub = imagezmq.ImageHub()
    print("Reading in video")
    print("Kilroy Was Here")
    while True:  # show streamed images until Ctrl-C
        rpi_name, image = image_hub.recv_image()

        # font which we will be using to display FPS
        font = cv2.FONT_HERSHEY_SIMPLEX


        cv2.imshow(rpi_name, image)  # 1 window for each RPi

        # used to record the time when we processed last frame
        # we will be subtracting it to get more accurate result
        print("Frame at {0}".format(getTime()))

        cv2.waitKey(1)

        image_hub.send_reply(b'OK')

def main():
    print("Ready to handle video")
    stream()


if __name__ == "__main__":
    main()
