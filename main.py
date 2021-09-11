##Calculations and evaluation of mouse gesture
import HandDetctionModule as hdm
import cv2
import numpy as np
import  math
import autopy
import time

cap = cv2.VideoCapture(0)
cap.set(3, 960) #camera resolution,values should be same in interpolation
cap.set(4, 540)

holdFlag = "Off"

reducedFrame = 100
smoothening = 6
plocX,plocY = 0,0

#holdFlag =0

screenW,screenH = autopy.screen.size()

def isTouching(p0,p1):
    dist = math.sqrt(pow(p0[0]-p1[0],2)+pow(p0[1]-p1[1],2))
    #print(dist) #distance deeps below 25 if its touching, above 25 is open for both thumb-index, index-middle
    if dist<35:
        return 1
    else:
        #return dist
        return 0

def caseMovement(frame,x1,y1):
    for i in range(0, len(cords)):
        frame = cv2.circle(frame, cords[i], 5, (0, 255, 0), 2)
    # Convert Coordinates
    x3 = np.interp(x1, (reducedFrame + 30, 960 - reducedFrame - 30), (0, screenW))  # np.interplot maps one range to another desired range, point, original range, desired range
    y3 = np.interp(y1, (reducedFrame - 80, 540 - reducedFrame - 130), (0, screenH))

    # MOve Mouse
    if x3 < screenW:
        if y3 < screenH:
            pass
        else:
            y3 = screenH - 1
    else:
        if y3 <= screenH:
            x3 = screenW - 1
        else:
            y3, x3 = screenH - 1, screenW - 1
    global plocY,plocX
    x3 = plocX + (x3 - plocX) / smoothening
    y3 = plocY + (y3 - plocY) / smoothening

    try:
        autopy.mouse.move(x3, y3)
    except:
        print("points out of bounds : ", x3, y3)

    plocX, plocY = x3, y3

def caseLeft():
    autopy.mouse.click(autopy.mouse.Button.LEFT, delay = None)

def caseRight():
    autopy.mouse.click(autopy.mouse.Button.RIGHT, delay = None)

def leftToggleOn(frame,x,y):
    print("holding : implement toggle")
    autopy.mouse.toggle(autopy.mouse.Button.LEFT,True)
    caseMovement(frame,x,y)

def leftToggleOff():
    print("not holding : implement toggle off")
    autopy.mouse.toggle(autopy.mouse.Button.LEFT,False)


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

    if len(x) == 21:
        thumb,index,middle,ring,pinky = (x[4],y[4]),(x[8],y[8]),(x[12],y[12]),(x[16],y[16]),(x[20],y[20])

    cv2.rectangle(frame,(reducedFrame+30,reducedFrame-80),(960-reducedFrame-30,540-reducedFrame-130),(255,255,0),1) #-

    if len(cords) != 3 and holdFlag == "On":
        leftToggleOff()

    if len(cords)==1:
        x1, y1 = float(cords[0][0]), float(cords[0][1])
        caseMovement(frame,x1,y1)
        #print("size ",autopy.screen.size())
        #print("scale ",autopy.screen.scale())

    elif len(cords)==2:
        if(isTouching(cords[0],cords[1])):
            if cords[0] == thumb :   #check if one of the oneper finger is thumb
                if cords[1] == index: #check if another is index
                    caseRight()#right button

                else:
                    pass
            elif cords[0]==index: #check if one of the oneper finger is index
                if cords[1] == middle: #check if another is middle
                    caseLeft()#left button
                    #time.sleep()
                else:
                    caseMovement(frame,cords[0][0],cords[0][1])
            else:
                caseDefault(frame)

        else:
            x1, y1 = float(x[8]), float(y[8])  #if thumb and index are open, then thumb would be at 0 iundex hence
            caseMovement(frame,x1, y1)

    elif len(cords)==3:
        print("entered loop")
        if cords[0] == index and cords[1] == middle and cords[2] == ring:
            print("left toggle  on")
            holdFlag = "On"
            leftToggleOn(frame,cords[0][0],cords[0][1])

    else:
        caseDefault(frame)

    #cv2.putText(frame, str(int(instance)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
    #           (255, 0, 0), 3)

    #x,y,z = hdm.detectCase()
    #print("x : ",x,"y : ",y,"z : ",z)
    #dump1, dump2  = hdm.detectCase(x,y)
    #frame = cv2.circle(cv2.circle(frame,dump2,5,(0,0,255),2),(dump1),5,(0,0,255),2)
    #cv2.resize(frame, (640, 480))
    cv2.imshow("2",frame)
    org = cv2.flip(cv2.resize(org,(600,300)),1)
    cv2.imshow("1",org)
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()
