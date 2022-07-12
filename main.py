import numpy as np
import cv2 as cv
from mss import mss
from PIL import Image

mon = {'left': 0, 'top': 0, 'width': 1920, 'height': 1080}

with mss() as sct:
    while True:
        screenShot = sct.grab(mon)
        img = Image.frombytes(
            'RGB', 
            (screenShot.width, screenShot.height), 
            screenShot.rgb, 
        )
        img = np.array(img)
        img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
        cv.imshow('whole screen capture', img)
        if cv.waitKey(33) & 0xFF in (
            ord('q'), 
            27, 
        ):
            break