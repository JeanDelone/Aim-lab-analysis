"""
Point of this, is to make a lot of screenshots for training set.
While positives have to be carefully selected, negatives don't, so I will
just make a looot of screenshots for negatives
"""

import pyautogui
import os
import random
from win32api import GetSystemMetrics
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

width_of_ss = random.randint(250,350)
height_of_ss = random.randint(250,350)
starting_x = random.randint(0,1920)
starting_y = random.randint(0,1080)

time.sleep(1)
path = os.path.join(os.path.dirname(__file__))
for i in range(200):
    time.sleep(0.2)
    width_of_ss = random.randint(250,350)
    height_of_ss = random.randint(250,350)
    starting_x = random.randint(0,1920)
    starting_y = random.randint(0,1080)
    while not (starting_x + width_of_ss <= width and starting_y + height_of_ss <= height):
        width_of_ss = random.randint(250,350)
        height_of_ss = random.randint(250,350)
        starting_x = random.randint(0,1920)
        starting_y = random.randint(0,1080)
    random_big_num = random.randint(0,9999999999)
    pyautogui.screenshot(path + f"/screenshoth{random_big_num}.png", region = (starting_x, starting_y,width_of_ss, height_of_ss))