import cv2 as cv
import numpy as np
import os
import time

path = os.path.join(os.path.dirname(__file__))


footage = cv.VideoCapture(path + "/Videos/gridshot 1.mp4")

haar_cascade = cv.CascadeClassifier(path + "/haarcascade-ball.xml")
haar_cascade2 = cv.CascadeClassifier(path + "/haarcascade-ball3.xml")

# THIS IS HARDCODED FOR NOW
mouse_click_position = (1800,900)
mouse_clicked = False
click_counter = 0
frames = 0
when_mouse_clicked = []



def clicker_check(input, position, mouse_clicked, click_counter):
    B, G, R = input[position[1], position[0]]
    if B >= 200 & R >= 200 & G <= 30:
        if mouse_clicked == False:
            click_counter += 1
        mouse_clicked = True
        cv.putText(input, "mouse clicked", (1700,800), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
    else:
        mouse_clicked = False
    cv.putText(input, f"click counter: {click_counter}", (1550,700), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)


while True:
    _, frame = footage.read()
    # frame = cv.resize(frame, (frame.shape[1]//2, frame.shape[0])//2)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame2 = frame.copy()



    balls_rect = haar_cascade.detectMultiScale(frame, scaleFactor = 1.1, minNeighbors = 8)
    for (x,y,w,h) in balls_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (255,0,255), thickness = 2)
    
    balls_rect2 = haar_cascade2.detectMultiScale(frame2, scaleFactor = 1.1, minNeighbors = 8)
    for (x,y,w,h) in balls_rect2:
        cv.rectangle(frame2, (x,y), (x+w, y+h), (255,0,255), thickness = 2)


    B, G, R = frame[mouse_click_position[1], mouse_click_position[0]]
    if B >= 200 & R >= 200 & G <= 30:
        if mouse_clicked == False:
            click_counter += 1
            when_mouse_clicked.append(frames)
        mouse_clicked = True
        cv.putText(frame, "mouse clicked", (1700,800), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
    else:
        mouse_clicked = False
    cv.putText(frame, f"click counter: {click_counter}", (1550,700), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)



    # clicker_check(frame, mouse_click_position, mouse_clicked, click_counter)
    cv.imshow("Video", frame)
    cv.imshow("Video 2", frame2)
    # time.sleep(0.02)
    frames += 1
    if cv.waitKey(20) & 0xFF==ord("q"):
        break
    

footage.release()
cv.destroyAllWindows()