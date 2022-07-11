import cv2 as cv
import numpy as np
import os
import time

path = os.path.join(os.path.dirname(__file__))


footage = cv.VideoCapture(path + "/Videos/gridshot 1.mp4")



# THIS IS HARDCODED FOR NOW
mouse_click_position = (1800,900)
mouse_clicked = False
mouse_clicks_count = 0

while True:
    _, frame = footage.read()
    # frame = cv.resize(frame, (frame.shape[1]//2, frame.shape[0])//2)

    B, G, R = frame[mouse_click_position[1], mouse_click_position[0]]
    if B >= 200 & R >= 200 & G <= 30:
        print("mouse_clicked")
        cv.putText(frame, "mouse clicked", (1700,800), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
    else:
        print(f"actual color: ({B}, {R})")
        cv.putText(frame, "not clicked", (1700,800), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)



    cv.imshow("Video", frame)
    time.sleep(0.02)

    if cv.waitKey(20) & 0xFF==ord("q"):
        break

footage.release()
cv.destroyAllWindows()