# @ 2022.05.06 Misoo Kim (hanul1546@gmail.com, misoo12@skku.edu)
# # This program sends the line message for checking the ready-to-use BaramyBot.

# pip install line_notify
# pip install pyautogui
# pip install opencv-python

from line_notify import LineNotify
import cv2 as cv
import numpy as np
import pyautogui
import time
import datetime
import sys

def main(ACCESS_TOKEN):
    print("ACCESS TOKEN : ", ACCESS_TOKEN)

    notify = LineNotify(ACCESS_TOKEN)
    notify.send("Hello! Ready to use BaramyBot!", "./saved_image.jpg")
        
# INPUT: ACCESS_TOKEN, waiting_time
## ACCESS_TOKEN: Please receive the token from the https://notify-bot.line.me/en/.
##               The guide line is https://engineering.linecorp.com/ko/blog/line-notify-with-node-js-python-1-basic/
## waiting_time: Waiting time until next screen identification.
##                The longer it is, the slower it identifies, but the lower the overhead.
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please input Access token for the line notify")
        print("For example: python line_test.py fGopT4h32ixB")
    elif len(sys.argv) == 2:        
        ACCESS_TOKEN = sys.argv[1]
        main(ACCESS_TOKEN)
        
        
            

