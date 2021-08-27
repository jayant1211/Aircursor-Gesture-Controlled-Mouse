##Calculations and evaluation of mouse gesture
import HandDetctionModule as hdm
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    org = frame.copy()
    x,y,frame= hdm.detectHand(frame)
    cords = hdm.detectCase(x,y)
    print(cords)

    for i in range(0,len(cords)):
        frame = cv2.circle(frame, cords[i], 5, (0, 0, 255), 2)
    #x,y,z = hdm.detectCase()
    #print("x : ",x,"y : ",y,"z : ",z)
    #dump1, dump2  = hdm.detectCase(x,y)
    #frame = cv2.circle(cv2.circle(frame,dump2,5,(0,0,255),2),(dump1),5,(0,0,255),2)
    cv2.imshow("hello",frame)
    cv2.imshow("hfb",org)
    if cv2.waitKey(5) & 0xFF == 27:
        break


cap.release()
