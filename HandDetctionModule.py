'''
*********APPROACH*********
#Step1
Detect hand--->yes--->step2
-------------->no---->continue
    detectHand()

#Step2
Case I: Single tip
    Implement Mouse Pointer Movement--->movement()

Case II: Joint
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

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


def detectHand(img):
    i = 0
    x_locs = []
    y_locs = []
    z_locs = []
    with mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5) as hands:
        img = cv2.flip(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 1)
        result = hands.process(img)
        height, width = img.shape[:2]
        if not result.multi_hand_landmarks:
            return x_locs,y_locs,cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        else:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS,mp_drawing_styles.get_default_hand_landmarks_style(),mp_drawing_styles.get_default_hand_connections_style())
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

        return x_locs,y_locs,cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

def detectCase(x,y):
    result = ['close','close','close','close','close']
    # ratio is a gpod idea as hnd distance may vary
    # 0.3>open
    #------ 0.4 definetly open finger
    #not implemented !=21
    ratio = []
    arr = len(x)
    final = []
    sum=0
    if arr==21:
        for i in range (1,6):
            ratio.append((y[i*4]-y[0]))
            sum= sum+ratio[i-1]
    ratio = np.array(ratio)
    ratio = ratio/sum

    for i in range(0,len(ratio)):
        if(ratio[i]>0.4):
            result[i] = 'open'
        if(ratio[i]>0.3):
            result[i] = 'open'
        if(ratio[i]<0.1):
            result[i] = 'close'
    #print(ratio)
    print(result)