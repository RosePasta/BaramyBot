# @ 2022.05.06 Misoo Kim (hanul1546@gmail.com, misoo12@skku.edu)
# # This program sends the line message when detecting the dead signal from the Baram Yeon.

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

def main(ACCESS_TOKEN, wait_time):
    print("ACCESS TOKEN : ", ACCESS_TOKEN)
    print("Waiting time : ", wait_time)

    notify = LineNotify(ACCESS_TOKEN)

    # 1. Load signal images
    # signal_image_names = ['dead_message', 'ghost_status', 'go_revive', 'hp_mp_bar', 'revive']
    # TODO: 'hp_mp_bar': Low accuracy, so filtering out it.
    signal_image_names = ['dead_message', 'ghost_status', 'go_revive',  'revive']
    signal_images = []
    # Ground truth positions for each piece
    gt_position_list = [[263, 95], [259, 242], [580, 143], [371, 242]]
    for name in signal_image_names:
        img_piece = cv.imread('./signal_images/'+name+'.png',cv.IMREAD_COLOR)
        signal_images.append(img_piece)

    # 2. Real-time detection
    err_rt = 10
    previous_detect = 0
    while 1:
        # 2.1. Saving a screenshot image
        image = pyautogui.screenshot('./saved_image.jpg', region=(0, 0, 750, 450))
        img_frame = np.array(image)
        img_frame = cv.cvtColor(img_frame, cv.COLOR_RGB2BGR)
        meth = 'cv.TM_CCOEFF'
        method = eval(meth)
        
        # 2.2. Mapping pieces on the image
        detecting_results = []
        for i, signal_img in enumerate(signal_images):
            result = cv.matchTemplate(signal_img, img_frame, method)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

            top_left1, top_left2 = max_loc[0], max_loc[1]
            gt_x1, gt_x2 = gt_position_list[i][0], gt_position_list[i][1]
            
            if gt_x1-err_rt <= top_left1 and top_left1 <= gt_x1+err_rt \
                and gt_x2-err_rt <= top_left2 and top_left2 <= gt_x2 + err_rt:
                detecting_results.append(signal_image_names[i])            
            else:
                continue

        if len(detecting_results) > 1:
            previous_detect += 1
            print("Detect "+' '.join(detecting_results), datetime.datetime.now())
            notify.send("Detect "+' '.join(detecting_results), "./saved_image.jpg")
        else:
            print("NO PROBLEM", datetime.datetime.now())

        time.sleep(wait_time)
        
# INPUT: ACCESS_TOKEN, waiting_time
## ACCESS_TOKEN: Please receive the token from the https://notify-bot.line.me/en/.
##               The guide line is https://engineering.linecorp.com/ko/blog/line-notify-with-node-js-python-1-basic/
## waiting_time: Waiting time until next screen identification.
##                The longer it is, the slower it identifies, but the lower the overhead.
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Please two inputs (Access token for the line notify and waiting second)")
        print("For example: python main.py fGopUv12ixB 30")
    elif len(sys.argv) == 3:        
        ACCESS_TOKEN = sys.argv[1]
        waiting_time = sys.argv[2]
        try: 
            waiting_time = int(sys.argv[2])
            main(ACCESS_TOKEN, int(waiting_time))
        except:
            print("The waiting time should be INTEGER. but you input ", sys.argv[2])
        
        
            

