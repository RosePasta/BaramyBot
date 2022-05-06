# @ 2022.05.06 Misoo Kim (hanul1546@gmail.com, misoo12@skku.edu)
# # This program prints out the screenshot for the user 
# #  to check if the location is correct for using the BaramyBot.

import pyautogui

image = pyautogui.screenshot('./saved_image.jpg', region=(0, 0, 750, 450))
