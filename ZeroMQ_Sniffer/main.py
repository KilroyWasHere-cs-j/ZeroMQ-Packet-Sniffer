import datetime
import tkinter as tk
import windowParams

import basicStreamer
import specificStreamer


t = tk.Tk()
bS = basicStreamer.BasicStream()
sS = specificStreamer.SpecificStreamer()

# Class so store window parameters not a cheap white phosphorus joke
wp = windowParams.Params()


def exit():
    t.destroy()
    exit(1)


def start_stream():
    print("Starting video stream")
    stream()


def createButton(window, button_text, width, command):
    button = tk.Button(window, text=button_text, width=width, command=command)
    button.pack()


def load_ui():
    t.title = wp.title
    t.geometry(wp.geo)

    createButton(t, wp.exitBTN.name, wp.exitBTN.width, exit)
    createButton(t, wp.startStreamBTN.name, wp.startStreamBTN.width, start_stream)

    t.mainloop()


def getTime():
    return datetime.datetime.now()


def stream():
    print("Reading in video")
    print("Kilroy Was Here")
    bS.Stream()


def main():
    print("Loading UI")
    load_ui()


if __name__ == "__main__":
    main()
