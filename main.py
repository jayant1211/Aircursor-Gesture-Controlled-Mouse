##Calculations and evaluation of mouse gesture
import HandDetctionModule as hdm
import cv2
import numpy as np
import  math
import autopy

cap = cv2.VideoCapture(0)
cap.set(3, 960) #camera resolution,values should be same in interpolation
cap.set(4, 540)

reducedFrame = 100

screenW,screenH = autopy.screen.size()

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

    cv2.rectangle(frame,(reducedFrame+20,reducedFrame-80),(960-reducedFrame-20,540-reducedFrame-120),(255,255,0),1) #-

    if len(cords)==1:
        frame = cv2.circle(frame, cords[0], 5, (0, 255, 0), 2)
        #print("size ",autopy.screen.size())
        #print("scale ",autopy.screen.scale())
        x1,y1 = float(cords[0][0]),float(cords[0][1])
        #Convert Coordinates
        x3 = np.interp(x1, (reducedFrame+20, 960 - reducedFrame-20), (0, screenW))  #np.interplot maps one range to another desired range, point, original range, desired range
        y3 = np.interp(y1, (reducedFrame-80, 540 - reducedFrame-120), (0, screenH))

        #MOve Mouse
        if x3<screenW:
            if y3<screenH:
                pass
            else:
                y3=screenH-1
        else:
            if y3<=screenH:
                x3=screenW-1
            else:
                y3,x3 = screenH-1,screenW-1

        try:
            autopy.mouse.move(x3,y3)
        except:
            print("points out of bounds : ",x3,y3)

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
    #cv2.resize(frame, (640, 480))
    cv2.imshow("hello",frame)
    #cv2.imshow("hfb",org)
    if cv2.waitKey(5) & 0xFF == 27:
        break


cap.release()
