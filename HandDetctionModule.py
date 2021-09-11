'''
*********APPROACH*********
#Step1
Detect hand--->yes--->step2
-------------->no---->continue
    detectHand()

#Step2
Case I: Single tip
    Implement Mouse Pointer Movement--->movement()

Case II: Two tips and Joint
    detectCase():
        SubCase 1: Twice tap in Short Duration
            Implement Left Click----------->leftClick()
        SubCase 2: Hold for more than 2 Sec
            Implement Right Click---------->rightClick()
        SubCase 3: Hold and move
            Implement Drag if applicable--->drag()

Case III: Anything else
    Continue to next Frame
'''
import mediapipe as mp
import numpy as np
import cv2
import mediapipe as mp
import math

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


def detectHand(img):
    ##case 1 finger open
    ##case 2 two finger
    ##case 3 rejection case
    i = 0
    x_locs = []
    y_locs = []
    z_locs = []
    with mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5) as hands:
        img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 1)
        white = np.full(img.shape, 255, dtype=np.uint8)
        result = hands.process(img)
        height, width = img.shape[:2]
        if not result.multi_hand_landmarks:
            #return x_locs,y_locs,cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            return x_locs, y_locs, white

        else:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS,mp_drawing_styles.get_default_hand_landmarks_style(),mp_drawing_styles.get_default_hand_connections_style())
                mp_drawing.draw_landmarks(white, hand_landmarks, mp_hands.HAND_CONNECTIONS,mp_drawing_styles.get_default_hand_landmarks_style(),mp_drawing_styles.get_default_hand_connections_style())

                for point in mp_hands.HandLandmark:
                    normalizedLandmark = hand_landmarks.landmark[point]
                    pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                              normalizedLandmark.y,
                                                                                              width, height)

                    try:
                            x_locs.append(pixelCoordinatesLandmark[0])
                            y_locs.append(pixelCoordinatesLandmark[1])
                    except:
                        continue
                    #z_locs.append(pixelCoordinatesLandmark[2])
                    #i=i+1
                    #print(normalizedLandmark)
                '''for i in range (0,24):
                    locs.append((hand_landmarks.landmark[i].x * width,
                                 hand_landmarks.landmark[i].y * height,
                                 hand_landmarks.landmark[i].z))'''

        #return x_locs,y_locs,cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        return x_locs,y_locs,white

def detectCase(x,y):
    tip_minus_middle = []
    status = ["Close","Close","Close","Close","Close"]
    arr = len(x)
    if arr==21:
        cords = list(zip(x,y))
        for i in range (1,6):
            tip_minus_middle.append(-1*(y[i*4]-y[4*i-1]))

    #print(tip_minus_middle)

    for i in range (0,len(tip_minus_middle)):
        if i == 0:
            #check pinky ans thumb
            #print(x[20]-x[4])       #positive is right front or left back
                                    # negative is right back or left front
            ortn = x[20]-x[4]
            flag_thumb_3_4 = x[4] - x[3]
            if  ortn>-30:  #-30 for case if hand is close and thumb overlaps pinky, in orientation its -250 so it should be fine
                if flag_thumb_3_4 < 0:
                    print("desired",y[5]-y[4])
                    status[i] = "Open"
                else:
                    status[i] = "Close"
            else:
                if flag_thumb_3_4>0:
                    status[i] = "Open"
            
        elif tip_minus_middle[i]>=0:
            status[i]="Open"

    open = status.count("Open")
    status = np.array(status)


    open_index = np.where(status == "Open")[0]
    open_cords = []
    for i in open_index:
        open_cords.append(cords[4*(i+1)])
    #print(len(open_index))
    #print(open_cords)
    #case thumb and index finger
    if status[0]=='Open':
        xcentre = open_cords[0][0]-cords[8][0]
        if abs(xcentre)<20:
            if status[1]!='Open':
                status[1] = 'Open'
                open_cords.insert(1,cords[8])
    print(status)
    if status[0] == "Open":
        # print("",xcentre)
        print("ortn",ortn)
        print("flag_thumb_3_4",flag_thumb_3_4)
    return open_cords


'''def detectCase2(x,y):
    result = [0,0,0,0,0]
    result = np.array(result)
    # ratio is a gpod idea as hnd distance may vary
    # 0.3>open
    #------ 0.4 definetly open finger
    #not implemented !=21
    ratio = []
    cords = []
    arr = len(x)
    final = []
    sum=0
    if arr==21:
        cords = list(zip(x,y))
        for i in range (1,6):
            ratio.append((y[i*4]-y[0]))
            sum= sum+ratio[i-1]
    ratio = np.array(ratio)
    ratio = ratio/sum

    for i in range(0,len(ratio)):
        if(ratio[i]>0.4):
            result[i] = 3  #3 : deginately open
        elif(ratio[i]>0.3):
            result[i] = 2  #2 : open
        elif(ratio[i]>0.1):
            result[i] = 1  #1: probably open but no use
                           # 0 : close

    def whichFinger(*ele):
        finger = {0:"thumb",1: "index", 2: "middle", 3: "ring", 4: "pinky"}
        for i in ele:
            print(finger.get(i),"is open",end = " ")
        print('\n')

    def oneOpen(fingCord):
        #print("One Open",fingCord)
        whichFinger(fingCord)
        p0= cords[4*(fingCord+1)]
        return p0,None

    def twoOpen(fingCord1,fingCord2):
        #print("Two Open",fingCord1,fingCord2)
        print(4 * fingCord1,4 * fingCord2)
        p0,p1 = cords[4*(fingCord1+1)],cords[4*(fingCord2+1)]
        print("p1,p2 : ",p0,p1)
        whichFinger(fingCord1,fingCord2)
        dist = math.sqrt(pow(p0[0]-p1[0],2)+pow(p0[1]-p1[1],2))
        print(dist)
        return p0,p1

    threes = np.where(result == 3)[0]
    twos = np.where(result == 2)[0]

    open = len(threes)+len(twos)

    if open==1:
        if len(threes)==1:
            return oneOpen(threes[0])
        else:
            return oneOpen(twos[0])

    elif open==2:
        if len(twos)==2:
            return twoOpen(twos[0],twos[1])

        elif len(twos)==1:
            return twoOpen(twos[0],threes[0])

        else:
            return twoOpen(threes[0],threes[1])

    else:
        print("case reject")
        return None, None

    #print(cords)
    #print(ratio)
  #  print(result)'''