##Calculations and evaluation of mouse gesture
import HandDetctionModule as hdm
import cv2
import numpy as np
import  math


cap = cv2.VideoCapture(0)

cap.set(3, 720)
cap.set(4, 1280)

def isTouching(p0,p1):
    dist = math.sqrt(pow(p0[0]-p1[0],2)+pow(p0[1]-p1[1],2))
    #print(dist) #distance deeps below 25 if its touching, above 25 is open for both thumb-index, index-middle
    if dist<35:
        return 1
    else:
        #return dist
        return 0

def caseDefault(frame):
    for i in range(0, len(cords)):
        frame = cv2.circle(frame, cords[i], 5, (0, 0, 255), 2)

while True:
    _, frame = cap.read()
    org = frame.copy()
    x,y,frame= hdm.detectHand(frame)
    cords = hdm.detectCase(x,y)
    print(len(cords))
    print(cords)

    if len(cords)==1:
        frame = cv2.circle(frame, cords[0], 5, (0, 255, 0), 2)

    elif len(cords)==2:
        if(isTouching(cords[0],cords[1])):
            for i in range(0, len(cords)):
                frame = cv2.circle(frame, cords[i], 5, (255, 0, 0), 2)
        else:
            caseDefault(frame)

        #check touch:"
            #if yes:
                #check double tap:
                    #implement left click
                #check long tap:
                    #implement right click
                #no touching:
                    #implement movement

    else:
        caseDefault(frame)

    #x,y,z = hdm.detectCase()
    #print("x : ",x,"y : ",y,"z : ",z)
    #dump1, dump2  = hdm.detectCase(x,y)
    #frame = cv2.circle(cv2.circle(frame,dump2,5,(0,0,255),2),(dump1),5,(0,0,255),2)
    cv2.imshow("hello",cv2.resize(frame,(640,360)))
    #cv2.imshow("hfb",org)
    if cv2.waitKey(5) & 0xFF == 27:
        break


cap.release()
