# methods for capturing image and video for WildLiveCam
# Devi 2020

from picamera import PiCamera
from time import sleep
from datetime import datetime
from logToFile import logToFile
import os
# this allows for a newline character but still shows file as empty
MIN_SIZE = 6

# take picture command
def take_pic():
    t = datetime.now()
    stamp = t.strftime("%m%y%H%M%S")

    camera = PiCamera()
    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/WildLive/photos/'+stamp+'.jpg')
    #add try/except to send error alert 
    camera.stop_preview()
    camera.close()

    t = datetime.now()
    logtime = t.strftime("%m%y%H%M%S")
    logToFile(logtime, 'saved image ' + stamp)

# listen for command
def listen():
    if os.stat("sms_input.txt").st_size > MIN_SIZE:
        print("opening file")

        # if it has open it
        with open("sms_input.txt", 'r+') as filestream:
            # read and parse commands
            line = filestream.readline()
            cmd_list = line.split(",")
            cmd_list[-1] = cmd_list[-1].rstrip("\n")
            for i in range(len(cmd_list)):
                cmd_list[i] = cmd_list[i].strip()
            print(cmd_list)

            # check if photo is in the commands list
            if 'photo' in cmd_list:
                print("taking photo")
                take_pic()

            # send file out

            # wipe file for next command
            filestream.truncate(0)
    else:
        print("file empty")
        sleep(3)

# vars
cmd_list = []

# runs continuously
while (True):
    # check if the file has been written to
    listen()
    





